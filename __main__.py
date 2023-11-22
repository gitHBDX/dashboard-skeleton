import datetime
import os
from pathlib import Path


clear_screen = lambda: print("\033c")
print_red = lambda x: print("\033[31m{}\033[0m".format(x))
print_green = lambda x: print("\033[32m{}\033[0m".format(x))
print_yellow = lambda x: print("\033[33m{}\033[0m".format(x))
print_blue = lambda x: print("\033[34m{}\033[0m".format(x))

def question(x: str, c:str="blue") -> bool:
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
print_yellow("dash-skeleton")
print_green("Creating a new dash app skeleton in the current directory \n\n\n")

if os.listdir(".") != ["main.zip"]:
    print_red("Current directory is not empty")
    exit(1)

cfg = {
"app_name": user_input("Enter the name of the app (dashboard-<name> will be used as the package name)"),
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
    cfg["dependencies"] += "\"anndata-cache@git+https://github.com/gitHBDX/anndata-cache\",\n"

Path("pyproject.toml").write_text(Path("skeleton/pyproject.toml").read_text().format(**cfg))
Path("README.md").write_text(Path("skeleton/README.md").read_text().format(**cfg))
Path(f"src/{cfg['package_name']}").mkdir(parents=True)
Path(f"src/{cfg['package_name']}/__init__.py").touch()
Path(f"src/{cfg['package_name']}/__main__.py").write_text(Path("skeleton/src/__main__.py").format(**cfg))
Path(f"src/{cfg['package_name']}/assets").mkdir(parents=True)
Path(f"src/{cfg['package_name']}/assets/favicon.ico").write_bytes(Path("skeleton/src/assets/favicon.ico").read_bytes())
Path(f"src/{cfg['package_name']}/assets/Logo-Hummingbird.png").write_bytes(Path("skeleton/src/assets/Logo-Hummingbird.png").read_bytes())

os.system("git init")
os.system("git add .")
os.system('git commit -m "Initial commit"')
os.system("git branch -M main")
os.system(f"git remote add origin git@github.com:gitHBDX/{cfg['project_name']}.git")
print_yellow("Open")
print_blue("https://github.com/new")
print_yellow("and create a new repository named")
print_green(f"gitHBDX/{cfg['project_name']}")
print_yellow("Then run the following commands:")
print_green("git push -u origin main")