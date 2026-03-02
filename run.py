import subprocess

subprocess.run("python job_parser.py > job.json", shell=True)
subprocess.run("python resume_parser.py > bullets.json", shell=True)
subprocess.run("python match.py > selected_bullets.json", shell=True)
subprocess.run("python rewrite.py > rewritten_bullets.json", shell=True)
subprocess.run("python ai_generate_resume.py", shell=True)

#Compile PDF 
subprocess.run("tectonic tailored_resume.tex", shell=True) 
print("Pipeline complete. PDF generated: tailored_resume.pdf")
