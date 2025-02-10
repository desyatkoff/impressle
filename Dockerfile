FROM python:3.9

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDONUNBUFFERED 1

RUN pip install pipenv

COPY . .

RUN pipenv install --python 3.9
RUN pipenv lock
RUN pipenv sync

CMD [ "pipenv", "run", "python3", "main.py" ]
