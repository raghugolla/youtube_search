FROM python:3.7.1

RUN pip install pipenv

WORKDIR /setup

ADD Pipfile /setup
ADD Pipfile.lock /setup

RUN pipenv install --dev --system

# Add these files AFTER pipenv install so that rebuilds are quick if Pipfile
# hasn't changed
ADD . /setup

ADD ./setup_sqs.py /bin

RUN chmod +x /bin/setup_sqs.py
