build_containers:
	docker-compose -f docker-compose.yml up --build --remove-orphans

start_containers:
	docker-compose -f docker-compose.yml up

stop_containers:
	docker-compose -f docker-compose.yml down

remove_containers:
	docker-compose -f docker-compose.yml down -v

create_admin:
	python manage.py shell -c "from apps.staff.models import User; User.objects.create_superuser('BestAdmin', 'admin@gmail.com', 'admin', first_name='Best', last_name='Admin')"

create_admin_in_container:
	docker exec -it project_web_1 python manage.py shell -c "from apps.staff.models import User; User.objects.create_superuser('BestAdmin', 'admin@gmail.com', 'admin', first_name='Best', last_name='Admin')"

populate_db:
	docker exec -it project_web_1 python manage.py loaddata test_data/db_dump.json