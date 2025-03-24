# Django Office Employee Management System
![{7B953034-CECF-40F3-AA6B-5E518D9EDBA4}](https://github.com/user-attachments/assets/469ac35d-053e-4f3a-be4b-21d66f625332)

# running with Docker
## Build the Docker container image
```
docker build -t django-docker .
```
## Build and run the project
To build and start your containers, run:
```
docker compose up --build
```
Django application should be accessible at http://localhost:8000
### Creating database tables
To verify the database connection, try running a migration:
```
docker compose run django-web python manage.py migrate
```
### Collect statics
And dont forget to make static files ready:
```
docker compose run django-web python manage.py collectstatic
```
# Demo
## Request forms:
![{C620EA73-3267-412E-942C-A9E49680E3EE}](https://github.com/user-attachments/assets/27718f36-0ffb-45ba-b8ca-bc6a8e34360b)
## Data tables
![{A611688B-1DB9-4968-8BBB-CC5AEC8DC1CA}](https://github.com/user-attachments/assets/ed8d47ef-29f3-4a52-9b72-03b3ec6677b9)
## Notes for requests
![{3FAD1046-FFC8-43DF-9D32-9EC511A5D5D2}](https://github.com/user-attachments/assets/e3c41303-32ef-4c50-88b9-1aeff736aaf6)
## Request review
![{F9D4480A-00DF-48DD-867F-95C190E81340}](https://github.com/user-attachments/assets/483c3b69-7b0a-4a71-a2ba-f2b12a4afd09)
## Admin logs
![{16879C14-392F-46F8-97AA-480A148C2478}](https://github.com/user-attachments/assets/3113c92b-47f6-4e02-9456-0c6abc1e8886)
