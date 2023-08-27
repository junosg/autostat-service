import logging
from flask import jsonify


class TestRouteValidate():
    
    def __init__(self, request) -> None:
        errors = {}
        logging.error(request)
        
        if "data" not in request:
            errors["data"] = "This is required."
        
        if "predictor" not in request:
            errors["predictor"] = "This is required."
            
        if "outcome" not in request:
            errors["outcome"] = "This is required."
            
        logging.error(errors)
        if errors != {}:
            exception = Exception(errors)
            logging.error(exception)
            raise exception

