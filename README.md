# APP

APP project based on [Django](https://docs.djangoproject.com/en/3.2/) is a high-level
Python web framework that encourages rapid development and clean, pragmatic design.
Built by experienced developers, it takes care of much of the hassle of web
development, so you can focus on writing your app without needing to reinvent the
wheel. It’s free and open source.

## Source Code Owner

**Name:** Ish Kumar  
**Email:** ish1301@gmail.com  
**Role:** Software Architect (_Full Stack Developer with DevOps chops_)

## Local Development

This is the initial setup for Image Analysis App .env.example to .env for the application to run. Navigate to the
project folder and deploy the stack. This command will launch 5 services.

GitHub Backend Repo: [https://github.com/ish1301/vin-frontend](https://github.com/ish1301/vin-frontend)

```shell
# Check all values if they needs to be updated
cp env.default .env
docker-compose up -d
```

### Services

- app: Backend service http://127.0.0.1:8888/
- pg_db: Database service
- db_ui: Database administration http://127.0.0.1:8099/

### Django Admin

URL: [http://127.0.0.1:8888/admin](http://127.0.0.1:8888/admin/)

## Database Migrations

[Migrations are Django](https://docs.djangoproject.com/en/3.2/topics/migrations/)'s way of propagating changes you make
to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly
automatic.

```shell
docker exec -it app bash
python manage.py makemigrations
python manage.py migrate
```

## Unit Testing

Unit testing is integrated as part of [PR merge workflow](#) and
executed before merges are approved at GitHub. Although unit tests can be executed locally as well.

```shell
docker exec -it app bash
python manage.py test
```

## Inventory Data Jobs

To load inventory data into your vehicle database you can leverage existing script to do so

```shell
docker exec -it app bash
python manage.py load_inventory ../data/inventory-listing-2022-08-17.txt
```

## Source Code Formatting

Source code formatting is part of GitHub workflow approval, but you can manually run this with below commands.

```shell
docker exec -it app bash
black api
flake8 api
```
