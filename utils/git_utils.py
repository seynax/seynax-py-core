import subprocess


def get_git_username():
    res = subprocess.run(["git", "config", "user.name"], stdout=subprocess.PIPE)
    return res.stdout.strip().decode()
