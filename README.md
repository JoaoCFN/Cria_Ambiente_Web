# Cria_Ambiente_Web
 Script em python que cria um ambiente de desenvolvimento web básico. 
 A estrutura criada contém as tecnologias HTML, CSS, SASS, JS E NPM.
 
 ## Execução
 Para usar o script, basta colocar ele dentro da pasta que você deseja criar o seu projeto. Existem duas maneiras de executá-lo:
 
   1. Clicar duas vezes no arquivo 
   2. Rodar ele por comandos no terminal usando o comando `python Ambiente.py`
   
 **OBS: É importante ressaltar que para rodar ele pelo terminal, se estiver no windows, precisará adicionar o python as suas   variáveis de ambiente. Caso você não conheça o PATH, esse tutorial pode te ajudar -> [Tutorial](https://pt.stackoverflow.com/questions/5024/como-mudar-o-path-nos-windows). :smile:**
 
## Funcionamento
O script irá criar a pasta do seu projeto contendo os arquivo `script.js`, `style.scss` e um `index.html`. Além disso, ele também irá iniciar o npm na sua aplicação. Após a criação do projeto, o programa irá executar o Node Sass para assistir as alterações no arquivo SASS e gerar um `estilo.css`. 

Caso você use outra maneira de compilação de SASS, altere o comando de inicialização dentro do script. Você deve procurar por este comando `os.system("node-sass --output-style compressed --watch sass/style.scss estilo.css")` e alterar o conteúdo do os.system. 

Se não tem o Node Sass instalado na sua máquina e deseja usá-lo, basta abrir o seu terminal e executar `npm install -g node-sass`.

## Alterações
Caso você queira alterar algo para adaptar a sua necessidade fique a vontade. Esse programa é bem básico e está desenhado inicialmente para atender a minha demanda. 
Aqui vai uma lista básica de comandos utilizados no programa:
`os.mkdir("sass")` : Cria uma pasta com o nome passado como parâmetro. Neste exemplo, cria a pasta sass.
`os.chdir("sass")` : Acessa a pasta com o nome passado como parâmetro. Neste exemplo, acessa a pasta sass.
`os.system("code .")` : Digita comandos no terminal. Neste exemplo, abre o VS Code.

O programa foi feito usando a biblioteca OS do Python. 
