import subprocess


def run(cmd):
    subprocess.run(cmd, shell=True, check=True)


# Initialize git repo
run("git init")

# Add all files
run("git add .")

# First commit
run('git commit -m "Initial commit from template"')

# pdm
run("pdm install")
