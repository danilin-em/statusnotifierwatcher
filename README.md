# StatusNotifierWatcher

Get apps from tray

## Usage:

```bash

# 0: Init VENV
python3 -m virtualenv venv && source venv/bin/activate

# 0.1: Install requirements
pip install -r requirements.txt

# 1: Start Watcher
python3 statusnotifierwatcher.py

# 1.1 Start Proxy
xembedsniproxy

# Now see apps in tray
python3 myapps.py

```

## FAQ:

**Q:**

```

Traceback (most recent call last):
  File "statusnotifierwatcher.py", line 45, in <module>
    from gi.repository import GLib
ModuleNotFoundError: No module named 'gi'

```

**A:**

See about *gi* module: https://askubuntu.com/questions/80448/what-would-cause-the-gi-module-to-be-missing-from-python

---
