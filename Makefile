run:
	@docker compose up

test:
	@pytest --cov

migrate:
	@docker-compose exec web python manage.py migrate

makemigrations:
	@docker-compose exec web python manage.py makemigrations

shell:
	@docker-compose exec web python manage.py shell

superuser:
	@docker-compose exec web python manage.py createsuperuser

collectstatic:
	@docker-compose exec web python manage.py collectstatic --noinput

dcd:
	@docker-compose down

tw-watch:
	@npx tailwindcss -i .\encyclopedia\static\encyclopedia\css\input.css -o .\encyclopedia\static\encyclopedia\css\styles.css --watch

tw-prod:
	@npx tailwindcss -i .\encyclopedia\static\encyclopedia\css\input.css -o .\encyclopedia\static\encyclopedia\css\styles.css --minify

pc:
	pre-commit run --all-files
