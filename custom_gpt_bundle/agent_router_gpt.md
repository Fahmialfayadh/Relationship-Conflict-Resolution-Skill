# Agent Router Matrix (Custom GPT)

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
