## Prerequisites

- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)
- `sh`

#### Basic Setup

Now the project can be run using docker, by running:

```shell
docker-compose up --build
```

This will set up and run the two containers described in the [docker-compose.yaml](docker-compose.yaml) file.

Once this has completed the project should be available on [http://localhost:8000](http://localhost:8000) where a default page should be displayed.

#### Docs

OpenAPI docs are automatically generated, these can be seen here [http://localhost:8000/docs](http://localhost:8000/docs)


#### Endpoints

A set of basic API endpoints have already been added to the application, these are:

For adding a new user
```shell
curl --location --request POST 'http://localhost:8000/users/' \
--header 'Content-Type: application/json' \
--data '{
    "email": "Your Name",
    "password": "secret"
}'
```

For getting all users
```shell
curl --location 'http://localhost:8000/users/'
```

For getting a single user
```shell
curl --location 'http://localhost:8000/users/{ID}'
```

For getting all items
```shell
curl --location 'http://localhost:8000/items/'
```

Try out the above requests in the terminal or something like Postman, bearing in mind that you'll need to run these 
outside of the container.

Congratulations, the application is up and running.

## Linting

The project includes some tools for automatically linting. These can be run using the following 

```shell
docker compose run api sh -c "poetry run ruff format ."
docker compose run api sh -c "poetry run ruff check . --fix"
```
