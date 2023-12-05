FROM python:3.10-slim

WORKDIR /project

ENV PYTHONUNBUFFERED 1

COPY ./project .

RUN chmod +x entrypoint.sh

EXPOSE 8000
ENTRYPOINT [ "sh", "entrypoint.sh" ]
