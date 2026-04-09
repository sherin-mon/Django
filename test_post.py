import requests
import uuid
import datetime

url = "http://127.0.0.1:8000/apply/st-andrews/60f9aead-9ed8-44c7-8617-1bcdadb7340e/"
payload = {
    'name': 'Test User',
    'email': 'testuser123@example.com',
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
files = {
    'doc_10th': ('test.txt', b'test', 'text/plain'),
    'doc_12th': ('test.txt', b'test', 'text/plain'),
    'doc_aadhar': ('test.txt', b'test', 'text/plain')
}

response = requests.post(url, data=payload, files=files)
print(f"Status Code: {response.status_code}")
if response.status_code != 200:
    print(response.text[:1000])
else:
    print("Redirected URL:", response.url)
