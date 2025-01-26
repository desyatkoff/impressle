import os

import config
import website


app = website.init_flask_app()


if __name__ == "__main__":
    if not os.path.exists(f"{config.PROJECT_ROOT_PATH}/database.db"):
        with app.app_context():
            website.db.create_all()


    app.run(
        host = config.HOST,
        port = config.PORT,
        debug = config.DEBUG_MODE
    )
