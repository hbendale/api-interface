# Api-interface
This repo hosts code for CRUD Demo

# Build Docker images

# docker login
You might need to login to docker (since in the Deloitte net there are too many requests)

create an account at https://hub.docker.com and then login with

    docker login

## python

### python dev
    docker build --target dev . -t divein-crud-demo-python-dev

    docker run -it -v ${PWD}:/work divein-crud-demo-python-dev

### python app
    docker build --target runtime . -t divein-crud-demo-python

    docker run --rm -p 5000:5000 divein-crud-demo-python