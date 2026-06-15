import os

modules_dir = "/home/data/kuliah/project/love-agentic-skills/modules"
cases_dir = "/home/data/kuliah/project/love-agentic-skills/modules/cases"
output_file = "/home/data/kuliah/project/love-agentic-skills/monolithic.md"

header = """# Relationship Conflict Resolution - Monolithic Prompt
Use this as the system prompt for your AI Agent.

---

## 1. Persona and Goal
You are an advanced Relationship Conflict Resolution Agent. Your goal is to act as the user's external emotional brain. You process psychological nuances, de-escalate conflicts, and provide actionable advice based on clinical psychology and attachment theory.

"""

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

system_files = [
    "toolbox_and_style.md",
    "decision_flow.md",
    "analytical_protocol.md",
    "guardrails.md"
]

with open(output_file, 'w') as out:
    out.write(header)
    
    out.write("## 2. System Guidelines & Guardrails\n\n")
    for sf in system_files:
        content = read_file(os.path.join(modules_dir, sf))
        out.write(content)
        out.write("\n\n---\n\n")
        
    out.write("## 3. Cases and Clinical Protocols\n\n")
    case_files = sorted([f for f in os.listdir(cases_dir) if f.endswith('.md')])
    for cf in case_files:
        content = read_file(os.path.join(cases_dir, cf))
        out.write(content)
        out.write("\n\n---\n\n")

print(f"monolithic.md successfully updated!")
