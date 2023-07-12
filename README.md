# All my scripts contained within a flask API to serve the data.

Use with an API enabled node, preferably locally

run by using:
```bash
cd UnificationScriptAPI

pip install -r requirements.txt
```
For running development/standalone:
```
python -m uniapi
```

Better yet, run with Gunicorn(installed with requirements.txt)
```
gunicorn -b 0.0.0.0:9169 uniapi.__main__:app
```
