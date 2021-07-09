# Seven_Sails_backend
Aplicação backend voltada para gerenciamento de estoque, visando observar entrada e saida de produtos.


Tendo em vista, o código utilizado neste projeto, é necessário ter a linguagem python instalada na máquina,
se possivel, utilize uma máquina LINUX UBUNTU.

Passos para compilar o código:

##1. Instalação do pip
sudo apt install python3-pip

##2. Passo opcional, faça download da virtualenv, para melhor organização das pastas e de um ambiente com memória alocada
 pip3 install virtualenv
       crie:
       ## Criação do ambiente
       virutalenv seven_sails_env
       ## acesse o diretório que contém a pasta de ambiente pela linha de comando, ativação do ambiente
       . seven_sails_env/bin/activate
       ## Desativação do ambiente
       deactivate
       
##3. Instalação dos pacotes utilizados na aplicação 
pip3 install -r requirements.txt

##4. Rodar os seguintes comandos na pasta base das apps (/Seven_sails/)
python3 manage.py makemigrations

python3 manage.py migrate

##5. Rode o programa na mesma pasta

python3 manage.py runserver

##6. Acesse o programa pelo endereço pelo navegador

http://127.0.0.1:8000/login/
