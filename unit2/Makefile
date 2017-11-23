MANAGE=django-admin.py

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=project.settings $(MANAGE) runserver

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=project.settings $(MANAGE) migrate

make:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=project.settings $(MANAGE) makemigrations

port:
	sudo fuser -k 8000/tcp

mail:
	python -m smtpd -n -c DebuggingServer localhost:1025

super:
	echo "from accounts.models import User; User.objects.create_superuser('root', 'root@root.com', 'root')" | python manage.py shell
