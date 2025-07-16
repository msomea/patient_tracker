import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patient_tracker.settings")  # Replace with your actual project name
django.setup()

from tracker.models import Disease

# ✅ Step 1: Delete all existing diseases
Disease.objects.all().delete()
print("🧹 Cleared all existing diseases.")

# ✅ Step 2: Define the new list of diseases
new_diseases = [
    "LOW BACK PAIN",
    "NECK PAIN",
    "STROKE",
    "ARTHRITIS",
    "SCIATICA",
    "ERB'S",
    "CLUBFOOT",
    "CEREBRAL PALSY",
]

# ✅ Step 3: Add new diseases
for name in new_diseases:
    Disease.objects.create(name=name)
    print(f"✅ Added: {name}")

print("🎉 Done! Disease list has been replaced.")
