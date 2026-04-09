import glob, re

files = glob.glob("/home/mohammed/Admission_Pro/admission_system/templates/admission_system/college_*.html")
for f in files:
    if "static" in f or "elims" in f or "base" in f:
        continue
    with open(f, 'r') as file:
        content = file.read()
    
    # Let's find the script block
    print(f"File: {f}")
    match = re.search(r'(function (goToStep|nextAppStep|nextStep)[^\{]*\{)(.*?)(\})', content, re.DOTALL)
    if match:
        func = match.group(0).split('\n')[:5]
        print("Function snippet:", "\n".join(func))
    else:
        print("No match")
    print("-" * 50)
