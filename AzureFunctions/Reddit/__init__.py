import logging

import azure.functions as func
from api.api_utils import *
from api.reddit_crawler import *

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        type = req.route_params.get('type')
        if (type == 'search-reddit'):
            # http://localhost:7071/api/Reddit/search-reddit?trends=Covid, Vaccine

            trends = req.params.get('trends')
            return func.HttpResponse(ResponseSuccess(search_post(trends)), mimetype="application/json")

        return func.HttpResponse(ResponseFail('Route not found'), mimetype="application/json")
    except Exception as e:
        traceback.print_exc() 
        logging.error('Error ' + str(e))

        return func.HttpResponse(
             ResponseFail("Error " + str(e)),
             mimetype="application/json", status_code=400
        )
