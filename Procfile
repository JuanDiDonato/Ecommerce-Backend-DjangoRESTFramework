web: gunicorn server/server:application 
release: python server/manage.py makemigrations --noinput
release: python server/manage.py collectstatic --noinput
release: python server/manage.py migrate --noinput