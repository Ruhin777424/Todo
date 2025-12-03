release: python manage.py migrate --noinput && python manage.py collectstatic --noinput && echo "Database migrations completed"
web: gunicorn todo.wsgi:application --bind 0.0.0.0:$PORT --timeout 60
