In this setup:
web: The web service uses a custom image (my-web-app:latest) that’s built from a Dockerfile in the ./webapp directory. This service exposes port 5000 to the host and sets environment variables for the database connection.
db: The database service uses the MySQL 8.0 image and defines a root password and database name via environment variables. The database data is stored in a Docker volume called db-data for persistence.

project-folder/
├── docker-compose.yml
└── webapp/
    ├── Dockerfile
    └── app.py
    └── requirements.txt
app.py:
This code uses Flask to create a simple app that connects to the MySQL database and returns the name of the database.

Step 5: Build and Run with Docker Compose
Build the Images: Run docker-compose build to build the web application’s Docker image.
Start the Services: Run docker-compose up to start both the web and database services.
Access the Application: You can access the web app at http://localhost:5000, and it should show a message confirming the database connection.

Troubleshooting Tips
Database Connection Issues: If the web app can’t connect to the database, ensure the DATABASE_HOST, DATABASE_USER, and DATABASE_PASSWORD environment variables match the MySQL configuration in docker-compose.yml.
Rebuilding the Application: If you make changes to the application code or Dockerfile, rerun docker-compose up --build to rebuild the images
