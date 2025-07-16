# 🧾 Patient Tracker – Django Web Application  
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)  
![Django](https://img.shields.io/badge/django-4.x-green.svg)  
![License](https://img.shields.io/badge/license-MIT-orange.svg)  
A **Django-based web application** for tracking **daily patient data**, categorized by **disease, age group, and gender**.  
This tool is ideal for **healthcare facilities** to monitor patient trends, improve reporting, and maintain organized medical records.  
---
## 🚀 Features  

✅ **Dynamic Disease-based Form** – Automatically generates fields based on available diseases  
✅ **Categorized Data** – Tracks patients by disease, age group, and gender  
✅ **Quick Database Seeding** – Pre-populate the database with predefined diseases  
✅ **Lightweight Setup** – Uses SQLite by default, no complex configuration required  
✅ **Easily Extendable** – Add new diseases anytime with one command  

---

## 📸 Demo  

![Patient Tracker Demo](https://via.placeholder.com/1000x500.png?text=Patient+Tracker+UI+Mockup)  

---

## ⚙️ Installation & Setup  

### 1️⃣ Prerequisites  

- Python **3.8+**  
- Django **4.x+**  

Install Django if not installed:  

pip install django

### 2️⃣ Database Setup
Run migrations to create necessary tables:

python manage.py makemigrations
python manage.py migrate

### 3️⃣ Seed the Database with Diseases
The app uses a dynamic form based on diseases stored in the database. To populate the initial disease list:

Open seed_diseases.py and ensure this line is correct:

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patient_tracker.settings")
Replace patient_tracker with your actual project folder name if different.

Run the seeding script:

python seed_diseases.py
✅ Example output:

python-repl

✅ Added: Typhoid
✅ Added: Cholera
...
🎉 Done! Disease list has been replaced.

### 4️⃣ Run the Development Server
Start the server:

python manage.py runserver
Open your browser at:
👉 http://127.0.0.1:8000/enter/

### 🔄 Updating Diseases Later
Want to update the list of diseases?
Modify the disease list inside seed_diseases.py
Rerun the script:

python seed_diseases.py
### ⚠️ Warning: This will delete all existing diseases and replace them with the new list.

### 🛠 Troubleshooting
No fields showing in the form?
Ensure migrations are applied
Seed the database with diseases
Errors about missing tables?
Run python manage.py migrate
Form requires all fields?
All fields are optional by default; users can enter only what’s needed
Clear all patient data without deleting diseases:

python manage.py clear_patient_data

### 📂 Project Structure
patient_tracker/                ← Root folder
├── manage.py                   ← Django's CLI entry point
├── db.sqlite3                  ← SQLite database file
├── seed_diseases.py            ← Script to populate Disease table
├── README.md                   ← Project setup guide

├── patient_tracker/            ← Main Django project folder
│   ├── settings.py             ← Django settings
│   ├── urls.py                 ← Project-level URL routing
│   ├── asgi.py / wsgi.py       ← Deployment files
│   └── __init__.py

├── tracker/                    ← Main Django app
│   ├── models.py               ← Disease, PatientCount, AGE_GROUPS
│   ├── forms.py                ← PatientEntryForm
│   ├── views.py                ← Form display & submission logic
│   ├── urls.py                 ← App-level URL routing
│   ├── admin.py                ← Admin interface config
│   └── migrations/             ← Database schema migrations

├── templates/                  ← HTML templates
│   └── enter_patient_data.html ← Form template

└── static/                     ← Optional: JS, CSS, images

### ☁️ Deployment
🔹 Deploy on PythonAnywhere
Create a free account at https://www.pythonanywhere.com
Upload your project files
Create a virtual environment and install Django
Configure a new Web App and point it to patient_tracker/wsgi.py

🔹 Deploy on Heroku
Install Heroku CLI:
curl https://cli-assets.heroku.com/install.sh | sh
Create a Procfile with:
web: gunicorn patient_tracker.wsgi
Add a requirements.txt file (generate it using):
pip freeze > requirements.txt
Commit your code to GitHub and deploy:
heroku login
heroku create patient-tracker-app
git push heroku main

### 🗺️ Roadmap / Future Improvements
🔹 Add authentication & role-based access (e.g., admin vs. staff)
🔹 Implement detailed reports & visual analytics
🔹 Export patient data as CSV/Excel
🔹 Support for PostgreSQL or MySQL for production
🔹 API endpoints for external integration

### 📜 License
This project is licensed under the MIT License.
MIT License
Copyright (c) 2025 Raphael MSOMEA
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

### 🤝 Contributing
Pull requests are welcome!
If you’d like to suggest a feature or report a bug, open an issue.
Or contact me through msomearaphael@gmail.com

### 💡 Pro Tip: Fork this repo and deploy it easily to Heroku, PythonAnywhere, or Railway.

## Made with ❤️ using Django