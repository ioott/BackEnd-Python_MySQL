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
  <a href="#pr%C3%B3ximos-passos">Próximos Passos</a>
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
  1 - Clone o repositório em sua máquina: <code> git@github.com:ioott/cw.git </code> <br/><br/>
  2 - Acesse o diretório do sistema: <code> cd cw.git </code> <br/><br/>
  3 - Crie um ambiente virtual e ative: <code> python3 -m venv .venv && source .venv/bin/activate </code> <br/><br/>
  4 - Instale as dependências do sistema: <code> python3 -m pip install -r dev-requirements.txt </code> <br/><br/>
  5 - Crie um arquivo <code> .env </code> na raiz e coloque as variáveis de configuração do banco de dados:

  ```
  DB_HOST=<host do banco de dados>
  DB_USER=<usuário do banco de dados>
  DB_PASSWORD=<senha do usuário do banco de dados>
  DB_NAME=<nome do banco de dados>
  ```
  6 - Crie o banco de dados no MySQL. Para isso, execute o comando <code> mysql -u <username> -p < create_database.sql </code> no terminal, substituindo <username> pelo seu nome de usuário do MySQL e inserindo a senha quando solicitado <br/><br/>
  7 - Popule o banco: <code> python3 utils/CSVLoader.py </code> <br/><br/>
  8 - Execute a aplicação com <code> python3 CSVLoader.py </code> <br/>
  </details>
  
<details>
  <summary> Funcionalidades </summary>
  
* Consulta de transações por ID de usuário: <br/>
      O sistema irá verificar se o user_id informado consta em algum dos relatórios, e informará se é suspeito ou não.<br/>
  
* Relatórios: 
      O sistema gera relatórios com informações relevantes sobre as transações analisadas. <br/>
      Os relatórios disponíveis são:<br/>
  
      - Valores altos
      - Ocorridas entre 00:00h e 05:59h
      - Mesmo usuário em um curto espaço de tempo
      - Mesmo cartão em dispositivos diferentes
      - Mesmo usuário com muitas transações
  
Ao escolher uma opção, o relatório correspondente será impresso em tela e exportado em formato CSV para a pasta exported_reports.
  
</details>

## Próximos passos

* Adicionar tratamento de erros
* Refatorar o código para adaptá-lo ao padrão Strategy, melhorando a legibilidade e organização
* Implementar testes automatizados para garantir a integridade da aplicação
* Integrar com outras fontes de dados além do CSV
* Utilizar a biblioteca Pandas para melhorar a apresentação do dados
  
#

<br/>

[Gravação de tela de 17-02-2023 16:19:38.webm](https://user-images.githubusercontent.com/98191041/219767707-288e7bf4-91d5-4789-a62e-1b715149679a.webm)

#

Este sistema foi desenvolvido por Vania Ioott.<br/>
Encontrou algum erro? Tem alguma sugestão? Faça contato! <br/>

#
  
<div align="center">
    <p align="center">
        <a href="https://www.linkedin.com/in/vania-ioott/">
            <img src="https://raw.githubusercontent.com/gauravghongde/social-icons/master/SVG/Color/LinkedIN.svg" width="50" height="50" />
        </a>
        <a href="mailto:vioott@gmail.com">
            <img src="https://raw.githubusercontent.com/gauravghongde/social-icons/master/SVG/Color/Gmail.svg" width="50" height="50" />
        </a>
        <a href="https://wa.me/5521999732102">
            <img src="https://raw.githubusercontent.com/gauravghongde/social-icons/master/SVG/Color/WhatsApp.svg" width="50" height="50" />
        </a>
    </p>
</div>

