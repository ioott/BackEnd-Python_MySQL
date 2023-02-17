<h1 align="center">Aplicação para Análise de Transações com Cartão</h1>
<p align="center">
  <img src="https://img.shields.io/badge/language-Python-blue.svg">
  <img src="https://img.shields.io/badge/language-MySQL-blue.svg">
</p>
<p align="center">
  <a href="#sobre">Sobre</a> •
  <a href="#tecnologias">Tecnologias</a> •
  <a href="#instalação">Instalação</a> •
  <a href="#utilização">Utilização</a> •
  <a href="#melhorias-futuras">Melhorias Futuras</a> •
  <a href="#licença">Licença</a>
</p>

## Sobre
Este é um sistema de análise de transações com cartão, desenvolvido em Python. A aplicação faz a leitura de um arquivo CSV contendo dados de transações, processa e armazena-os em um banco de dados MySQL. Além disso, a aplicação também permite gerar relatórios com base nos dados armazenados e verificar se um usuário específico é suspeito ou não de realizar transações fraudulentas.

## Tecnologias
O sistema foi desenvolvido utilizando as seguintes tecnologias:

* Python
* MySQL

## Instalação
<details>
  <summary> Para utilizar o sistema, é necessário instalar o Python e o MySQL em sua máquina.</summary>

  ### Python
  Para instalar o Python:

  * Acesse o site oficial: https://www.python.org/downloads/
  * Escolha a versão mais recente do Python 3 e faça o download de acordo com seu sistema operacional.
  * Execute o instalador e siga as instruções para concluir a instalação.

  ### MySQL
  Para instalar o MySQL:

  * Acesse o site oficial: https://dev.mysql.com/downloads/
  * Escolha a versão mais recente do MySQL 8 e faça o download de acordo com seu sistema operacional.
  * Execute o instalador e siga as instruções para concluir a instalação.
</details>

## Utilização
<details>
  <summary> Para utilizar o sistema </summary> <br/>
  1 - Clone o repositório em sua máquina: <code> git@github.com:ioott/cw.git </code> <br/>
  2 - Acesse o diretório do sistema: <code> cd cw.git </code> <br/>
  3 - Crie um ambiente virtual e ative: <code> python3 -m venv .venv && source .venv/bin/activate </code> <br/>
  4 - Instale as dependências do sistema: <code> python3 -m pip install -r dev-requirements.txt </code> <br/>
  5 - Crie um arquivo <code> .env </code> na raiz e coloque as variáveis de configuração do banco de dados:

  ```
  DB_HOST=<host do banco de dados>
  DB_USER=<usuário do banco de dados>
  DB_PASSWORD=<senha do usuário do banco de dados>
  DB_NAME=<nome do banco de dados>
  ```
  6 - Crie a estrutura do banco de dados: <code> mysql -u root -p < create_database.sql </code> <br/>
  7 - Quando solicitado, insira sua senha <br/>
  8 - Popule o banco: <code> python3 CSVLoader.py </code> <br/>
  9 - Execute a aplicação com <code> python3 CSVLoader.py </code> <br/>
  </details>
  
<details>
  <summary> Funcionalidades </summary> <br/>
   * Consulta de transações por ID de usuário: o sistema irá verificar se o user_id informado consta em algum dos relatórios, e informará se é suspeito ou não.
   * Relatórios: o sistema gera relatórios com informações relevantes sobre as transações analisadas. 
      - Os relatórios disponíveis são:
</details>
  

<br/><br/>
<h1 align="center">(README EM CONSTRUÇÃO)</h1>
