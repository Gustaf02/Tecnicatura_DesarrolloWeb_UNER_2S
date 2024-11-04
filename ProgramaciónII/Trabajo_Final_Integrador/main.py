from integrador import *
from flask_restful import Resource, Api  # Asegúrate de importar Api también
from flask import Flask, request  # Aquí importamos Flask

# API
from recursos import *

if __name__ == "__main__":
    Vinoteca.inicializar()

    app = Flask(__name__)  # Ahora Flask debería estar definido

    api = Api(app)
    api.add_resource(RecursoBodega, '/api/bodegas/<id>')
    api.add_resource(RecursoBodegas, '/api/bodegas')
    api.add_resource(RecursoCepa, '/api/cepas/<id>')
    api.add_resource(RecursoCepas, '/api/cepas')
    api.add_resource(RecursoVino, '/api/vinos/<id>')
    api.add_resource(RecursoVinos, '/api/vinos')

    app.run(debug=True)



