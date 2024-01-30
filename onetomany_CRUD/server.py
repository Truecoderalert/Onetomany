from flask_app import app
from flask_app.controllers import controllers_dojos
from flask_app.models import models_dojo
from flask_app.models import models_ninja
from flask_app.controllers import controllers_ninjas


if __name__=='__main__':
    app.run(debug=True)