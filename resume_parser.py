# resume_parser.py
import re
import json
from pathlib import Path

def extract_bullets(tex_path="resume.tex"):
    text = Path(tex_path).read_text()
    bullets = re.findall(r"\\item\s+(.*)", text)

    bullet_objs = []
    for i, b in enumerate(bullets):
        bullet_objs.append({
            "id": f"bullet_{i}",
            "text": b.strip()
        })

    return bullet_objs

if __name__ == "__main__":
    bullets = extract_bullets()
    print(json.dumps(bullets, indent=2))

