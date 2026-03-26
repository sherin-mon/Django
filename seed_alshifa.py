import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ams_project.settings')
django.setup()

from admission_system.models import College, Course

def seed_alshifa():
    # 1. Create College
    alshifa, created = College.objects.update_or_create(
        slug='alshifa',
        defaults={
            'name': 'Al Shifa College of Arts and Science',
            'description': 'A premier institution of higher learning in Malapuram, affiliated with the University of Calicut, dedicated to academic excellence and student success through (Hons.) programmes.',
            'theme_color': '#4B367C',
            'website_content': '<p>Al Shifa College of Arts & Science (ACAS) is a prominent institution providing value-based education. With modern facilities and a dedicated faculty, ACAS offers specialized Honours programmes designed to equip students for global challenges.</p>',
            'logo_url': 'https://www.alshifacollegeofartsandscience.ac.in/assets/images/logo.png' 
        }
    )
    if created:
        print(f"Created College: {alshifa.name}")
    else:
        print(f"Updated College: {alshifa.name}")

    # 2. Create Courses
    courses = [
        # Undergraduate (Hons.)
        ('BBA (Hons.)', 'Bachelor of Business Administration Honours programme focusing on modern management and leadership.'),
        ('BCA (Hons.)', 'Bachelor of Computer Applications Honours with focus on software development and technology.'),
        ('B.Sc. Artificial Intelligence (Hons.)', 'Specialized program in AI, Machine Learning, and Data Science.'),
        ('B.Sc. Psychology (Hons.)', 'Deep dive into human behavior and mental processes with practical exposure.'),
        ('B.Sc. Nutrition and Dietetics (Hons.)', 'Science of food and its impact on human health.'),
        ('B.Com. with Finance (Hons.)', 'Advanced commerce curriculum with specialization in financial management.'),
        ('B.Com. with Taxation (Hons.)', 'Comprehensive study of direct and indirect taxation systems.'),
        ('B.Com. with Computer Application (Hons.)', 'Integration of commerce principles with computer technology.'),
        ('B.A. English (Hons.)', 'In-depth study of literature and language proficiency.'),
        ('B.A. Economics (Hons.)', 'Advanced economic theories and data analysis techniques.'),
        # Postgraduate
        ('M.Sc. Clinical Psychology', 'Advanced study in therapeutic techniques and clinical assessment.'),
        ('M.Sc. Applied Psychology', 'Application of psychological principles in professional and social settings.')
    ]

    for name, desc in courses:
        course, c = Course.objects.update_or_create(
            college=alshifa,
            name=name,
            defaults={'description': desc}
        )
        if c:
            print(f"  Created Course: {name}")

if __name__ == "__main__":
    seed_alshifa()
