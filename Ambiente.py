import os
def npm(): os.system("npm init -y")
def html(): os.system("copy NUL index.html")
def js():
    os.mkdir("js")
    os.chdir("js")
    os.system("copy NUL script.js")
    os.chdir("../")
def sass():
    os.mkdir("sass")
    os.chdir("sass")
    os.system("copy NUL style.scss")
    os.chdir("../")
    os.system("code .")
    os.system("node-sass --output-style compressed --watch sass/style.scss estilo.css")
def main():
    npm()
    html()
    js()
    sass()
main()
