# sudo apt-get install python3-venv
# python3 -m venv ./venv
# pip3 install Flask
# pip3 install autopep8

# export FLASK_APP=app.py

# ruta inicial

# flask run || flask run --host=0.0.0.0
#app.run(debug=True, host="0.0.0.0", port=3000)

# Incertar primer error. Retornar un entero.
# Explicar HTTP retorna texto

# export FLASK_ENV=development

# Navegador. Mostrar la peticion htttp y la respuesta

# Explicar flask esta creando un web server

# crear base de datos
# JINJA

# pip freeze > requirements.txt

from flask import Flask
from controllers.students_controller import controller

app = Flask(__name__)


app.register_blueprint(controller)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5001)
