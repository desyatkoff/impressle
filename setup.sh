#!usr/bin/env bash

mv .env.example .env
echo "$(cat .env)FLASK_SECRET" > .env
uv sync
uv run pybabel compile -f -d translations/
