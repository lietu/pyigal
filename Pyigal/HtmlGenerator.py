# -*- coding: utf-8 -*-

import os
import codecs
from jinja2 import Environment
from jinja2 import FileSystemLoader


class HtmlGenerator(object):
    html = None

    def generate(self, source, template_params):

        # Get the template
        env = Environment(loader=FileSystemLoader(os.path.dirname(source)))
        template = env.get_template(os.path.basename(source))

        # Render the template into HTML
        self.html = template.render(**template_params)

    def save(self, destination):

        # Write the result HTML
        file = codecs.open(destination, 'w', 'utf-8')
        file.write(self.html)
        file.close()
