import os
import django
import urllib.parse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ams_project.settings')
django.setup()

from admission_system.models import College

general_logos = {
    "alshifa": "https://ui-avatars.com/api/?name=Al+Shifa&background=4B367C&color=fff&size=256&rounded=true&bold=true",
    "alazhar": "https://ui-avatars.com/api/?name=Al+Azhar&background=006400&color=fff&size=256&rounded=true&bold=true",
    "nirmala": "https://ui-avatars.com/api/?name=Nirmala+College&background=253E7D&color=fff&size=256&rounded=true&bold=true",
    "jbcmet": "https://ui-avatars.com/api/?name=JBCMET&background=1A237E&color=fff&size=256&rounded=true&bold=true",
    "mes-kunnukara": "https://ui-avatars.com/api/?name=MES+College&background=1B5E20&color=fff&size=256&rounded=true&bold=true",
    "elims": "https://ui-avatars.com/api/?name=ELIMS&background=0f172a&color=fff&size=256&rounded=true&bold=true",
}

print("Running Logo Update Script...")
updated = 0
for slug, url in general_logos.items():
    try:
        c = College.objects.get(slug=slug)
        c.logo_url = url
        c.save()
        print(f"Updated logo for {c.name}")
        updated += 1
    except College.DoesNotExist:
        pass

# Fallback for any others
for c in College.objects.all():
    if not c.logo_url:
        safe_name = urllib.parse.quote_plus(c.name)
        color = c.theme_color.replace('#', '') if c.theme_color else 'random'
        c.logo_url = f"https://ui-avatars.com/api/?name={safe_name}&background={color}&color=fff&size=256&rounded=true&bold=true"
        c.save()
        print(f"Generated fallback UI-Avatar for {c.name}")
        updated += 1

print(f"Done. Processed {updated} logos.")
