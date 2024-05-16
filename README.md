# FunnelFuel Python Technical Challenge

## Goal

The goal of this test is to assess (to some degree) your coding and architectural skills. You're given a simple problem
so you can focus on showcasing development techniques. The challenge has two (or three) parts, the first is simply following a 
set of instructions to get a very basic FastAPI based REST API up and running. The second is to add some additional 
functionality to the API. The optional third part is to create functional tests for the API endpoints.

## Prerequisites

- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)
- `sh`

## Instructions

### Part 1.

#### Basic Setup

The first thing to do it to clone this repository to your local development environment. To do this run the following from 
an appropriate location:

```shell
git clone git@github.com:<REPOSITORY>.git
``` 

Where `<REPOSITORY>` is the name of this repository.

Then `cd` into the project directory, by running:

```shell
cd <REPOSITORY>
```

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

### Part 2.

For the second part, the challenge is to create a second set of api endpoints for the existing entities. These endpoints should be as follows

Adding an item to an existing user. _Some crud code for this may already exist in the repo!_
```shell
curl --location --request POST 'http://localhost:8000/users/{ID}/items/' \
--header 'Content-Type: application/json' \
--data '{
    "title": "Item Title",
    "description": "Item Description"
}'
```

Updating an existing user
```shell
curl --location --request PUT 'http://localhost:8000/users/{ID}' \
--header 'Content-Type: application/json' \
--data '{
    "name": "New Name",
    "password": "new_secret"
}'
```

Deleting an existing user
```shell
curl --location --request DELETE 'http://localhost:8000/user/{ID}'
```

Getting items belonging to a specific user
```shell
curl --location --request GET 'http://localhost/users/{ID}/items/
```

### Part 3 (Optional).

#### Tests

The third part involves creating functional tests that will verify the functionality of the endpoints provided by the API. 
A sample test has been added to the [tests](tests) directory. Feel free to handle loading data to use in the tests however you feel best. 
This could be populating the database with dummy data, using fixtures, etc.

#### Bonus Points

For bonus points make any improvements to the project you see fit. This could be the project structure in general, splitting 
up code across multiple files, adding async, whatever you think.

## Linting

The project includes some tools for automatically linting. These can be run using the following 

```shell
docker compose run api sh -c "poetry run ruff format ."
docker compose run api sh -c "poetry run ruff check . --fix"
```

## Submission instructions

The challenge needs to be submitted as a pull request to this repository so we can leave reviews and have discussion about the application.

### Steps

1. Create a new branch called `dev`
2. Complete the Parts
3. Commit your work
4. Create a PR but don't merge it

The PR description should contain a detailed description of the steps taken for Part 2 & (optionally) Part 3.

## Grading

The reviewers will attribute points on the following categories:

1. How successfully the Parts have been completed
2. Readability of any new code
3. Inclusion of testing
4. Documentation of the code and PR description

## Good luck!  