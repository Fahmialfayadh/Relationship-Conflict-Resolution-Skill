import os
import shutil

source_cases_dir = "/home/data/kuliah/project/love-agentic-skills/modules/cases"
source_modules_dir = "/home/data/kuliah/project/love-agentic-skills/modules"
output_dir = "/home/data/kuliah/project/love-agentic-skills/custom_gpt_bundle"

os.makedirs(output_dir, exist_ok=True)

# Copy system files
system_files = ["analytical_protocol.md", "decision_flow.md", "guardrails.md", "toolbox_and_style.md"]
for sf in system_files:
    shutil.copy(os.path.join(source_modules_dir, sf), os.path.join(output_dir, sf))

def combine_files(file_list, output_name):
    combined_content = []
    for f in file_list:
        with open(os.path.join(source_cases_dir, f), 'r') as infile:
            combined_content.append(infile.read())
            combined_content.append("\n\n---\n\n")
    
    with open(os.path.join(output_dir, output_name), 'w') as outfile:
        outfile.write("".join(combined_content))

# Group 1: Modern Dating
combine_files(["01_busy_partner.md", "02_ghosting.md", "03_breadcrumbing.md", "04_situationships.md"], "case_bundle_modern_dating.md")

# Group 2: Conflict & Repair
combine_files(["06_conflict.md", "08_apologizing.md", "11_self_aware_user.md"], "case_bundle_conflict_and_repair.md")

# Group 3: Abuse & Trauma
combine_files(["15_abuse_coercive_control.md", "21_trauma_triggers.md"], "case_bundle_abuse_and_trauma.md")

# Group 4: LDR
combine_files(["12_ldr_digital_cold_war.md", "13_ldr_touch_starvation.md", "14_ldr_initiative_asymmetry.md"], "case_bundle_ldr.md")

# Copy the remaining individual cases
remaining_cases = [
    "05_jealousy.md",
    "07_feeling_worthless.md",
    "09_breakups.md",
    "10_setting_healthy_boundaries.md",
    "16_sexual_intimacy_consent.md",
    "17_mood_swings_stress.md",
    "18_attachment_styles.md",
    "19_digital_communication_warfare.md",
    "20_external_stressors.md"
]

for rc in remaining_cases:
    shutil.copy(os.path.join(source_cases_dir, rc), os.path.join(output_dir, rc))

# Generate a new router specifically for the Custom GPT
router_content = """# Agent Router Matrix (Custom GPT)

Use this table to map the user's situation to the correct knowledge base file.

### System & Guardrails
| Function | File to Read | Priority |
|---|---|---|
| **Tone & Style** | `toolbox_and_style.md` | Mandatory baseline |
| **Logic Workflow** | `decision_flow.md` | Core framework |
| **Analytical Users** | `analytical_protocol.md` | Use if user is purely logical |
| **Danger/Abuse** | `guardrails.md` | Highest (Safety overrules all) |

### Cases & Clinical Protocols
| Trigger / Situation | Primary File | Secondary / Support File |
|---|---|---|
| Ignored, ghosted, breadcrumbing, busy partner | `case_bundle_modern_dating.md` | `10_setting_healthy_boundaries.md` |
| Arguing, apologies, user admitting fault | `case_bundle_conflict_and_repair.md` | `17_mood_swings_stress.md` |
| Coercive control, DARVO, past trauma, flashbacks | `case_bundle_abuse_and_trauma.md` | `guardrails.md` (Check safety) |
| Long-Distance (LDR) issues (timezones, cold war) | `case_bundle_ldr.md` | `19_digital_communication_warfare.md` |
| Jealousy, suspicion, insecurity | `05_jealousy.md` | `18_attachment_styles.md` |
| Digital fights, texting wars, read receipt anxiety | `19_digital_communication_warfare.md` | `case_bundle_modern_dating.md` |
| Libido mismatch, sexual pressure, nudes | `16_sexual_intimacy_consent.md` | `10_setting_healthy_boundaries.md` |
| Partner acting clingy, demanding, or cold/distant | `18_attachment_styles.md` | `05_jealousy.md` |
| Stress from work, traffic, hormonal cycles | `17_mood_swings_stress.md` | `case_bundle_conflict_and_repair.md` |
| Interference from parents/in-laws, financial stress | `20_external_stressors.md` | `10_setting_healthy_boundaries.md` |
| User feeling worthless, discarded, insecure | `07_feeling_worthless.md` | `18_attachment_styles.md` |
| Wanting to end it, breakups, post-breakup | `09_breakups.md` | `07_feeling_worthless.md` |
| User needs help setting a hard boundary | `10_setting_healthy_boundaries.md` | None |
"""

with open(os.path.join(output_dir, "agent_router_gpt.md"), 'w') as f:
    f.write(router_content)

print(f"Bundled files created successfully in {output_dir}")
