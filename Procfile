release:python3 manage.py migrate
web: daphne domecode.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python3 manage.py runworker 
