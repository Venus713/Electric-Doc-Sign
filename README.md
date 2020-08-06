# DocSign backend

## instruction to lauch on local

You need to have your own virtual development environment based on python3. We use `Django` v3, which requires `python` 3.6 or later version.

### Install dependencies
```
(your_env)$ pip install -r rquirements.txt
```

### Prepare environment variables
Create a `.env` file in the backend project root directory by using `.env.example`.
```
(your_env)$ copy .env.example .env
```
Correct the env file with your own info.

### Migration and create superuser to test and launch on local
```
(your_env)$ python manage.py migrate
(your_env)$ python manage.py createsuperuser
(your_env)$ python manage.py runserver
```

When you are going to test with react app that was deployed to a clouding. Please see `CORS_ORIGIN_WHITELIST` variable in `local.py` file. Suppose that you deployed the frontend to `https://app.docsign.com` then do the following.
```python
CORS_ORIGIN_WHITELIST = ['http://localhost:3000', 'https://app.docksign.com']
```
