FROM python:3.7

RUN apt-get update
RUN apt-get upgrade -y

## Ensure that Python outputs everything that's prinsted inside the application
# rather than buffering it.
ENV PYTHONBUFFERED 1

# create the woirkdir
RUN mkdir /code

WORKDIR /code

# Add requirements to container
ADD ./requirements/main.txt /code/

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r /code/main.txt

# Add django directory to Docker container
ADD ./tracker /code/