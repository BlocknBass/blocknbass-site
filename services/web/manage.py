from flask.cli import FlaskGroup

from blocknbass import create_app

cli, app = FlaskGroup(create_app=create_app), create_app()

if __name__ == "__main__":
    cli()
