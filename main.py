import config
import website


app = website.init_flask_app()


if __name__ == "__main__":
    app.run(
        host = config.HOST,
        port = config.PORT,
        debug = config.DEBUG_MODE
    )
