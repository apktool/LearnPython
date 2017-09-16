
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
        loader=PackageLoader('jinja2Demo', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
        )

template1 = env.get_template('mytemplate.html')
users1=[{'name':'John'},{'name':'Tom', 'hidden':True},{'name':'Lisa'},{'name':'Bob'}]
users2=['li', 'zhang', 'zhong', 'zhou']
html1 = template1.render(a_variable='a_variable', name='apktool', users=users1,
        users2 = users2)

template2 = env.get_template('child.html')
html2 = template2.render()

print(html1)
