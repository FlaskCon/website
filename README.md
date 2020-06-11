# statictipy
Static site generator for FlaskCon and hopefully a number of other uses

Launch live watch
```
python statictipy.py
```

Launch generate without live watch (regenerate on each change manually)
```
python statictipy.py --no-server
```

Changes in browser

```
# go to docs/
python server.py
```
Normally connects on localhost:8000

With livereload you only change files and it regenerates automatically. Bit like NodeJs

All Jinja2 files in templates. Settings in settings.py


