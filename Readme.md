# Django Project with Docker Compose, Makefile, and PostgreSQL

This project serves as a template for quickly starting a Django application using Docker Compose for containerization, Makefile for process management, and PostgreSQL as the database.

## Installation and Setup

### Requirements

- Docker
- Docker Compose
- GNU Make (optional)

### Steps

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

2. Copy `.env.example` to `.env` and configure the environment variables if necessary:

```bash
cp .env.example .env
```

3. Start the containers using Docker Compose:

```bash
docker-compose up -d —build
```

4. Apply Django migrations:
```bash
make migrate
```

5. Create a superuser (optional):

```bash
make createsuperuser
```

6. Now you can open your application in a browser at [http://localhost:8000](http://localhost:8000).

## Makefile Commands

- `make app` - up application and database/infrastructure
- `make app-logs` - follow the logs in app container
- `make app-down` - down application and all infrastructure
- `make storages` - up only storages. You should run your application locally for debugging/developing
- `make storages-logs` - follow the logs in storages containers
- `make storages-down` - down all infrastructure

## Most Used Django Specific Commands

- `make migrations` - make migrations to models
- `make migrate` - Apply Django migrations
- `make createsuperuser` - Create a Django superuser
- `make collectstatic` - collect static files



## Project Structure

- `src/`: Source code of the Django application.
- `docker-compose.yml`: Docker Compose configuration file.
- `Makefile`: File for managing processes using the make command.
- `.env.example`: Example environment variables file. Copy it to `.env` and configure as needed.

## Contributions

If you have suggestions or improvements, feel free to make a Pull Request or create an Issue.

## License

This project is licensed under the [MIT License](LICENSE).