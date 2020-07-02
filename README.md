# FlaskCon Website

Static site generator for the FlaskCon website.

## File Structure

```
- docs/  # Output folder
  - assets/  # Images used in the page
  - index.html  # The final page generated with templates, be sure not to edit this file manually
- templates/  # You know, the Jinja templates folder
  - layout/  # HTML structure
  - sections/  # Page content
- settings.py  # Page information
- staticpy.py  # Tool used to generate the website
```

## Generate the Site

Generate the website and launch live watch:
```
$ python statictipy.py
```

With livereload you only change files and it regenerates automatically. A bit like NodeJs.

Otherwise, you can generate the website without live watch (then you will need to re-run the following command on each change manually):
```
$ python statictipy.py --no-server
```
## Check the Generated Site

You may need to create a new terminal session, then launch a server for the output website:

```
$ cd docs
$ python server.py
```

Now the website will be running on http://localhost:8000, it's the same with open the docs/index.html manually.
