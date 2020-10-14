FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app

RUN python setup.py install

WORKDIR /app/build/lib/lugat

ENTRYPOINT [ "python", "cli.py" ]
