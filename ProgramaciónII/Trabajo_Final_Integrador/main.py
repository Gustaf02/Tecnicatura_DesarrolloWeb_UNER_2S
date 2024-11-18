from flask_cors import CORS
from flask import Flask
from vinoteca import Vinoteca
from flask_restful import Api
from recursos import *  # Asegúrate de importar tus recursos (RecursoBodega, RecursoVino, etc.)

app = Flask(__name__)

# Aquí es donde habilitas CORS en tu aplicación Flask
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})

api = Api(app)
api.add_resource(RecursoBodega, '/api/bodegas/<id>')
api.add_resource(RecursoBodegas, '/api/bodegas')
api.add_resource(RecursoCepa, '/api/cepas/<id>')
api.add_resource(RecursoCepas, '/api/cepas')
api.add_resource(RecursoVino, '/api/vinos/<id>')
api.add_resource(RecursoVinos, '/api/vinos')

if __name__ == "__main__":
    Vinoteca.inicializar()
    app.run(debug=True)
