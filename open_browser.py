"""
Script to automatically take screenshots of the Django app for Coursera assignment.
Uses selenium/playwright or just opens browser URLs.
"""
import subprocess
import sys
import os
import time

# Open the admin site in the browser
admin_url = "http://127.0.0.1:8000/admin/"
course_url = "http://127.0.0.1:8000/"

print("Opening browser windows for screenshots...")
print("")
print("INSTRUCTIONS:")
print("1. Browser will open the Admin site at:", admin_url)
print("   - Login with: admin / admin123")
print("   - Take a screenshot (Win+Shift+S or Snipping Tool)")
print("   - Save as: 03-admin-site.png")
print("")
print("2. Browser will open the Course site at:", course_url)
print("   - Login with: testuser / test123")
print("   - Go to 'Introduction to Python' course")
print("   - Select 'x = 5' for Q1 and 'for' for Q2")
print("   - Submit the exam")
print("   - Take a screenshot of the Congratulations page")
print("   - Save as: 07-final.png")
print("")

# Open browser
subprocess.Popen(['start', admin_url], shell=True)
time.sleep(2)
subprocess.Popen(['start', course_url], shell=True)
