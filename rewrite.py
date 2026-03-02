# rewrite.py
import json

def rewrite_with_llm(bullet_text, job):
    """
    Lightweight local rewrite step.
    This does NOT call an LLM — the real rewriting happens in ai_generate_resume.py.
    This step simply enriches each bullet with job-relevant emphasis signals.
    """
    skills = job.get("skills_required", [])
    keywords = ", ".join(skills)

    # Add a structured hint for the final AI step
    return {
        "original": bullet_text,
        "emphasis": skills,
        "rewritten_hint": f"Focus on impact, quantification, and relevance to: {keywords}"
    }

def rewrite_bullets(bullets, job):
    rewritten = []
    for b in bullets:
        rewritten.append({
            "id": b["id"],
            "text": b["text"],
            "rewrite": rewrite_with_llm(b["text"], job)
        })
    return rewritten

if __name__ == "__main__":
    job = json.load(open("job.json", "r", encoding="utf-8"))
    bullets = json.load(open("selected_bullets.json", "r", encoding="utf-8"))
    rewritten = rewrite_bullets(bullets, job)
    print(json.dumps(rewritten, indent=2))
