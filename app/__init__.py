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

from app.gracenote.controllers import gracenote as gracenote_module
app.register_blueprint(gracenote_module, )

from app.auth.controllers import auth as auth_module
app.register_blueprint(gracenote_module, )

from app.notification.controllers import notification as notification_module
app.register_blueprint(notification_module, )
