import os
import subprocess
import time
import webbrowser

# 1. Set the project directory
project_dir = r"A:\PY\patient_tracker"

# 2. Change to the project directory
os.chdir(project_dir)

# 3. Start the Django development server in a new process
# Use creationflags to keep the server running in a separate terminal window (on Windows)
server_process = subprocess.Popen(
    ["python", "manage.py", "runserver"],
    creationflags=subprocess.CREATE_NEW_CONSOLE
)

# 4. Wait for 10 seconds to let the server start
print("⏳ Waiting 10 seconds for server to start...")
time.sleep(10)

# 5. Open the default web browser to the patient data entry page
url = "http://127.0.0.1:8000/enter/"
print(f"🌐 Opening browser at: {url}")
webbrowser.open(url)

print("✅ Server should be running in a new console window.")
