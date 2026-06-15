import json
import os

log_path = '/home/fahmialfayadh/.gemini/antigravity-ide/brain/44e24312-bc4e-4046-965e-37f1c93504ef/.system_generated/logs/transcript.jsonl'
out_path = '/home/data/kuliah/project/love-agentic-skills/scratch_research.md'

last_user_msg = ""

with open(log_path, 'r') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('type') == 'USER_INPUT':
                last_user_msg = data.get('content', '')
        except:
            pass

with open(out_path, 'w') as f:
    f.write(last_user_msg)

print(f"Extracted to {out_path}")
