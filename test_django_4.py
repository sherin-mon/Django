import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ams_project.settings')
django.setup()

from django.test import Client
from admission_system.models import CREProfile, College

cre = CREProfile.objects.first()
college = College.objects.first()

c = Client()
url = f"/apply/{college.slug}/{cre.cre_id}/"

payload = {
    'name': 'Test User',
    'email': 'testusernew3@example.com',
    'phone': '9876543210',
    'dob': '2000-01-01',
    'gender': 'M',
    'aadhar_number': '123456789012',
    'blood_group': 'B+',
    'category': 'General',
    'permanent_address': '123 Fake St',
    'correspondence_address': '123 Fake St',
    'state': 'Kerala',
    'city': 'Kochi',
    'father_name': 'Test Father',
    'father_mobile': '9876543210',
    'father_occupation': 'Business',
    'mother_name': 'Test Mother',
    'mother_mobile': '9876543210',
    'mother_occupation': 'Housewife',
    'guardian_name': 'Test Guardian',
    'guardian_mobile': '9876543210',
    'preferred_contact': 'Student',
    'course': '1',
    'addon_course': ''
}

import io
from django.core.files.uploadedfile import SimpleUploadedFile

f = SimpleUploadedFile("test.txt", b"file_content")
payload['doc_10th'] = f
payload['doc_12th'] = f
payload['doc_aadhar'] = f

response = c.post(url, data=payload)
if response.status_code == 200:
    content = response.content.decode('utf-8')
    print("Content string contains 'check-circle' (success message)?", "check-circle" in content)
    print("Content string contains 'alert-circle' (error message)?", "alert-circle" in content)
    
    # Just print the first error message div
    import re
    msg = re.search(r'<div[^>]*alert-circle[^>]*>(.*?)</div>', content, re.DOTALL)
    if msg: print("Error message found in HTML:", msg.group(1).strip())
elif response.status_code in [301, 302]:
    print("Redirected to:", response.url)
