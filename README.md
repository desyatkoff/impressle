# Impressle

<p align="center">
    <img
        src = "/website/static/images/logo-full-dark.svg"
        height = "256"
    />
</p>


## Description

**Unleash your creativity!**

**Impressle** is a unique social network where you have to draw by hand, not uploading image files. Follow your favorite artists, give likes to other users' pictures and make your own ones. It's fun, just try it!


## Table of Contents

1. [Title](#impressle)
2. [Description](#description)
3. [Table of Contents](#table-of-contents)
4. [Tech Stack](#tech-stack)
5. [Features](#features)
6. [Install and Setup](#install-and-setup)
    * [Easy Method](#easy-method)
    * [Normal Method](#normal-method)
    * [Using Docker Method](#using-docker-method)
7. [Contributing](#contributing)
8. [Support the Project](#support-the-project)


## Tech Stack
\
<img
    src = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"
    height = "64"
/>
<img
    src = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg"
    height = "64"
/>
<img
    src = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original.svg"
    height = "64"
/>
<img
    src = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original.svg"
    height = "64"
/>
<img
    src = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg"
    height = "64"
/>
<img
    src = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg"
    height = "64"
/>
<img
    src = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg"
    height = "64"
/>

* **Backend**
    + Python
        - [Flask](https://flask.palletsprojects.com/en/stable)
        - [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/stable)
    + SQLite Database
* **Frontend**
    + HTML
    + CSS
        - [Pure.CSS](https://pure-css.github.io)
    + JavaScript


## Features

* **Account System**
    + Sign up
    + Log in
    + Account settings
        - Profile
            - Edit "About Me"
        - Privacy
            - Show followers count in your profile?
            - Allow users to comment your pictures?
        - Danger Zone
            - Delete account
    + Follow/Unfollow other users
    + Log out
* **Create Pictures**
* **Interact With Pictures**
    + Like
    + Dislike
    + Comment
* **Delete Pictures and Comments**
* **Ranking System**
    + Get more karma to upgrade rank
        - +1 karma for publishing a picture
        - +1 karma for getting a like/comment
        - +1 karma for getting a follower
        - Visit the FAQ (Frequently Asked Questions) page for more details
* **Admin Panel**
    + Inspect the database
    + Edit the database (not recommended though)
    + Ban users/pictures/comments
        - Banned user will lost the access to their account and will be marked with `[ BANNED ]` tag in their profile
        - Banned picture will not be shown in Feed page, but still can be accessed by visiting URL ("/picture/{picture_uid}") and author's profile
        - Banned comment's text will be changed to `[ BANNED ]`


## Install and Setup

### Easy Method

1. **Clone the Repository**
    ```Shell
    $ git clone https://github.com/desyatkoff/impressle.git
    ```
2. **Go to the Repository Directory**
    ```Shell
    $ cd impressle/
    ```
3. **Launch Auto-Setup Script (`setup.sh`)**
    ```Shell
    $ sh setup.sh
    ```
4. **Launch the Web App**
    ```Shell
    $ python main.py
    ```

### Normal Method

1. **Clone the Repository**
    ```Shell
    $ git clone https://github.com/desyatkoff/impressle.git
    ```
2. **Go to the Repository Directory**
    ```Shell
    $ cd impressle/
    ```
3. **Edit Configuration Files**
    * Environment variables (secret data)
        + Rename `.env.example` to `.env`
        ```Shell
        $ mv .env.example .env
        ```
        + Edit `.env` using your code editor
    * Other configs (public data)
        + Edit `config.py` using your code editor
4. **Install `pipenv`**
    ```Shell
    $ pip install pipenv
    ```
5. **Add `pipenv` to PATH**
6. **Create the Virtual Environment**
    ```Shell
    $ pipenv install --python 3.9
    ```
7. **Lock the `Pipfile`**
    ```Shell
    $ pipenv lock
    ```
8. **Install All the Dependencies**
    ```Shell
    $ pipenv sync
    ```
9. **Activate the Virtual Environment**
    ```Shell
    $ pipenv shell
    ```
10. **Launch the Web App**
    * Using Python
        ```Shell
        $ python main.py
        ```
    * Using Flask
        ```Shell
        $ flask --app main:app run
        ```
    * Using Gunicorn
        ```Shell
        $ gunicorn main:app
        ```

### Using Docker Method

1. **Clone the Repository**
    ```Shell
    $ git clone https://github.com/desyatkoff/impressle.git
    ```
2. **Go to the Repository Directory**
    ```Shell
    $ cd impressle/
    ```
3. **Edit Configuration Files**
    * Environment variables (secret data)
        + Rename `.env.example` to `.env`
        ```Shell
        $ mv .env.example .env
        ```
        + Edit `.env` using your code editor
    * Other configs (public data)
        + Edit `config.py` using your code editor
4. **Build the Docker Image**
    ```Shell
    $ docker build -t impressle:latest
    ```
5. **Run Your New Docker Image**
    ```Shell
    $ docker run impressle:latest
    ```


## Contributing

**Want to help? You can update or fix something, here's how to contribute to the project repository:**

1. Fork the repository
2. Create new branch
3. Edit some code
4. Push the changes to your branch
5. Open a pull request here

> [!NOTE]\
> **Prefer naming your git commits something like that:**
>
> 1. "UPDATE: Added/Improved/Removed the \*feature\*"\
> *OR*\
> "ADD: \*Feature\*"\
> "REMOVE: \*Feature\*"
> 2. "FIX: Fixed the \*bug\*"
> 3. "COMMENT: Added/Edited/Removed a comment on line \*123\*"

Done! I'll review your code changes and *maybe* will accept them. Even just adding comments for some lines is a good contribution


## Support the Project

**Want to help but don't know how to code?**

* Crypto (only send TON, other coins will be lost!)
    ```
    UQCsdH1ItNGo9RB8f8AoNfGTr9gdPAi_YkCV2hk7_MVOHydV
    ```
* ...or just give a star to this repository and tell your friends about **Impressle** :)
