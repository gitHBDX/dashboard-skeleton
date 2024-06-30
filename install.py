#!/bin/python

import datetime
import os
from pathlib import Path
import subprocess


clear_screen = lambda: print("\033c")
print_red = lambda x: print("\033[31m{}\033[0m".format(x))
print_green = lambda x: print("\033[32m{}\033[0m".format(x))
print_yellow = lambda x: print("\033[33m{}\033[0m".format(x))
print_blue = lambda x: print("\033[34m{}\033[0m".format(x))


def question(x: str, c: str = "blue") -> bool:
    ccode = 33 if c == "yellow" else 34
    while (resp := input(f"\033[{ccode}m{x} (y/n)\033[0m > ").strip().lower()) not in ["y", "n"]:
        print_red("Please enter y or n")
    print(resp)
    return resp == "y"


def user_input(x: str) -> str:
    while True:
        print_blue(x)
        inp = input("> ").strip()
        if question(f"Is {inp} correct?", "yellow"):
            return inp


clear_screen()
os.chdir(Path(__file__).parent)
print_yellow("dash-skeleton")
print_green("setting up a new dashboard…\n\n\n")

cfg = {
    "app_name": user_input("Enter the name of the app (without \"dashboard-\" dashboard-<name> will be used as the package name)"),
    "user_name": user_input("Enter your name"),
    "user_email": user_input("Enter your email address"),
    "description": user_input("Enter a short description of the app (Shown in the header)"),
    "current_year": datetime.datetime.now().year,
    "current_month": datetime.datetime.now().month,
    "dependencies": "",
    "extras": "",
}

cfg["project_name"] = f"dashboard-{cfg['app_name'].lower()}"
cfg["package_name"] = cfg["project_name"].replace("-", "_")

if question("Include cache?"):
    cfg["dependencies"] += '"anndata-cache@git+https://github.com/gitHBDX/anndata-cache",\n'


for filename in map(Path, ["pyproject.toml", "_README.md", "Dockerfile", "src/dashboard-skeleton/__main__.py", "src/dashboard-skeleton/pages/index.py", "src/dashboard-skeleton/assets/config.yaml", "src/dashboard-skeleton/pages/idnex.py"]):
    filename.write_text(filename.read_text().format(**cfg))

Path("src/dashboard-skeleton").rename(f"src/{cfg['package_name']}")
Path("_README.md").rename("README.md")

if question("Setup a new conda environment? (recommended)"):
    if "CONDA_EXE" not in os.environ:
        print_red("Conda is not installed. Can't create a new environment.")
    else:
        conda_exe = os.environ["CONDA_EXE"]
        print(f"{conda_exe} create -n {cfg['project_name']} python=3.9")
        subprocess.run(f"{conda_exe} create -n {cfg['project_name']} python=3.9", shell=True)
        pip = Path(os.environ["CONDA_PREFIX"]).parent / cfg["project_name"] / "bin" / "pip"
        print(f"{pip} install -r requirements.txt")
        subprocess.run(f"{pip} install --force-reinstall -e .", shell=True)

#delete the install.py file and commit all changes
os.remove("install.py")
subprocess.run("git add .", shell=True)
subprocess.run('git commit -m "Initial commit"', shell=True)

print_green("Done!")


