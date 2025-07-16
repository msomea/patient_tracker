from django.shortcuts import render, redirect
from tracker.models import Disease, PatientCount, AGE_GROUPS
from .forms import PatientEntryForm
from django.contrib import messages
from django.db.models import Sum, Max

def enter_patient_data(request):
    if request.method == 'POST':
        form = PatientEntryForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            for disease in Disease.objects.all():
                for age_code, _ in AGE_GROUPS:
                    male = form.cleaned_data.get(f"{disease.name}_{age_code}_male", 0) or 0
                    female = form.cleaned_data.get(f"{disease.name}_{age_code}_female", 0) or 0

                    record, created = PatientCount.objects.get_or_create(
                        disease=disease, date=date, age_group=age_code,
                        defaults={'male': male, 'female': female}
                    )
                    if not created:
                        record.male += male
                        record.female += female
                        record.save()
            messages.success(request, "Patient data saved successfully.")
            return redirect('enter_patient_data')
    else:
        form = PatientEntryForm()
    return render(request, 'tracker/enter_patient_data.html', {'form': form})


def patient_summary(request):
    totals = (
        PatientCount.objects
        .values('disease__name', 'age_group')
        .annotate(
            total_male=Sum('male'),
            total_female=Sum('female')
        )
        .order_by('disease__name', 'age_group')
    )

    overall_total = sum(t['total_male'] + t['total_female'] for t in totals)

    # 🔹 Get latest entry date
    last_entry = PatientCount.objects.aggregate(latest=Max('date'))['latest']

    return render(request, 'tracker/summary.html', {
        'totals': totals,
        'overall_total': overall_total,
        'last_entry': last_entry,
    })


def clear_patient_data(request):
    if request.method == "POST":
        PatientCount.objects.all().delete()
        messages.success(request, "🧹 All patient data has been deleted.")
    return redirect('enter_patient_data')
