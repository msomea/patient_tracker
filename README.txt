# 🧾 Patient Tracker Django App

This is a Django-based application for entering and tracking daily patient data categorized by disease, age group, and gender.

---

## ⚙️ Setup Instructions

### 1. 📦 Install Requirements

Make sure you have Python and Django installed. You can install dependencies using:

```bash
pip install django

🏗️ Run Migrations
Set up your database schema by running the following commands:

python manage.py makemigrations
python manage.py migrate


🌱 Seed the Database with Diseases

This project uses a custom dynamic form based on diseases in the database. To populate the Disease table with initial values:
✅ Step-by-step
Open the seed_diseases.py file
Make sure this line is correctly configured:

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patient_tracker.settings")

Replace patient_tracker with your actual project folder name if different.


Run the script:

python seed_diseases.py

You should see output like:

🧹 Cleared all existing diseases.
✅ Added: Typhoid
✅ Added: Cholera
...
🎉 Done! Disease list has been replaced.


🚀 Run the Development Server

python manage.py runserver

Open your browser and go to:
http://127.0.0.1:8000/enter/
🔄 Updating Diseases

🔄 Updating Diseases Later

    Modify the new_seed_diseases.py list 

    Rerun the script:

python seed_diseases.py

⚠️ This will delete all existing diseases and replace them with the new list.



🛠 Troubleshooting

    No fields showing in form?

        Run migrations

        Seed diseases using the script above

    Getting errors about missing tables?

        Check that you've applied all migrations

    Form requires all fields?

        All fields are optional by default; user can enter only what’s needed

To delete all `PatientCount` entries without affecting diseases:


python manage.py clear_patient_data



✅ Full Project Directory Structure

patient_tracker/                ← Root folder
├── manage.py                   ← Django's CLI entry point
├── db.sqlite3                  ← SQLite database file (auto-created)
├── seed_diseases.py           ← Custom script to populate Disease table
├── README.md                  ← Project instructions and setup guide

├── patient_tracker/           ← Project folder (contains settings, URLs, etc.)
│   ├── __init__.py
│   ├── settings.py            ← Django settings file
│   ├── urls.py                ← Project-level URL routing
│   ├── asgi.py
│   └── wsgi.py

├── tracker/                   ← Your main Django app
│   ├── __init__.py
│   ├── admin.py               ← Admin interface config
│   ├── apps.py
│   ├── forms.py               ← Contains PatientEntryForm
│   ├── models.py              ← Disease, PatientCount, AGE_GROUPS
│   ├── tests.py
│   ├── urls.py                ← App-level URL routing (included in project urls.py)
│   ├── views.py               ← Logic for handling form display & submission
│   └── migrations/            ← Auto-generated DB schema migrations
│       ├── __init__.py
│       └── 0001_initial.py    ← First migration file (may vary)

├── templates/                 ← Template directory (global or per app)
│   └── enter_patient_data.html  ← The form template

└── static/                    ← (Optional) for static files like JS/CSS/images

