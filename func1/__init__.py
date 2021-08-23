import logging
import base64
import json
import time

import azure.functions as func
from .resolvers import get_answer
from .decision_logic import calculate
from .reasoning import prepare_output


def main(req: func.HttpRequest) -> func.HttpResponse:
    '''
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    '''
    
    logging.info('Python HTTP trigger function processed a request.')

    
    # Get the content and parse it
    req_body = req.get_json()
    encoded_content = ""

    try:
        encoded_content = req_body["$content"]
        logging.info("content field found")
    except:
        pass
    
    if encoded_content == "wakeup":
        return func.HttpResponse(f"This HTTP triggered function executed successfully. Wakeup operation")

    #content_str = base64.b64decode(encoded_content)
    #content = json.loads(content_str)
    content = req_body

    # Get details
    # Trim twice because the request that is sent from logic app is different than regular function call.
    segment = get_answer("segment", content).strip("\\n").strip("\n")
    logging.info("segment " + segment)
    org_size = get_answer("org_size", content).strip("\\n").strip("\n")
    logging.info("org_size " + org_size)
    sec_department = get_answer("sec_department", content).strip("\\n").strip("\n")
    logging.info("sec_department " + sec_department)
    web = get_answer("web", content).strip("\\n").strip("\n")
    logging.info("web " + web)
    sql = get_answer("sql", content).strip("\\n").strip("\n")
    logging.info("sql " + sql)
    storage = get_answer("storage", content).strip("\\n").strip("\n")
    logging.info("storage " + storage)
    cloud = get_answer("cloud", content).strip("\\n").strip("\n")
    logging.info("cloud " + cloud)
    containers = get_answer("containers", content).strip("\\n").strip("\n")
    logging.info("containers " + containers)
    iot = get_answer("iot", content).strip("\\n").strip("\n")
    logging.info("iot " + iot)
    industrial = get_answer("industrial", content).strip("\\n").strip("\n")
    logging.info("industrial " + industrial)
    internet_exposed = get_answer("internet_exposed", content).strip("\\n").strip("\n")
    logging.info("internet_exposed " + internet_exposed)
    top_concern = get_answer("top_concern", content).strip("\\n").strip("\n")
    logging.info("top_concern " + top_concern)
    top_impact = get_answer("top_impact", content).strip("\\n").strip("\n")
    logging.info("top_impact " + top_impact)
    sensitivity = get_answer("sensitivity", content).strip("\\n").strip("\n")
    logging.info("sensitivity " + sensitivity)

    scores = calculate(segment, org_size, sec_department, web, sql, storage, cloud, containers, iot, industrial, internet_exposed, top_concern, top_impact, sensitivity)

    sorted_products = dict(sorted(scores.items(), key = lambda kv: kv[1], reverse=True))
    # Convert the score to percentage
    products_final_dict = convert_to_percentage(sorted_products)
    output = prepare_output(products_final_dict)

    
    time.sleep(2)
    return func.HttpResponse(output)

# The function gets a dictionary with scores and convers the scores to percentage
def convert_to_percentage(products):
    products_with_percentage = {}
    scores_sum = sum(products.values())

    for k in products:
        if products[k] != 0:
            products_with_percentage[k] = round((products[k] / scores_sum) * 100)

    return products_with_percentage

