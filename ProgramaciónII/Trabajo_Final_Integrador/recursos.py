from flask_restful import Resource
from flask import request

import json

from integrador import *

class RecursoBodega(Resource):

    def get(self, id):
        bodega = Vinoteca.buscarBodega(id)
        if isinstance(bodega, Bodega):
            return json.loads(json.dumps(bodega.convertirAJSONFull())), 200
        else:
            return {"error": "Bodega no encontrada"}, 404


class RecursoBodegas(Resource):

    def get(self):
        orden = request.args.get("orden")
        if orden:
            reverso = request.args.get("reverso")
            bodegas = Vinoteca.obtenerBodegas(
                orden=orden, reverso=reverso == "si"
            )
        else:
            bodegas = Vinoteca.obtenerBodegas()
        return (
            json.loads(json.dumps(bodegas, default=lambda o: o.convertirAJSON())),
            200,
        )
47098080

class RecursoCepa(Resource):

    def get(self, id):
        cepa = Vinoteca.buscarCepa(id)
        if isinstance(cepa, Cepa):
            return json.loads(json.dumps(cepa.convertirAJSONFull())), 200
        else:
            return {"error": "Cepa no encontrada"}, 404


class RecursoCepas(Resource):

    def get(self):
        orden = request.args.get("orden")
        if orden:
            reverso = request.args.get("reverso")
            cepas = Vinoteca.obtenerCepas(orden=orden, reverso=reverso == "si")
        else:
            cepas = Vinoteca.obtenerCepas()
        return (
            json.loads(json.dumps(cepas, default=lambda o: o.convertirAJSONFull())),
            200,
        )


class RecursoVino(Resource):

    def get(self, id):
        vino = Vinoteca.buscarVino(id)
        if isinstance(vino, Vino):
            return json.loads(json.dumps(vino.convertirAJSONFull())), 200
        else:
            return {"error": "Vino no encontrado"}, 404


class RecursoVinos(Resource):

    def get(self):
        anio = request.args.get("anio")
        if anio:
            anio = int(anio)
        orden = request.args.get("orden")
        if orden:
            reverso = request.args.get("reverso")
            vinos = Vinoteca.obtenerVinos(
                anio, orden=orden, reverso=reverso == "si"
            )
        else:
            vinos = Vinoteca.obtenerVinos(anio)
        return json.loads(json.dumps(vinos, default=lambda o: o.convertirAJSON())), 200
