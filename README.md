Automated pipeline that rewrites your LaTeX résumé using Groq, aligns it to a job description, and outputs a one‑page PDF.

---

## Installation

### 1. Clone the project
```bash
git clone https://github.com/yourusername/resume-tailor
cd resume-tailor
```

### 2. Create and activate Conda environment
```bash
conda create -n resume-tailor python=3.11 -y
conda activate resume-tailor
```

### 3. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 4. Install LaTeX compiler (Tectonic)
```bash
conda install -c conda-forge tectonic
```

### 5. Add your Groq API key  
Create a `.env` file:
```
GROQ_API_KEY=your_key_here
```

---

## Required Files

Place these in the project root:

- `resume.tex` — your original LaTeX résumé  
- `job.txt` — the job description  
- `resume.cls` — required for LaTeX compilation
---

## Usage

Run the full pipeline:

```bash
python run.py
```

This generates:

- `job.json`  
- `bullets.json`  
- `selected_bullets.json`  
- `rewritten_bullets.json`  
- `tailored_resume.tex`  
- `tailored_resume.pdf`  

Open `tailored_resume.pdf` to view your final one‑page résumé.

---

## Model

The rewrite step uses Groq.  
Default model (free):

```
model="groq/compound"
```

You may switch to a paid Groq model (higher quality) by editing `ai_generate_resume.py`.

---

## requirements.txt

```
groq==1.0.0
python-dotenv==1.2.2
```
