import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patient_tracker.settings")  # ✅ Adjusted here
django.setup()

from tracker.models import Disease

diseases = ["Malaria", "Dengue", "Tuberculosis", "COVID-19", "Influenza"]

for name in diseases:
    obj, created = Disease.objects.get_or_create(name=name)
    if created:
        print(f"Added: {name}")
    else:
        print(f"Already exists: {name}")

print("✅ Done seeding diseases.")
