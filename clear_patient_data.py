import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patient_tracker.settings")  # Replace if needed
django.setup()

from tracker.models import PatientCount

# Delete all patient count records
deleted_count, _ = PatientCount.objects.all().delete()

print(f"🧹 Deleted {deleted_count} patient entries.")
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patient_tracker.settings")  # Replace if needed
django.setup()

from tracker.models import PatientCount

# Delete all patient count records
deleted_count, _ = PatientCount.objects.all().delete()

print(f"🧹 Deleted {deleted_count} patient entries.")
