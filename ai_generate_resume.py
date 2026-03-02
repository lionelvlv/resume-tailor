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
You rewrite LaTeX résumés and must output ONLY valid LaTeX that fully compiles.

Strict rules:
- Preserve the original LaTeX structure exactly: documentclass, packages, macros, custom commands, spacing, layout, and sectioning.
- Do NOT modify the preamble.
- Do NOT remove or alter \\begin{{document}} or \\end{{document}}.
- Do NOT output markdown, comments, explanations, or code fences.
- Output a complete, valid .tex file.

Rewrite rules:
- Rewrite the résumé to maximize interview conversion.
- Use the rewritten bullet metadata to guide emphasis on impact, quantification, technical depth, and alignment with required skills.
- Keep at most 3 experience items and 3 project items, each with at most 3 bullet points.
- Prioritize recent experience (within ~2 years) when relevant.
- Remove or shorten low‑impact, redundant, or irrelevant bullets.
- Remove coursework unless highly relevant.
- Remove graduation dates or age‑revealing info.
- You may tighten spacing or shorten text to ensure the résumé fits on ONE PAGE without harming readability.
- Do NOT invent new jobs, skills, or technologies.

Inputs:

Original LaTeX résumé:
{original_resume}

Job description (condensed):
{json.dumps({
    "title": job.get("title", ""),
    "skills_required": job.get("skills_required", []),
    "responsibilities": job.get("responsibilities", [])[:6]
}, indent=2)}

Rewritten bullets (with emphasis metadata):
{json.dumps(rewritten, indent=2)}

Selected bullets (for reference):
{json.dumps(selected, indent=2)}

Now output the FULL rewritten LaTeX résumé, preserving the preamble and structure.
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
