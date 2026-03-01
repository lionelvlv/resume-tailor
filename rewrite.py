# rewrite.py
def rewrite_with_llm(bullet_text, job):
    # Replace this with your actual LLM call
    jd_keywords = ", ".join(job["skills_required"])
    return f"{bullet_text} (emphasizing: {jd_keywords})"

def rewrite_bullets(bullets, job):
    rewritten = []
    for b in bullets:
        new_text = rewrite_with_llm(b["text"], job)
        rewritten.append(new_text)
    return rewritten

if __name__ == "__main__":
    import json
    job = json.load(open("job.json"))
    bullets = json.load(open("selected_bullets.json"))
    print(rewrite_bullets(bullets, job))
