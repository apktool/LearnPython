# Jinja2 demo

from jinja2 import Template
template = Template('Hello {{name}}')
name = template.render(name='Apktool')
print(name)
