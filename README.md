# QUICKSTART

python -m venv venv

venv/Scripts/activate (Windows)

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

# ROTAS

## DESTINO

[GET]      hospedax/           -> list


[GET]      hospedax/1/         -> retrieve

[GET,POST] hospedax/novo/      -> create

[GET,POST] hospedax/editar/1/  -> update

[POST]     hospedax/deletar/1/ -> delete

## USUARIO

[GET,POST] hospedax/usuario/login/     -> login

[POST]     hospedax/usuario/logout/    -> logout

[GET]      hospedax/usuario/           -> list

[GET]      hospedax/usuario/1/         -> retrieve

[GET,POST] hospedax/usuario/novo/      -> create

[GET,POST] hospedax/usuario/editar/1/  -> update

[POST]     hospedax/usuario/deletar/1/ -> delete
