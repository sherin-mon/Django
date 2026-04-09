import re
with open("/home/mohammed/Admission_Pro/admission_system/templates/admission_system/college_ymbc.html", "r") as f:
    content = f.read()

if "checkValidity()" not in content:
    print("Missing validity check in ymbc, patching...")
    validation_js = """function nextAppStep(step) {
        // If moving forward, validate current step
        const currentStepEl = document.querySelector('.step-content:not(.hidden)');
        if (currentStepEl) {
            const currentStepMatch = currentStepEl.id.match(/\d+/);
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
    new_content = content.replace("function nextAppStep(step) {", validation_js)
    if new_content != content:
        with open("/home/mohammed/Admission_Pro/admission_system/templates/admission_system/college_ymbc.html", "w") as f:
            f.write(new_content)
        print("Patched.")
    else:
        print("Could not find function declaration.")
else:
    print("Already valid")
