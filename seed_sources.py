import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ams_project.settings')
django.setup()

from admission_system.models import ApplicationSource

sources = [
    "Social media",
    "Newspaper advertisement",
    "Digital marketing",
    "Agents",
    "Others"
]

for source_name in sources:
    obj, created = ApplicationSource.objects.get_or_create(name=source_name)
    if created:
        print(f"Created source: {source_name}")
    else:
        print(f"Source already exists: {source_name}")

print("Seeding complete.")
