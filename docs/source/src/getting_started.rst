Requirements
############

This project requires Docker_ and Docker-Compose_



Getting Started
###############

Clone repository::

    $ git clone https://github.com/devguerreiro/backend-test.git

Change to directory::

    $ cd backend_test/

Get the codes from development branch::

    $ git pull origin development

Add a .env file following the .env.example::

    # config to send email
    EMAIL=""
    # key authentication or password
    KEY=""

    # django settings
    SECRET_KEY=""

    # db settings
    POSTGRES_DB=""
    POSTGRES_USER=""
    POSTGRES_PASSWORD=""

Run container::

    $ docker-compose up -d

Run migrations::

    $ docker container exec backend python manage.py migrate

**This steps order is mandatory**.

The application will be running on **localhost:8000/api/v1/**

.. _Docker: https://docs.docker.com/engine/install/
.. _Docker-Compose: https://docs.docker.com/compose/install/