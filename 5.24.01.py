# markdown

from markdown import Markdown

def render(md_file):
    with open(md_file, 'r') as f:
        text = f.read()
        md = Markdown(
                extensions=[
                    "fenced_code",
                    "codehilite(css_class=highlight,linenums=None)",
                    "meta",
                    "admonition",
                    "tables",
                    "toc",
                    "wikilinks",
                ],
            )
        html = md.convert(text)
        # meta = md.Meta if hasattr(md, "Meta") else {}
        toc = md.toc if hasattr(md, "toc") else ""
    return html


if __name__ == '__main__':
    md = 'About.md'
    html = render(md)
    with open('About.html', 'w') as f:
        f.write(html)

'''
title: 关于
summary: 介绍
authors: apktool
publish_date: 2016-05-24
tags: 简介
      Markdown

# 关于本文

我是文章

# Markdown基本语法

Markdown基本语法参见：
[https://daringfireball.net/projects/markdown/syntax](https://daringfireball.net/projects/markdown/syntax)

# 扩展的Markdown特殊语法

本Markdown的生成基于Python的Markdown包，因此支持的扩展语法也源于Python
Markdown，参>见：[Python Markdown](https://pythonhosted.org/Markdown/)

## 支持表格，引用，重点标识等
'''

'''
生成的html文档无head和title和body标签，因此需要手动加进去或者采用已有模板

<html lang="en" xmlns="http://www.w3.org/1999/html">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width,
        initial-scale=1">
        <title>helel</title>
    </head>
<body>
html context
</body>
</html>
'''
