import os

cases_dir = "/home/data/kuliah/project/love-agentic-skills/modules/cases"
target_cases = [
    "06_conflict.md",
    "08_apologizing.md",
    "15_abuse_coercive_control.md",
    "16_sexual_intimacy_consent.md",
    "17_mood_swings_stress.md",
    "18_attachment_styles.md",
    "19_digital_communication_warfare.md",
    "20_external_stressors.md",
    "21_trauma_triggers.md"
]

replacements = {
    # Headers
    "Advanced Clinical Protocol:": "Advanced Relational Protocol:",
    "Diagnostic Logic & Interpretation:": "Pattern Indicators & Context:",
    "Actionable Directives (Agent Instructions):": "Suggested Approaches (Agent Reference):",
    
    # Softening extreme directives inside the text (without altering facts)
    "must immediately": "are strongly advised to",
    "must physically return": "should ideally return",
    "fatal error": "high-risk misstep",
    "fatal mistake": "high-risk misstep",
    "absolute prohibition": "strong boundary",
    "deliver this absolute affirmation": "deliver this grounding affirmation",
    "leave without setting time expectations": "consider leaving without setting strict time expectations (ensure physical safety first)",
    "You MUST keep this boundary absolutely": "You are strongly encouraged to maintain this boundary",
    "strictly forbidden": "strongly discouraged",
    "contractually obligated": "highly encouraged",
    "absolute rule": "strong guideline",
    "absolute validation": "strong validation",
    "absolute reassurance": "clear reassurance",
    "absolute boundary": "clear boundary"
}

def soften_file(filename):
    filepath = os.path.join(cases_dir, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}, not found.")
        return
        
    with open(filepath, 'r') as f:
        content = f.read()
        
    original_content = content
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    if content != original_content:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Softened {filename}")
    else:
        print(f"No changes needed for {filename}")

for case in target_cases:
    soften_file(case)
