cfg = None

def load_cfg():
    import yaml
    from pathlib import Path
    global cfg
    cfg = Path(__file__).parent / "assets" / "config.yaml"

    if not cfg.exists():
        raise FileNotFoundError("Config file not found")
    
    cfg = yaml.safe_load(cfg.read_text())

load_cfg()