mv .env.example .env

echo "$(cat .env)FLASK_SECRET" > .env

pipx install pipenv
pipx ensurepath

pipenv lock
pipenv sync
pipenv shell
