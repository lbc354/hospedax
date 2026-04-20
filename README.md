# QUICKSTART

python -m venv venv

(Windows) venv/Scripts/activate

python.exe -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

# ROTAS

## HOME

[GET] /hospedax/ -> home page

## DESTINO

[GET]      /hospedax/destino/           -> list

[GET]      /hospedax/destino/1/         -> retrieve

[GET,POST] /hospedax/destino/criar/     -> create

[GET,POST] /hospedax/destino/editar/1/  -> update

[POST]     /hospedax/destino/deletar/1/ -> delete

## USUARIO

[GET,POST] /hospedax/usuario/login/            -> login

[POST]     /hospedax/usuario/logout/           -> logout

[GET]      /hospedax/usuario/                  -> list

[GET]      /hospedax/usuario/inativos/         -> list

[GET]      /hospedax/usuario/perfil/<int:pk>/  -> retrieve

[GET]      /hospedax/usuario/perfil/           -> retrieve

[GET,POST] /hospedax/usuario/criar/            -> create

[GET,POST] /hospedax/usuario/editar/<int:pk>/  -> update

[GET,POST] /hospedax/usuario/editar/           -> update

[POST]     /hospedax/usuario/deletar/<int:pk>/ -> delete
