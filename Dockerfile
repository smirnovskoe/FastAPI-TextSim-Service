FROM python:3.7.10

LABEL user="yanix"

RUN mkdir -p /usr/src/fastapi-service

WORKDIR /usr/src/fastapi-service

COPY . /usr/src/fastapi-service

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]