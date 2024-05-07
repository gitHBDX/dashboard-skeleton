# {project_name}
Dashboard {app_name}

## Installation

### Local environment 

```bash
pip install git+ssh://git@github.com/gitHBDX/{project_name}.git
```

### With mamba

```bash
mamba create -n {project_name} -y "python=3.9"
mamba activate {project_name}
pip install git+ssh://git@github.com/gitHBDX/{project_name}.git
{package_name}-init
```

One-liner:

```bash
mamba create -n {project_name} -y "python=3.9" && mamba activate {project_name} && pip install git+ssh://git@github.com/gitHBDX/{project_name}.git && {package_name}-init
```

## Run

Run in dev mode

```bash
{package_name} --debug
````

Run in production mode

```bash
gunicorn {package_name}.__main__
```

Run as a service

```bash
systemctl --user enable --now {package_name}
```

-----

<p>Developed @</p>
<img src="https://www.hummingbird-diagnostics.com/application/files/4214/6893/9202/logo.png" alt="Hummingbid Diagnostics logo" width="200"/>