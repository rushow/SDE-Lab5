import logging
from api.linkedin_crawler import *
import azure.functions as func
from api.api_utils import *

# get_job(2846000000)
# get_job(2843000055)
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        type = req.route_params.get('type')
        if (type == 'job'):
            # 2846001789
            # http://localhost:7071/api/Linkedin/job?job_id=2845615594
            job_id = req.params.get('job_id')
            return func.HttpResponse(ResponseSuccess(get_job(job_id)), mimetype="application/json")

        if (type == 'post'):
            # https://www.linkedin.com/posts/tom-alder_strategy-fintech-payments-activity-6835038759793381376-gz2F
            # http://localhost:7071/api/Linkedin/post/?post_url=https://www.linkedin.com/posts/tom-alder_strategy-fintech-payments-activity-6835038759793381376-gz2F
            post_url = req.params.get('post_url')
            return func.HttpResponse(ResponseSuccess(get_post(post_url)), mimetype="application/json")

        if (type == 'pulse'):
            # https://www.linkedin.com/pulse/future-ge-larry-culp
            # http://localhost:7071/api/Linkedin/pulse/?pulse_url=https://www.linkedin.com/pulse/future-ge-larry-culp
            pulse_url = req.params.get('pulse_url')
            return func.HttpResponse(ResponseSuccess(get_pulse(pulse_url)), mimetype="application/json")

        if (type == 'main-hub'):
            # http://localhost:7071/api/Linkedin/main-hub
            return func.HttpResponse(ResponseSuccess(get_main_hub_topics()), mimetype="application/json")

        if (type == 'child-hub'):
            # http://localhost:7071/api/Linkedin/child-hub?hub_url=https://www.linkedin.com/content-hub/accounting-f1/?trk=content-hub-home_explore-career-topics-pill
            hub_url = req.params.get('hub_url')
            return func.HttpResponse(ResponseSuccess(get_child_hub_topics(hub_url)), mimetype="application/json")

        if (type == 'post-hub'):
            # http://localhost:7071/api/Linkedin/post-hub?hub_url=https://www.linkedin.com/content-hub/accounting-f1/?trk=content-hub-home_explore-career-topics-pill
            # http://localhost:7071/api/Linkedin/post-hub?hub_url=https://www.linkedin.com/content-hub/accountant-t40/?trk=aside-explore-pill
            
            hub_url = req.params.get('hub_url')
            return func.HttpResponse(ResponseSuccess(get_post_links_in_topic(hub_url)), mimetype="application/json")

        if (type == 'post-content-hub'):
            # http://localhost:7071/api/Linkedin/post-content-hub?hub_url=https://www.linkedin.com/content-hub/accounting-f1/?trk=content-hub-home_explore-career-topics-pill
            # http://localhost:7071/api/Linkedin/post-content-hub?hub_url=https://www.linkedin.com/content-hub/accountant-t40/?trk=aside-explore-pill
            
            hub_url = req.params.get('hub_url')
            return func.HttpResponse(ResponseSuccess(get_post_from_hub(hub_url)), mimetype="application/json")

        if (type == 'search-geo'):
            # http://localhost:7071/api/Linkedin/search-geo?location=Trento
            location = req.params.get('location')
            return func.HttpResponse(ResponseSuccess(json.loads(search_geo_id(location))), mimetype="application/json")

        if (type == 'search-job'):
            # http://localhost:7071/api/Linkedin/search-job?title=ComputerScience&location=Colorado&paging=1
            title = req.params.get('title')
            location =  req.params.get('location')
            geo_id =  req.params.get('geo_id')
            if geo_id is None:
                geo_id = ''

            paging = req.params.get('paging')
            if paging is None:
                paging = '1'

            return func.HttpResponse(ResponseSuccess(search_job(title, location, paging, geo_id)), 
                        mimetype="application/json")

        return func.HttpResponse(ResponseFail('Route not found'), mimetype="application/json")
    except Exception as e:
        traceback.print_exc() 
        logging.error('Error ' + str(e))

        return func.HttpResponse(
             ResponseFail("Error " + str(e)),
             mimetype="application/json", status_code=400
        )
