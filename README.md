# DJango Proyect Visual style

## Description

This is a proyect to learn how to use DJango and Python to create a web page.

## Installation

To install DJango you need to have Python installed in your computer. Then you can install DJango using the command:

```
pip install django
```

## Previw

![Preview](https://i.imgur.com/mc0UTp8.png)

### Login page

![Preview](https://i.imgur.com/QX0apVc.png)

### Register page

![Preview](https://i.imgur.com/IHdXuM2.png)

## Usage

Then configure the database in the file:

```
> GenPassProyect/Settings.py
```

```mysql
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "genpassdb",
        "USER": "root",
        # "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
```

To use DJango you need to create a project using the command:

```
django manage.py migrate
```

To run the server you need to use the command:

```
python manage.py runserver
```

## Support

If you have any doubt you can contact me at: [My email](mailto:Serphp@hotmail.com)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Project status

This proyect is still in development.

## Author and Acknowledgment

This proyect was created by Bryan Rodriguez.
