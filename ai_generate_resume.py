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

prompt = f""" You are a LaTeX résumé rewriting assistant focused on maximizing interview conversion. Your objectives: 
- Rewrite the entire résumé using the original LaTeX file as the structural template. 
- Update ALL relevant sections (Skills, WORK AND LEADERSHIP EXPERIENCE, Experience, Projects, Coursework, etc.) to best match the job description and the rewritten bullet metadata. 
- Use the rewritten bullet metadata to guide emphasis: highlight impact, quantification, technical depth, and alignment with required skills. 
Content rules: - Keep at most THREE experience items and THREE project items. 
- Each item may contain at most THREE bullet points. 
- Prioritize bullets that demonstrate quantifiable impact, leadership, ownership, technical depth, or direct relevance to the job. 
- Remove or shorten bullets that are low‑impact, redundant, non‑quantitative, or irrelevant to the job. 
- You may rewrite bullets for clarity, conciseness, and impact, but do NOT invent experiences or technologies not present in the original résumé or rewritten bullet metadata. 
- You may reorder sections and items to maximize relevance and interview likelihood. Formatting rules: 
- Preserve ALL LaTeX formatting exactly: documentclass, packages, macros, custom commands, spacing, layout, and sectioning. 
- Do NOT modify the preamble. 
- Do NOT introduce new LaTeX commands. 
- Do NOT output markdown or explanations. 
- Output ONLY valid LaTeX. Rewrite strategy: 
- For each experience/project, rewrite bullets to emphasize: • measurable outcomes • technical sophistication • leadership or ownership • alignment with job-required skills (Python, SQL, AWS, Docker, JavaScript, etc.) 
- Use the rewritten bullet metadata to guide emphasis and phrasing. 
- Remove coursework and skills unless it meaningfully improves relevance. 
- Ensure the final résumé compiles cleanly to ONE PAGE. This is mandatory. 
- Do not include anything to indicate age such as education graduation date. Any phrases like "Expected by..." are bad

Inputs:
Original resume (.tex):
{original_resume}
Job description (parsed):
{json.dumps(job, indent=2)}

Selected bullets:
{json.dumps(selected, indent=2)}

Rewritten bullets (with metadata for emphasis):
{json.dumps(rewritten, indent=2)}
"""

response = client.chat.completions.create(
model="groq/compound",
messages=[{"role": "user", "content": prompt}],
temperature=0
)

output_tex = response.choices[0].message.content

with open("tailored_resume.tex", "w", encoding="utf-8") as f:
  f.write(output_tex)

print("Generated tailored_resume.tex")
