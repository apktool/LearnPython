
import os

PATH = os.path.dirname(os.path.abspath(__file__))

from jinja2 import FileSystemLoader
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
        # Environmentloader=PackageLoader('jinja2Demo', 'templates'),
        # autoescape=select_autoescape(['html', 'xml'])
        loader=FileSystemLoader(PATH + '/templates'),
        )
template = env.get_template('mytemplate.html')
html = template.render(a_variable='haha')
