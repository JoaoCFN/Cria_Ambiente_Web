import os
# inicia o npm no projeto
def npm(): os.system("npm init -y")
# cria meu index.html
def html(): os.system("copy NUL index.html")
# cria a pasta js e o script.js e volta ao diretório raiz
def js():
    os.mkdir("js")
    os.chdir("js")
    os.system("copy NUL script.js")
    os.chdir("../")
# cria a pasta sass e o style.scss e volta ao diretório raiz
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
