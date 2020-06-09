# https://github.com/pymug/website-AV19-AV20

from flask import Flask
import os
import sys
from os.path import join
import settings

from jinja2 import FileSystemLoader
from jinja2 import Environment

import uuid
import datetime
from livereload import Server, shell

def generate(file_in_templates, outpath, template_dir='templates', assets_path_append='', **kwargs):
    '''the raw generate function to generate files'''

    file_loader = FileSystemLoader(template_dir)
    env = Environment(loader=file_loader)
    template = env.get_template(file_in_templates)

    build_id = str(uuid.uuid4()) # to be used

    output = template.render(kwargs, year=datetime.datetime.now().year,
        build_id=build_id, assets_path_append=assets_path_append)
    print(output, file=open(outpath, 'w+', encoding="utf8"))



context = {
    'SITE_NAME': settings.SITE_NAME,
    'CFP_LINK': settings.CFP_LINK,
    'REVIEWERS': settings.REVIEWERS,
    'ORGANISERS': settings.ORGANISERS,
    'MEDIA': settings.MEDIA
}

def main(args):
    def gen():
        generate('index.html', join(settings.OUTPUT_FOLDER, 'index.html'), **context)

    if len(args) > 1 and args[1] == '--no-server':
        gen()
    else:
        app = Flask(__name__)

        # remember to use DEBUG mode for templates auto reload
        # https://github.com/lepture/python-livereload/issues/144
        app.debug = True

        server = Server(app.wsgi_app)

        # run a shell command
        #server.watch('.', 'make static')

        # run a function
        
        server.watch('.', gen, delay=3)

        # output stdout into a file
        #server.watch('style.less', shell('lessc style.less', output='style.css'))

        server.serve()
    

if __name__ == '__main__':
    main(sys.argv)
