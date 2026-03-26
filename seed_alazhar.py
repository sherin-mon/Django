import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ams_project.settings')
django.setup()

from admission_system.models import College, Course

def seed_alazhar():
    # 1. Create College
    alazhar, created = College.objects.update_or_create(
        slug='alazhar',
        defaults={
            'name': 'Al Azhar Group of Institutions, Thodupuzha',
            'description': 'A massive educational ecosystem in Thodupuzha, Kerala, offering a wide array of professional and academic programmes across 12 institutions including Engineering, Arts & Science, Medical, and Dental sciences.',
            'theme_color': '#006400', # Emerald Green
            'website_content': '<p>Al-Azhar Group of Institutions is a premier educational hub established under the Noorul Islam Trust. With state-of-the-art infrastructure and a focus on holistic development, Al-Azhar provides a platform for students to excel in various disciplines from Medicine to Engineering.</p>',
            'logo_url': 'https://alazharthodupuzha.org/wp-content/uploads/2021/05/logo.png' 
        }
    )
    if created:
        print(f"Created College: {alazhar.name}")
    else:
        print(f"Updated College: {alazhar.name}")

    # 2. Create Courses
    courses = [
        # Engineering (Al-Azhar College of Engineering & Technology)
        ('[Engineering] B.Tech Computer Science & Engineering', 'Focus on software engineering, algorithms, and advanced computing.'),
        ('[Engineering] B.Tech AI & Machine Learning', 'Specialized track in Artificial Intelligence and ML architectures.'),
        ('[Engineering] B.Tech Computer Science (Cyber Security)', 'Advanced training in network security and digital forensics.'),
        ('[Engineering] B.Tech Civil Engineering', 'Core engineering discipline focusing on infrastructure and design.'),
        ('[Engineering] B.Tech Mechanical Engineering', 'Core focus on thermal, manufacturing, and design engineering.'),
        ('[Engineering] B.Tech Automobile Engineering', 'Specialized branch focusing on vehicle design and technology.'),
        ('[Engineering] B.Tech Biomedical Engineering', 'Integration of engineering principles with healthcare sciences.'),
        # Arts & Science (Al-Azhar College of Arts & Science)
        ('[Arts & Science] BBA', 'Bachelor of Business Administration for future corporate leaders.'),
        ('[Arts & Science] BCA', 'Bachelor of Computer Applications for software and IT careers.'),
        ('[Arts & Science] B.Com Finance & Taxation', 'Commerce degree with deep dive into accounting and tax law.'),
        ('[Arts & Science] B.Com Computer Application', 'Fusion of commerce principles with IT skills.'),
        ('[Arts & Science] B.Sc Computer Science', 'Pure computer science degree focusing on theoretical and practical computing.'),
        ('[Arts & Science] B.A English', 'Degree in English literature and language proficiency.'),
        ('[Arts & Science] M.Com Marketing & International Business', 'Postgraduate commerce degree for global business.'),
        # Medical & Allied (Al-Azhar Medical/Paramedical)
        ('[Medical] Bachelor of Physiotherapy (BPT)', 'Allied health program focusing on physical rehabilitation.'),
        ('[Medical] B.Sc Medical Laboratory Technology (B.Sc MLT)', 'Diagnostic medicine and laboratory sciences.'),
        ('[Medical] B.Sc Optometry', 'Degree in eye care and vision sciences.')
    ]

    for name, desc in courses:
        course, c = Course.objects.update_or_create(
            college=alazhar,
            name=name,
            defaults={'description': desc}
        )
        if c:
            print(f"  Created Course: {name}")

if __name__ == "__main__":
    seed_alazhar()
