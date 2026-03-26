import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ams_project.settings')
django.setup()

from admission_system.models import College, Course

def seed_nirmala():
    college, created = College.objects.update_or_create(
        slug='nirmala',
        defaults={
            'name': 'Nirmala College, Muvattupuzha',
            'description': (
                'Nirmala College, Muvattupuzha, is a prestigious co-educational institution '
                'affiliated to Mahatma Gandhi University, Kottayam. Established in 1965 and '
                'managed by the Diocese of Kothamangalam, the college offers a wide range of '
                'undergraduate, postgraduate, and doctoral programmes across arts, science, '
                'commerce, and management disciplines.'
            ),
            'theme_color': '#253E7D',
            'website_content': (
                '<p>Nirmala College, Muvattupuzha, stands as a centre of academic excellence '
                'in Kerala, offering holistic education rooted in Catholic values. '
                'As an autonomous college affiliated to Mahatma Gandhi University, '
                'the institution fosters critical thinking, research, and community development.</p>'
            ),
        }
    )
    action = 'Created' if created else 'Updated'
    print(f'{action} College: {college.name}')

    courses = [
        # Undergraduate – Arts & Commerce
        ('B.A. English Literature', 'Study of English language, literature, and critical analysis. Ideal for writers, educators, and communicators.'),
        ('B.A. Economics', 'In-depth study of macro/microeconomics, statistics, and econometrics for policy and finance careers.'),
        ('B.Com (Finance & Taxation)', 'Commerce degree with specialisation in financial management, accountancy, and Indian taxation systems.'),
        ('B.Com (Computer Application)', 'Commerce principles integrated with core computer application skills for modern business environments.'),
        ('B.Com (Travel & Tourism)', 'Commerce and hospitality curriculum tailored for the global travel and tourism industry.'),
        ('Bachelor of Tourism & Travel Management (BTTM)', 'Comprehensive degree in tourism operations, hospitality management, and travel marketing.'),
        # Undergraduate – Science & Technology
        ('B.Sc. Computer Science', 'Foundation in programming, data structures, algorithms, and software engineering practices.'),
        ('B.Sc. Mathematics', 'Pure and applied mathematics including calculus, algebra, statistics, and numerical methods.'),
        ('B.Sc. Physics', 'Core physics curriculum covering mechanics, optics, quantum theory, and lab practice.'),
        ('B.Sc. Chemistry', 'Study of organic, inorganic, and physical chemistry with advanced laboratory work.'),
        ('B.Sc. Botany', 'Plant biology, ecology, and biotechnology for careers in agriculture and life sciences.'),
        ('B.Sc. Zoology', 'Animal biology, ecology, and physiology with field and laboratory-based research.'),
        ('B.Sc. Statistics', 'Probability theory, statistical inference, data analysis, and actuarial applications.'),
        ('Bachelor of Computer Applications (BCA)', 'Practical-oriented degree in software development, web technologies, and database management.'),
        # Postgraduate
        ('M.Sc. Computer Science', 'Advanced computing, AI, machine learning, and research-oriented curriculum for tech innovators.'),
        ('M.Sc. Mathematics', 'Advanced mathematical theories, research methods, and applications in science and engineering.'),
        ('M.Com (Finance)', 'Postgraduate commerce with advanced study in corporate finance, investment banking, and taxation.'),
        ('Master of Computer Applications (MCA)', 'Two-year PG programme in software engineering, cloud computing, and enterprise application development.'),
        ('Master of Tourism Management (MTM)', 'Advanced study in tourism policy, destination management, and sustainable tourism practices.'),
        ('M.A. English', 'Literary theory, linguistics, creative writing, and advanced language studies at postgraduate level.'),
    ]

    for name, desc in courses:
        obj, c = Course.objects.update_or_create(
            college=college,
            name=name,
            defaults={'description': desc}
        )
        if c:
            print(f'  Created Course: {name}')

    print(f'\nDone! {len(courses)} courses seeded for {college.name}.')

if __name__ == '__main__':
    seed_nirmala()
