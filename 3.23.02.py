from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('application', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('home.html')
print(template.render(name='aptkool'))

# 目录结构
'''
3.23.02.py
application
├── __init__.py
└── templates
    ├── base.html
    └── home.html
'''

# base.html
'''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">   
<html lang="en">   
<html xmlns="http://www.w3.org/1999/xhtml">   
<head>   
	{% block head %}   
	<link rel="stylesheet" href="style.css" />   
	<title>{% block title %}{% endblock %}'s Webpage</title>   
	{% endblock %}   
</head>   
<body>   
	<div id="content">{% block content %}{% endblock %}</div>   
	<div id="footer">   
		{% block footer %}   
		&copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.   
		{% endblock %}   
	</div>   
</body>   
'''

# home.html
'''
{% extends "base.html" %}   
{% block title %}{{ name }}{% endblock %}   
{% block head %}   
	{{ super() }}   
	<style type="text/css">   
		.important { color: #336699; }   
	</style>   
{% endblock %}   
{% block content %}   
	<h1>Index</h1>   
	<p class="important">   
	  Welcome on my awsome homepage.   
	</p>   
{% endblock %}   
'''
