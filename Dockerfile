FROM python:3.7

# Build Args
ARG module="omniLatam_ecommerce.settings"
ARG wsgi="omniLatam_ecommerce.wsgi:application"
ARG bind=8000

# Deploy env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=$module
ENV BIND=$bind
ENV WSGI=$wsgi

USER root

# Set workdir
WORKDIR /app

# Add files
ADD . .

# Upgrade PIP
RUN python -m pip install --upgrade pip

# Install Pipenv
RUN pip install -U pipenv

# Install dependencies
RUN pipenv install --deploy --system

# Migrate to DB
RUN python manage.py migrate

# Deploy gunicorn sever
RUN pip install gunicorn
EXPOSE $BIND
ENTRYPOINT /usr/local/bin/gunicorn --bind 0.0.0.0:${BIND} $WSG