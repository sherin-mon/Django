import os
import django
import pandas as pd
import math

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ams_project.settings')
django.setup()

from admission_system.models import College, Course, AddonCourse

def clean_name(name):
    if pd.isna(name):
        return None
    return str(name).strip()

def normalize(name):
    if not name:
        return ""
    import re
    # Remove punctuation like dots, commas, parentheses
    res = re.sub(r'[^a-zA-Z0-9\s]', '', str(name))
    # Convert to lowercase
    res = res.lower()
    # Replace common abbreviations anywhere they appear
    res = res.replace("bcom", "b com").replace("mcom", "m com")
    # Strip and collapse whitespace
    res = " ".join(res.split())
    return res

def process_campus_course_details():
    print("Processing CAMPUS-COURSE DETAILES (2).xlsx...")
    file_path = 'CAMPUS-COURSE DETAILES (2).xlsx'
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    df = pd.read_excel(file_path)
    # Strip spaces from column names
    df.columns = [c.strip() for c in df.columns]
    
    # Forward fill College and Course if they are merged in Excel
    df['College'] = df['College'].ffill()
    df['Course'] = df['Course'].ffill()

    added_count = 0
    for _, row in df.iterrows():
        college_name = clean_name(row.get('College'))
        course_name = clean_name(row.get('Course'))
        addon_name = clean_name(row.get('Add-on- Course'))

        if not college_name or not course_name or not addon_name:
            continue

        # Try to find college
        colleges = College.objects.all()
        target_college = None
        norm_college_name = normalize(college_name)
        for c in colleges:
            if norm_college_name in normalize(c.name):
                target_college = c
                break
        
        if not target_college:
            print(f"College not found: '{college_name}'")
            continue
        
        # Try to find course
        target_course = None
        norm_course_name = normalize(course_name)
        for c in Course.objects.filter(college=target_college):
            if norm_course_name in normalize(c.name):
                target_course = c
                break
            # Also try matching if target is an abbreviation in the name
            if f"({course_name.upper()})" in c.name:
                target_course = c
                break
        
        if not target_course:
            print(f"Course not found for {target_college.name}: '{course_name}'")
            continue
            
        # Create AddonCourse
        addon, created = AddonCourse.objects.get_or_create(
            course=target_course,
            name=addon_name
        )
        if created:
            added_count += 1
            print(f"Added '{addon_name}' to '{target_course.name}' ({target_college.name})")

    print(f"Added {added_count} addon courses from Campus file.")

def process_al_azhar_details():
    print("\nProcessing AL AZHAR- COURSE DETAILES.xlsx...")
    file_path = 'AL AZHAR- COURSE DETAILES.xlsx'
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    college = College.objects.filter(name__icontains="Al Azhar").first()
    if not college:
        print("Al Azhar college not found in DB.")
        return

    xls = pd.ExcelFile(file_path)
    added_count = 0
    for sheet_name in xls.sheet_names:
        print(f"  Processing sheet: {sheet_name}")
        df = xls.parse(sheet_name)
        
        # Let's try to detect columns by content
        main_course_col = None
        addon_course_col = None
        
        # Heuristic search for cols
        found = False
        for r in range(min(10, len(df))):
            for c in range(len(df.columns)):
                cell = str(df.iloc[r, c]).upper()
                if "ADD ON" in cell or "ADD-ON" in cell:
                    addon_course_col = c
                    if c > 0:
                        main_course_col = c - 1
                    start_row = r + 1
                    found = True
                    break
            if found: break
        else:
            main_course_col = 2
            addon_course_col = 3
            start_row = 1

        df_data = df.iloc[start_row:].copy()
        # ffill the main course col, but ONLY if it's not the addon col
        if main_course_col is not None:
             df_data.iloc[:, main_course_col] = df_data.iloc[:, main_course_col].ffill()
        
        for _, row in df_data.iterrows():
            m_course = clean_name(row.iloc[main_course_col]) if main_course_col is not None else None
            a_course = clean_name(row.iloc[addon_course_col]) if addon_course_col is not None else None
            
            if not m_course or not a_course or str(m_course).isdigit() or "ADD ON" in str(a_course).upper():
                continue
            
            # Match main course in DB
            norm_m_course = normalize(m_course)
            db_course = None
            for c in Course.objects.filter(college=college):
                if norm_m_course in normalize(c.name):
                    db_course = c
                    break
            
            if not db_course:
                continue
                
            addon, created = AddonCourse.objects.get_or_create(
                course=db_course,
                name=a_course
            )
            if created:
                added_count += 1
                print(f"    Added '{a_course}' to '{db_course.name}'")

    print(f"Added {added_count} addon courses from Al Azhar file.")

if __name__ == "__main__":
    process_campus_course_details()
    process_al_azhar_details()
