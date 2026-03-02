# ai_generate_resume.py
from groq import Groq
from dotenv import load_dotenv

import os, json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

original_resume = load_text("resume.tex")
job = json.load(open("job.json", "r", encoding="utf-8"))
selected = json.load(open("selected_bullets.json", "r", encoding="utf-8"))
rewritten = json.load(open("rewritten_bullets.json", "r", encoding="utf-8"))

prompt = f"""
You are a LaTeX résumé rewriting assistant.

Goal:
- Take the original LaTeX résumé.
- Update ALL relevant sections (summary, skills, WORK AND LEADERSHIP EXPERIENCE, experience, projects, coursework, etc.)
  to best match the job description and the rewritten bullets.
- Filter and trim content so that the final compiled résumé is approximately ONE PAGE.
- This means at most 3 items for work experience and projects
- Each item should have at most 3 bullet points. Trim bullet points that aren't quantitative or demonstrate impact.
- Prefer keeping the strongest, most relevant experiences and projects.
- You may shorten or remove less relevant bullets/sections to stay within one page.
- Preserve ALL LaTeX formatting: documentclass, packages, macros, custom commands, spacing, and layout.
- Do NOT change the preamble or structure beyond swapping/rewriting content.
- Output ONLY valid LaTeX, no explanations, no markdown.

Original resume (.tex):
{original_resume}
Job description (parsed):
{json.dumps(job, indent=2)}

Selected bullets:
{json.dumps(selected, indent=2)}

Rewritten bullets:
{json.dumps(rewritten, indent=2)}
"""

response = client.chat.completions.create(
model="llama-3.3-70b-versatile",
messages=[{"role": "user", "content": prompt}],
temperature=0
)

output_tex = response.choices[0].message.content

with open("tailored_resume.tex", "w", encoding="utf-8") as f:
  f.write(output_tex)

print("Generated tailored_resume.tex")
