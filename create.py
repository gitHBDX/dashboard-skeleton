import datetime
import os

clear_screen = lambda: print("\033c")
print_red = lambda x: print("\033[31m{}\033[0m".format(x))
print_green = lambda x: print("\033[32m{}\033[0m".format(x))
print_yellow = lambda x: print("\033[33m{}\033[0m".format(x))
print_blue = lambda x: print("\033[34m{}\033[0m".format(x))

def question(x: str) -> bool:
    print_blue(x)
    while resp := input() not in ["y", "n"]:
        print_red("Please enter y or n")
    return resp == "y"

def user_input(x: str) -> str:
    print_blue(x)
    while True:
        inp = input()
        if question(f"Is {inp} correct?"):
            return inp

pyproject_toml_template = """
[project]
name = "dashboard-{app_name}"
version = "{current_year}.{current_month}.0"
description = "The DASH dashboard for {app_name}"
readme = "README.md"
requires-python = ">=3.9"
authors = [{{ name = "{user_name}", email = "{user_email}" }}]


dependencies = [
    "anndata=0.8.0",
    "pyarrow=11.0.0",
    "yaml",
]

[project.urls]
"Homepage" = "https://github.com/gitHBDX/anndata-cache"

[build-system]
requires = ["setuptools>=43.0.0", "wheel"]
build-backend = "setuptools.build_meta"
"""

clear_screen()
print_yellow("dash-skeleton")
print_green("Creating a new dash app skeleton")

if os.listdir(".") != []:
    print_red("Current directory is not empty")
    exit(1)

cfg = {
"app_name": user_input("Enter the name of the app (dashboard-<name> will be used as the package name)"),
"user_name": user_input("Enter your name"),
"user_email": user_input("Enter your email address"),
"current_year": datetime.datetime.now().year,
"current_month": datetime.datetime.now().month,
}

pyproject_toml = pyproject_toml_template.format(**cfg)

if question("Include logging?"):
    pass

if question("Include cache?"):
    pass

if question("Set-UP git?"):
    pass

print(pyproject_toml)