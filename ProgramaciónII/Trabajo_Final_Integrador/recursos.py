from flask_restful import Resource
from flask import request

import json

import vinoteca

from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class RecursoBodega(Resource):



    def get(self, id):
        bodega = vinoteca.Vinoteca.buscarBodega(id)
        if isinstance(bodega, Bodega):
            return json.loads(json.dumps(bodega.convertirAJSONFull())), 200
        else:
            return {"error": "Bodega no encontrada"}, 404


class RecursoBodegas(Resource):
    def get(self):
        orden = request.args.get('orden')
        reverso = request.args.get('reverso', 'no') == 'si'
        bodegas = vinoteca.Vinoteca.obtener_bodegas(orden, reverso)
        if bodegas:
            bodegas_json = [b.convertirAJSON() for b in bodegas]
            return json.loads(json.dumps(bodegas_json)), 200
        else:
            return {"error": "No se encontraron bodegas"}, 404


class RecursoCepa(Resource):

    def get(self, id):
        cepa = vinoteca.Vinoteca.buscarCepa(id)
        if isinstance(cepa, Cepa):
            return json.loads(json.dumps(cepa.convertirAJSONFull())), 200
        else:
            return {"error": "Cepa no encontrada"}, 404


class RecursoCepas(Resource):
    def get(self):
        orden = request.args.get('orden')
        reverso = request.args.get('reverso', 'no') == 'si'
        cepas = vinoteca.Vinoteca.obtener_cepas(orden, reverso)
        if cepas:
            cepas_json = [c.convertirAJSON() for c in cepas]
            return json.loads(json.dumps(cepas_json)), 200
        else:
            return {"error": "No se encontraron cepas"}, 404



class RecursoVino(Resource):

    def get(self, id):
        vino = vinoteca.Vinoteca.buscarVino(id)
        if isinstance(vino, Vino):
            return json.loads(json.dumps(vino.convertirAJSONFull())), 200
        else:
            return {"error": "Vino no encontrado"}, 404



class RecursoVinos(Resource):
    def get(self):
        orden = request.args.get('orden')
        reverso = request.args.get('reverso', 'no') == 'si'
        anios = request.args.get('anios')
        if anios:
            anios = [int(anio) for anio in anios.split(',')]
        vinos = vinoteca.Vinoteca.obtener_vinos(orden, reverso, anios)
        if vinos:
            vinos_json = [v.convertirAJSON() for v in vinos]
            return json.loads(json.dumps(vinos_json)), 200
        else:
            return {"error": "No se encontraron vinos"}, 404


