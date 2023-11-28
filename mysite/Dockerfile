FROM python:3.10-slim

WORKDIR /project

ENV PYTHONUNBUFFERED 1

COPY ./project .

RUN pip3 install poetry

EXPOSE 8000
RUN poetry install
ENTRYPOINT [ "poetry" ,"run", "uvicorn", "apps.shared_kernel.server:app", "--host", "0.0.0.0" ]
