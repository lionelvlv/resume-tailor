# match.py
import json

def score_bullet(bullet, job):
    score = 0
    text = bullet["text"].lower()

    for skill in job["skills_required"]:
        if skill.lower() in text:
            score += 2

    for resp in job["responsibilities"]:
        if any(word.lower() in text for word in resp.split()):
            score += 1

    return score

def match_bullets(bullets, job, top_n=12):
    scored = []
    for b in bullets:
        s = score_bullet(b, job)
        scored.append((s, b))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [b for _, b in scored[:top_n]]

if __name__ == "__main__":
    job = json.load(open("job.json"))
    bullets = json.load(open("bullets.json"))
    selected = match_bullets(bullets, job)
    print(json.dumps(selected, indent=2))
