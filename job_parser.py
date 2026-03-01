# job_parser.py
import spacy
import json
from pathlib import Path

nlp = spacy.load("en_core_web_sm")

def load_skill_list():
    with open("data/skills_list.json") as f:
        return set(json.load(f))

def extract_job_info(text):
    doc = nlp(text)
    skills_list = load_skill_list()

    skills_found = set()
    responsibilities = []

    for token in doc:
        if token.text.lower() in skills_list:
            skills_found.add(token.text)

    for sent in doc.sents:
        if sent.text.strip().startswith(("Build", "Develop", "Design", "Implement", "Maintain", "Collaborate")):
            responsibilities.append(sent.text.strip())

    return {
        "skills_required": sorted(list(skills_found)),
        "responsibilities": responsibilities,
        "raw_text": text
    }

if __name__ == "__main__":
    jd = Path("job.txt").read_text()
    parsed = extract_job_info(jd)
    print(json.dumps(parsed, indent=2))
