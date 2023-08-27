import logging
from flask import Blueprint, request, jsonify

from src.Services.Tests.TestService import TestService
from src.Utils.Validation.TestRouteValidate import TestRouteValidate
from src.Utils.DataSource import DataSource

import json

test_bp = Blueprint('test', __name__)

@test_bp.route('/test', methods=['POST'])
def test():    
    try:
        TestRouteValidate(request.json)
        dataSource = DataSource(request.json['data'], request.json['predictor'], request.json['outcome'])

        result = TestService(dataSource).autoAnalyze()
        return jsonify(result)
    except Exception as error:
        logging.error(error)
        return error, 403