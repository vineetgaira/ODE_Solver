import json
import os 

SETTINGS_FILE = "data/settings.json"

DEFAULT_SETTINGS = {
    "precision": 5,
    "colour": True,
    "save_automatically": True,
    "graph_style": "line"
}

_settings = DEFAULT_SETTINGS.copy()

def load_settings():
    global _settings
    if os.path.exists(SETTINGS_FILE) and os.path.getsize(SETTINGS_FILE) > 0:
        with open ("SETTINGS_FILE", "r") as file:
            saved = json.load(file)
        _settings = {**DEFAULT_SETTINGS, **saved}
    else:
        _settings = DEFAULT_SETTINGS.copy()

def save_settings():
    with open("SETTINGS_FILE", "w") as file:
        json.dump(_settings, file, sort_keys=True, indent=2)

def get_setting(key):
    return _settings[key]

def set_settings(key, value):
    _settings[key] = value
    save_settings()