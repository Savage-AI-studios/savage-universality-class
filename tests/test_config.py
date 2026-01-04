import json
from pathlib import Path


def test_config_exists_and_has_execution_windows():
    p = Path("config.json")
    assert p.exists(), "config.json must exist in project root"
    data = json.loads(p.read_text())
    assert "execution_windows" in data
    assert isinstance(data["execution_windows"], dict)
