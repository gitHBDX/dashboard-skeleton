from pathlib import Path
import subprocess
import sys

def main():
    systemd_folder = Path("~/.config/systemd/user/").expanduser().absolute()
    systemd_folder.mkdir(parents=True, exist_ok=True)

    gunicorn_bin = Path(sys.executable).parent / "gunicorn"

    service_file = systemd_folder / f"{__package__}.service"
    service_file.write_text(
    f"""[Unit]
    Description=Running DASH app {__package__}
    Requires=plasma_cache.service
    Wants=jupyter_notebook.service
    After=plasma_cache.service

    [Service]
    ExecStart={gunicorn_bin} {__package__}.__main__ -b :{port}
    WorkingDirectory={Path(__file__).absolute().parents[0]}
    Restart=always

    [Install]
    WantedBy=default.target"""
    )
    print(f"Service file written to {service_file}")

    subprocess.run(["systemctl", "--user", "daemon-reload"])
    print("Daemon reloaded")


if __name__ == "__main__":
    main()