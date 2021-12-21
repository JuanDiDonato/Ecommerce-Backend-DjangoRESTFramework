web: gunicorn server.server.wsgi --log-file -
release: python server.manage.py makemigrations --noinput
release: python server.manage.py collectstatic --noinput
release: python server.manage.py migrate --noinput