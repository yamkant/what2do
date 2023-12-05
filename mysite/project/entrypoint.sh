#!/bin/bash

poetry run alembic upgrade head

pip3 install poetry
poetry install
poetry run uvicorn apps.shared_kernel.server:app --host 0.0.0.0