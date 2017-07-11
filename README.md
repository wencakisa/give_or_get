[![Requires.io](https://img.shields.io/requires/github/wencakisa/give_or_get.svg?style=flat-square)](https://raw.githubusercontent.com/wencakisa/give_or_get/master/requirements.txt)

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

# give_or_get

**give_or_get** is a *RESTful API*, written in *Django*.

Sometimes anything is missing in our household. This can be domestic appliances such as a besom, a hand mixer or a TV.

Wouldn't it be fantastic to find someone who can provide you with something you need and who is close to you?

If you don't need something, but want to give something such as an old radio, don't hesitate and just upload it. There will be someone for sure like you, who want to get it.

## Prerequisites

- [Python v3.5+](https://www.python.org/downloads/)
- [pip v9.0.1+](https://pypi.python.org/pypi/pip)

## Tech

**give_or_get** uses a number of open-source projects to work properly:

* [Django](https://github.com/django/django) - A really nice high-level Python web framework
* [Django REST Framework](https://github.com/tomchristie/django-rest-framework) - Framework for building Django REST APIs with one touch
* [REST Condition](https://github.com/caxap/rest_condition) - Complex permissions flow for Django REST Framework
* [drf-nested-routers](https://github.com/alanjds/drf-nested-routers) - Nested routing for Django REST Framework
* [Visual Studio Code](https://github.com/Microsoft/vscode) - A really nice text editor

## Getting started

How to copy this project on your machine and run it:

1. Download a copy from GitHub:

    ```
    $ git clone https://github.com/wencakisa/give_or_get.git
    $ cd give_or_get/
    ```

2. Setup Django requirements:

    ```
    $ pip3 install -r requirements.txt
    $ python3 manage.py makemigrations
    $ python3 manage.py migrate
    ```

3. Create a superuser:

    ```
    $ python3 manage.py createsuperuser
    ```

4. Run the tests:

    ```
    $ python3 manage.py test
    ```

5. Run the local server:

    ```
    $ python3 manage.py runserver
    ```

## API routes

* **/api/items/personal** - List of the items, added by you
* **/api/deals/personal?is_active=(true of false)** - Deals for your items
* **/api/deals/following?is_active=(true of false)** - Deals that you created
* **/api/items** - List of all the items
* **/api/items/:id** - Information for a certain item
* **/api/items/:id/deals** - List with all the deals for this item
* **/api/items/:id/deals/:dealId** - Information for a certain deal

## The admin site

1. `$ python3 manage.py runserver`
2. Visit **http://127.0.0.1:8000/admin/**
3. Log in with your superuser data.
4. Here you can add, update and remove your models.

### TODOs

* [ ] - Create *users* app with registration, login, etc.
* [ ] - Write unit tests for the both *users* & *items* apps.
* [ ] - Probably move *deals* into separate app.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
