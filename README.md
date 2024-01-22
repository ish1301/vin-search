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

GitHub Backend Repo: [https://github.com/ish1301/assignment-project](https://github.com/ish1301/assignment-project)

```shell
# Check all values if they needs to be updated
cp env.example .env
docker-compose up -d
```

### Services

- app: Backend service http://localhost:8888
- pg_db: Database service
- db_ui: Database administration http://localhost:8099
- redis: Cache and Message Queue
- celery_broker: Job Queue for running workers

### Django Admin

URL: [http://localhost:8888/admin](http://localhost:8888/admin/)

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

Unit testing is integrated as part of [PR merge workflow](https://github.com/ish1301/edlight-project/actions) and
executed before merges are approved at GitHub. Although unit tests can be executed locally as well.

```shell
docker exec -it app bash
python manage.py test app.tests
```

## Monitoring Celery Events

Navigate to docker image on your DockerDesktop and view logs for container `celery_broker`, In AWS deployment all these logs will go to CloudWatch

## Source Code Formatting

Source code formatting is part of GitHub workflow approval, but you can manually run this with below commands.

```shell
docker exec -it app bash
black api
flake8 api
```
