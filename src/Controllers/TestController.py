from flask import Blueprint, request

from src.Services.Tests.TwoGroups.TwoGroupsService import TwoGroupsService
from src.Utils.DataSource import DataSource

test_bp = Blueprint('test', __name__)



@test_bp.route('/test', methods=['POST'])
def test():
    dataSource = DataSource(request.json['data'], request.json['predictor'], request.json['outcome'])

    result = TwoGroupsService(dataSource).analyze()
    result["descriptives"] = dataSource.descriptives

    return result