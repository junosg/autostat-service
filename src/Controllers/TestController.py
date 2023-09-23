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
        headers = request.headers

        if (headers.get('auth') and headers['auth'] == 'JunoDev2023'):
            TestRouteValidate(request.json)
            dataSource = DataSource(request.json['data'], request.json['predictor'], request.json['outcome'], request.json['predictorPaired'])

            result = TestService(dataSource).autoAnalyze()
            return jsonify(result)
        else:
            return jsonify({'message': 'Unauthorized'}), 401

    except Exception as error:
        logging.error(error)
        return jsonify({'message': 'Analysis failed. Please try again.'}), 403