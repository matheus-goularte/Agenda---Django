# Iniciar o projeto Django

python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp contact

# Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Configure o .gitignore

git init

git add .
git commit -m 'Mensagem'   AQUI É A MENSAGEM DA ALTERAÇÃO (DESCRIÇÃO)
git push    PARA COMITAR


git remote add origin git@github.com:matheus-goularte/Agenda---Django.git
