import subprocess
import os

def run_git_cmd(cmd):
    try:
        print(f"Running: {cmd}")
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

os.chdir(r"c:\Users\hiche\pharm")

# Sequence of commands
run_git_cmd("git init")
run_git_cmd("git remote add origin https://github.com/nourcherguii/pharm.git")
run_git_cmd("git add .")
run_git_cmd('git commit -m "Initial commit: Microservices Architecture Optimized"')
run_git_cmd("git branch -M main")
run_git_cmd("git push -u origin main")
