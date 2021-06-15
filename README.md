# Omni Latam Ecommerce

* Super User admin

## Comandos

### Start local server

```console
pipenv run start
```

### Run tests

```console
pipenv run test
```

### Start local server

```console
pipenv run start
```

## Docker deployment

### Build

```console
docker build -t omnilatam .
```

### Deploy

```console
docker run -d -p 80:8000 omnilatam
```


### API Postman
importar el archivo postman con el consumo de las api
.API_omniLatam_ecommerce.postman_collection.json

### Opción 1. Ejecutar con pipenv


```console
pip install pipenv
pipenv install

pipenv run start 9097
pipenv run test
pipenv run makemigrations
pipenv run migrate
```

### Opción 2. Ejecutar con virtualenv

```console
pip install virtualenv
# cambiar python3.7 por la ubicación del python 3.7 
virtualenv env_omniLatam_ecommerce -p python3.7
source env_omniLatam_ecommerce/bin/activate
```
