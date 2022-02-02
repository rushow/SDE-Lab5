import logging
import sys
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info("Python executable path is: {}".format(sys.executable))
 
    return func.HttpResponse(
            "Python executable path is: {}".format(sys.executable),
            status_code=200
    )
