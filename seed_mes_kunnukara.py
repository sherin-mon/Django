import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ams_project.settings')
django.setup()

from admission_system.models import College, Course

def seed():
    college, created = College.objects.update_or_create(
        slug='mes-kunnukara',
        defaults={
            'name': 'MES T.O. Abdulla Memorial College, Kunnukara',
            'description': (
                'MES T.O. Abdulla Memorial College, Kunnukara, is a premier self-financing '
                'institution established in 2004 under the Muslim Education Society (MES). '
                'Affiliated to Mahatma Gandhi University, Kottayam, the college offers a '
                'diverse range of undergraduate and postgraduate programmes across Commerce, '
                'Management, Computer Applications, Psychology, and English.'
            ),
            'theme_color': '#1B5E20',
        }
    )
    print(f"{'Created' if created else 'Updated'}: {college.name}")

    courses = [
        # Commerce
        ('B.Com (Computer Applications)', 'Commerce integrated with practical IT skills — database, accounting software, and e-commerce.'),
        ('B.Com (Finance & Taxation)', 'In-depth study of financial management, GST, income tax, and corporate financial reporting.'),
        ('B.Com (Marketing)', 'Commerce programme with focus on market research, brand management, and consumer behaviour.'),
        ('B.Com (Co-operation)', 'Study of cooperative movement, cooperatives law, and community-centred business models.'),
        ('B.Com (Logistics Management)', 'Specialised commerce track in supply chain management, warehousing, and logistics operations.'),
        # Management & Technology
        ('BBA (Bachelor of Business Administration)', 'Foundation degree in corporate management, entrepreneurship, and strategic business planning.'),
        ('BBM (Bachelor of Business Management)', 'Applied management programme focusing on organisational behaviour and business operations.'),
        ('BCA (Bachelor of Computer Applications)', 'Three-year programme in software development, databases, networking, and web technologies.'),
        # Arts & Social Sciences
        ('B.Sc. Psychology', 'Scientific study of human behaviour, cognitive processes, and mental health fundamentals.'),
        ('B.A. English', 'Study of English language, literature, and communication for journalism, education, and media.'),
        # Postgraduate
        ('M.Com (E-Commerce)', 'Advanced commerce degree specialising in digital business, online marketing, and e-payment systems.'),
        ('M.Com (Finance & Taxation)', 'PG programme in advanced financial instruments, corporate taxation, and investment analysis.'),
        ('M.Sc. Psychology', 'Postgraduate study in clinical, counselling, and organisational psychology with research methodology.'),
    ]

    for name, desc in courses:
        _, c = Course.objects.update_or_create(
            college=college, name=name, defaults={'description': desc}
        )
        if c: print(f'  + {name}')

    print(f'\nDone — {len(courses)} courses seeded.')

if __name__ == '__main__':
    seed()
