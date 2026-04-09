import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ams_project.settings')
django.setup()

from django.test import Client
from admission_system.models import Application, College, CREProfile, Student, Course
from django.urls import reverse

college = College.objects.first()
cre = CREProfile.objects.first()
student = Student.objects.first()
course = Course.objects.filter(college=college).first()

if not student:
    student = Student.objects.create(name="Test", email="test@example.com")
if not course:
    course = Course.objects.create(name="Test Course", college=college)

app, _ = Application.objects.get_or_create(
    student=student, 
    college=college, 
    course=course,
    defaults={'referred_by': cre, 'payment_status': 'Success'}
)

c = Client()
url = reverse('manual_payment', args=[app.id])
response = c.get(url)
print(f"Status: {response.status_code}")
print(f"Redirected to: {response.url}")
