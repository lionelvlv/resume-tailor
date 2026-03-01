# generate.py
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import json

def generate_resume(bullets, template="templates/resume.tex.j2", output="tailored_resume.tex"):
    env = Environment(loader=FileSystemLoader("templates"))
    tmpl = env.get_template("resume.tex.j2")

    rendered = tmpl.render(bullets=bullets)
    Path(output).write_text(rendered)
    return output

if __name__ == "__main__":
    bullets = json.load(open("rewritten_bullets.json"))
    generate_resume(bullets)
