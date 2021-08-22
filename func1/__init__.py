import logging
import base64
import json

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
    logging.info(req_body)
    logging.info(type(req_body))
    encoded_content = ""

    try:
        encoded_content = req_body["$content"]
        logging.info("content field found")
    except:
        pass
    
    logging.info("aftre try-except")
    if encoded_content == "wakeup":
        return func.HttpResponse(f"This HTTP triggered function executed successfully. Wakeup operation")

    #content_str = base64.b64decode(encoded_content)
    #content = json.loads(content_str)
    content = req_body

    # Get details
    segment = get_answer("segment", content).strip()
    org_size = get_answer("org_size", content).strip()
    sec_department = get_answer("sec_department", content).strip()
    web = get_answer("web", content).strip()
    sql = get_answer("sql", content).strip()
    storage = get_answer("storage", content).strip()
    cloud = get_answer("cloud", content).strip()
    containers = get_answer("containers", content).strip()
    iot = get_answer("iot", content).strip()
    industrial = get_answer("industrial", content).strip()
    internet_exposed = get_answer("internet_exposed", content).strip()
    top_concern = get_answer("top_concern", content).strip()
    top_impact = get_answer("top_impact", content).strip()
    sensitivity = get_answer("sensitivity", content).strip()

    scores = calculate(segment, org_size, sec_department, web, sql, storage, cloud, containers, iot, industrial, internet_exposed, top_concern, top_impact, sensitivity)

    sorted_products = dict(sorted(scores.items(), key = lambda kv: kv[1], reverse=True))
    # Convert the score to percentage
    products_final_dict = convert_to_percentage(sorted_products)
    output = prepare_output(products_final_dict)

    #return func.HttpResponse(f"This HTTP triggered function executed successfully.")
    return func.HttpResponse(output)

# The function gets a dictionary with scores and convers the scores to percentage
def convert_to_percentage(products):
    products_with_percentage = {}
    scores_sum = sum(products.values())

    for k in products:
        if products[k] != 0:
            products_with_percentage[k] = round((products[k] / scores_sum) * 100)

    return products_with_percentage

