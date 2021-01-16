# Workclass API

Workclass API is an API base on Python for provide workclass app.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements.

```bash
pip install -r requirements.txt --no-index --find-links file:///tmp/packages
```

## Usage

Create the migrations first!

```python
python manage.py makemigrations jobapi
```

Run the app

```python
pip freeze > requirements.txt
python manage.py runserver
```

**[NOTE] Please update requimentrs if you have added a library**

```python
pip freeze > requirements.txt
```

**[NOTE] Collect static files for prepare in server**

```python
python manage.py collectstatic
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
