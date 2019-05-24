FROM python:3.7

## Ensure that Python outputs everything that's prinsted inside the application
# rather than buffering it.
ENV PYTHONBUFFERED 1

# create the woirkdir
RUN mkdir /code

WORKDIR /code

# Add requirements to container
ADD requirements.txt /code/

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

# Add current directory to Docker container
ADD . /code/