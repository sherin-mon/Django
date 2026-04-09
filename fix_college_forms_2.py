import glob, re

files = glob.glob("/home/mohammed/Admission_Pro/admission_system/templates/admission_system/college_*.html")

validation_js = """function goToStep(step) {
        // If moving forward, validate current step
        const currentStepEl = document.querySelector('.step-content:not(.hidden)');
        if (currentStepEl) {
            const currentStepMatch = currentStepEl.id.match(/\\d+/);
            if (currentStepMatch) {
                const currentStep = parseInt(currentStepMatch[0]);
                if (step > currentStep) {
                    const inputs = currentStepEl.querySelectorAll('input, select, textarea');
                    for (let i = 0; i < inputs.length; i++) {
                        if (!inputs[i].checkValidity()) {
                            inputs[i].reportValidity();
                            return; // Stop and do not proceed
                        }
                    }
                }
            }
        }
"""

patched_files = []
for f in files:
    if "static" in f or "elims" in f or "base" in f:
        continue
    with open(f, 'r') as file:
        content = file.read()
    
    if "inputs[i].checkValidity()" in content:
        continue # Already patched or has it
        
    new_content = content.replace("function goToStep(step) {", validation_js)
    if new_content != content:
        with open(f, 'w') as file:
            file.write(new_content)
        patched_files.append(f)

print("Patched:", len(patched_files))
for f in patched_files:
    print("-", f)
