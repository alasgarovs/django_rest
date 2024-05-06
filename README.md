# Python's Django Rest Framework

## Installation and Usage

### Clone the repository.

```console
https://github.com/alasgarovs/django_rest.git
cd django_rest
```

### Set Development Enviroment
- Create virtualenv in the project root directory named ".venv" (i use python3.12).
```console
python3.12 -m venv .venv
```
- Add the following statements to end of the  ".venv/bin/activate" file:
```console
echo "export DJANGO_SETTINGS_MODULE=main.development" >> .venv/bin/activate
```
- Install the required dependencies.
```console
pip install -r requirements.txt
```
- Create `.env` file and add `SECRET_KEY`: Create a file named .env in the root directory of project.
```console
echo "SECRET_KEY=your_secret_key_here" > .env
```

- And create `migrations` files and `migrate`:
```console
python manage.py makemigrations
python maanage.py migrate
```