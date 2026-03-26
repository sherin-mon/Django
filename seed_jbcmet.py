import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ams_project.settings')
django.setup()

from admission_system.models import College, Course

def seed_jbcmet():
    college, created = College.objects.update_or_create(
        slug='jbcmet',
        defaults={
            'name': 'Jai Bharath College of Management and Engineering Technology',
            'description': (
                'Jai Bharath College of Management and Engineering Technology (JBCMET), '
                'located in Vengola, Perumbavoor, Ernakulam, Kerala, is a premier technical '
                'institution established in 2009. Affiliated to APJ Abdul Kalam Technological '
                'University (KTU) and approved by AICTE, the college offers a rich portfolio '
                'of engineering, management, and technology programmes.'
            ),
            'theme_color': '#1A237E',
        }
    )
    print(f"{'Created' if created else 'Updated'}: {college.name}")

    courses = [
        # B.Tech Engineering
        ('[B.Tech] Computer Science & Engineering', 'Core computing, algorithms, data structures, and software engineering for the modern tech industry.'),
        ('[B.Tech] CSE – Artificial Intelligence & Machine Learning', 'Advanced AI and ML specialisation covering deep learning, neural networks, and intelligent systems.'),
        ('[B.Tech] CSE – Artificial Intelligence & Data Science', 'Data-driven engineering programme combining AI, big data analytics, and statistical modelling.'),
        ('[B.Tech] CSE – Internet of Things', 'Embedded systems, IoT architecture, sensor networks, and cloud integration for connected devices.'),
        ('[B.Tech] CSE – Cyber Security', 'Specialised programme in ethical hacking, network security, cryptography, and digital forensics.'),
        ('[B.Tech] Electronics & Communication Engineering', 'Signal processing, VLSI design, communications systems, and embedded electronics engineering.'),
        ('[B.Tech] Electrical & Electronics Engineering', 'Power systems, control engineering, renewable energy, and industrial automation.'),
        ('[B.Tech] Mechanical Engineering', 'Thermodynamics, manufacturing processes, design engineering, and CAD/CAM technologies.'),
        ('[B.Tech] Civil Engineering', 'Structural engineering, construction management, environmental engineering, and surveying.'),
        # Diploma
        ('[Diploma] Mechanical Engineering', 'Polytechnic diploma in mechanical systems, workshop practice, and industrial design.'),
        ('[Diploma] Civil Engineering', 'Diploma in construction technology, AutoCAD, and building materials.'),
        ('[Diploma] Electrical & Electronics Engineering', 'Polytechnic programme in electrical circuits, wiring, and industrial electronics.'),
        ('[Diploma] Automobile Engineering', 'Vehicle technology, engine mechanics, auto electronics, and service management.'),
        ('[Diploma] Computer Engineering', 'Practical computing, hardware maintenance, networking, and software applications.'),
        ('[Diploma] Cyber Forensics & Information Security', 'Digital investigation, cybercrime analysis, and information security fundamentals.'),
        # Management & Technology
        ('[MBA] Master of Business Administration', 'Two-year postgraduate management programme with specialisations in Finance, Marketing, and HR.'),
        ('[MCA] Master of Computer Applications', 'Advanced computing and full-stack software development for postgraduate tech professionals.'),
        ('[BCA] Bachelor of Computer Applications', 'Three-year UG programme in software development, databases, and web technologies.'),
        ('[BBA] Bachelor of Business Administration', 'Foundation degree in business management, entrepreneurship, and corporate operations.'),
    ]

    for name, desc in courses:
        _, c = Course.objects.update_or_create(
            college=college, name=name, defaults={'description': desc}
        )
        if c:
            print(f'  + {name}')

    print(f'\nDone — {len(courses)} courses seeded.')

if __name__ == '__main__':
    seed_jbcmet()
