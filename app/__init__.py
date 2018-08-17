import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app_setting = os.getenv(
    'APP_SETTING',
    'app.config.DevelopmentConfig'
)

app.config.from_object(app_setting)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.provider.controllers import providers as provide_module
app.register_blueprint(provide_module, )
