# impressle

<p align="center">
    <img
        src = "/website/static/images/logo-full-dark.svg"
        height = "256"
    />
</p>


## Description

**Unleash your creativity!**

**impressle** is a unique social network where you have to draw by hand, not uploading image files. Follow your favorite artists, give likes to other users' pictures and make your own ones. It's fun, just try it!


## Table of Contents

1. [Title](#impressle)
2. [Description](#description)
3. [Table of Contents](#table%20of%20contents)
4. [Tech Stack](#tech%20stack)
5. [Features](#features)
6. [Installation](#installation)
7. [Contributing](#contributing)
8. [Support the Project](#support%20the%20project)


## Tech Stack
\
<img
    src = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg"
    height = "64"
/>
<img
    src = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg"
    height = "64"
/>
<img
    src = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg"
    height = "64"
/>
<img
    src = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg"
    height = "64"
/>
<img
    src = "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"
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


## Features

* Account system
    + Sign up
    + Log in
    + Edit profile
        - Edit "About Me"
    + Log out
* Create pictures
* Interact with pictures
    + Like
    + Comment
* Delete pictures and comments
* Admin panel


## Installation and Launching

1. Clone the repository
    ```Shell
    $ git clone https://github.com/desyatkoff/impressle.git
    ```
2. Go to the repository directory
    ```Shell
    $ cd impressle/
    ```
3. Create and activate Python virtual environment
    * Create
        ```Shell
        $ python3 -m venv .venv/
        ```
    * Activate
        + Windows
            ```Shell
            $ .venv\Scripts\activate
            ```
        + Linux/macOS
            ```Shell
            $ source .venv/bin/activate
            ```
4. Install all the dependencies
    ```Shell
    $ pip3 install -r requirements.txt
    ```
5. Edit `.env` and `config.py` files to make best configuration for you
6. Launch the app on localhost
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


## Contributing

Want to help? You can update or fix something, here's how to contribute to the project repository:

1. Fork the repository
2. Create new branch
3. Edit some code
4. Push the changes to your branch
5. Open a pull request here

> [!NOTE]\
> **Prefer naming your git commits something like that:**
>
> 1. "UPDATE: Added/Removed the \*feature\*"\
> *OR*\
> "ADD: \*Feature\*"\
> "REMOVE: \*Feature\*"
> 2. "FIX: Fixed the \*bug\*"
> 3. "COMMENT: Added/Edited/Removed a comment on line \*123\*"

Done! I'll review your code changes and *maybe* will accept them. Even just adding comments for some lines is a good contribution


## Support the Project

Want to help but don't know how to code?

* Crypto (only send TON, other coins will be lost!)
    ```
    UQCsdH1ItNGo9RB8f8AoNfGTr9gdPAi_YkCV2hk7_MVOHydV
    ```
* ...or just give a star to this repository and tell your friends about **impressle** :)
