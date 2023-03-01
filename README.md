# LittleLemon

Coursera Meta Back-End Developer Capstone Project

## Setup

If you have [Docker](https://www.docker.com/) and the [Remote Developement](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) extension of vscode you can open the repository in a devcontainer that automatically installs mysql, django and the required dependencies.

Otherwise run `pipenv install`. Be sure to have mysql installed and check the settings.py for the database required settings.

1. `python manage.py makemigrations`
2. `python manage.py migrate`
3. `python manage.py runserver`
4. `python manage.py test tests`
