# test-chat-app
This chat app is developed using django and here users can talk to each other privately

# base requirement
python 3.10.6

# how to run this application
1- clone the app from using url : https://github.com/Azamali786/test-chat-app.git
2- move to repo and make venv using : python3 -m venv venv
3- activate venv using : source ven/bin/activate
4- install requirements using : pip install -r requirements.txt
5- run migrate using : python manage.py migrate
5- run server using : python manage.py runserver


## pre-commit commands:
- pre-commit install  => to install pre-commit hooks
- pre-commit autoupdate  => to update all hooks to latest version in pre-commit file.
- pre-commit run --all-files  => to run against all the files in the project.
