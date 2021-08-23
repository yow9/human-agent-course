import logging
import base64

EASY_TO_OPERATE = ["AM", "WAF", "DDOS"]

# The function calculates the score of each security products
def calculate(segment, org_size, sec_department, web, sql, storage, cloud, containers, iot, industrial, internet_exposed, top_concern, top_impact, sensitivity):
    
    products = {
        "AM": 6,
        "EDR": 0,
        "SIEM": 0,
        "CONTAINERS":0,
        "IDENTITY":0,
        "DDOS": 0,
        "VUL_SCANNER": 0,
        "WAF": 0,
        "FIREWALL": 0,
        "SQL": 0,
        "STORAGE":0,
        "CSPM":0,
        "CWPP":0,
        "IOT":0,
        "SCADA":0,
        "APPLICATION_CONTROL": 0,
        "DLP": 0
    }


    # Handle sensitive segments
    if segment.lower() == "health" or segment.lower() == "finance":
        products["APPLICATION_CONTROL"] += 1
        products["DLP"] += 1

    # Handle high availability segments
    if segment.lower() == "e-commerce" or segment.lower() == "manufacturing and infrastructure":
        products["DDOS"] += 1


    # Handle organization size. Over 50, Identities should be monitored. Larger than that, also EDR
    if org_size == "50-200":
        products["IDENTITY"] += 1
    
    if org_size == "200-1000":
        products["IDENTITY"] += 2
        products["EDR"] += 2

    if org_size == "1000+":
        products["IDENTITY"] += 3
        products["EDR"] += 3


    #Handle security department size
    if sec_department.lower() == "5-15":
        products["VUL_SCANNER"] += 1
    
    if sec_department.lower() == "15-50":
        products["SIEM"] += 2
        products["EDR"] += 1
    
    if sec_department.lower() == "50+":
        products["SIEM"] += 3
        products["EDR"] += 1


    # Handle web application:
    if web == "2":
        products["WAF"] += 3
        products["DDOS"] += 3

    if web == "3":
        products["WAF"] += 5
        products["DDOS"] += 5

    
    # Handle SQL
    if sql == "2":
        products["SQL"] += 3

    if sql == "3":
        products["SQL"] += 5
    

    # Handle storage
    if storage == "2":
        products["STORAGE"] += 3
        products["DLP"] += 1

    if storage == "3":
        products["STORAGE"] += 5
        products["DLP"] += 1


    # Handle cloud. Add CSPM. For orgs with larger sec department, add CWPP
    if cloud == "2":
        products["CSPM"] += 3
        if sec_department.lower() != "not exist" and sec_department.lower() != "0-5":
            products["CWPP"] += 3

    if cloud == "3":
        products["CSPM"] += 5
        if sec_department.lower() != "not exist" and sec_department.lower() != "0-5":
            products["CWPP"] += 5


    # Handle containers
    if containers == "2":
        products["CONTAINERS"] += 3

    if containers == "3":
        products["CONTAINERS"] += 5


    # Handle IOT
    if iot == "2":
        products["IOT"] += 3

    if iot == "3":
        products["IOT"] += 5


    # Handle industrial
    if industrial == "2":
        products["SCADA"] += 5

    if industrial == "3":
        products["SCADA"] += 7


    # Handle internet exposed servers. Requires FW, Vul scanner, DDOS protection and also WAF if web server are used
    if internet_exposed.lower() == "yes":
        products["FIREWALL"] += 5
        products["VUL_SCANNER"] += 5
        products["DDOS"] += 3
        if web != "1":
            products["WAF"] += 2

    # Handle top concern

    # If the top concern is misconfiguration, then CSPM, identity protection, and siem can help
    if top_concern.lower() == "environment misconfiguration":
        products["CSPM"] += 2
        products["IDENTITY"] += 2
        products["SIEM"] += 2

    # If the top concern is vul, so add vul scanner
    if top_concern.lower() == "application vulnerability":
        products["VUL_SCANNER"] += 5

    # If the top concern is targeted attack, so add EDR and SIEM
    if top_concern.lower() == "targeted attack (apt)":
        products["SIEM"] += 3
        products["EDR"] += 3
        products["IDENTITY"] += 3


    # Handle top impact

    # If the top impact is data breach, add storage protection
    if top_impact.lower() == "data breach" or top_impact.lower() == "data destruction":
        products["STORAGE"] += 3
        products["DLP"] += 3
    
    # Handle DOS
    if top_impact.lower() == "denial of service":
        products["DDOS"] += 5

    # Handle resource hijack
    if top_impact.lower() == "resource hijacking":
        products["EDR"] += 2
        products["DDOS"] += 2


    # Handle sensitive org
    if sensitivity == "3":
        products["APPLICATION_CONTROL"] += 7
        products["DLP"] += 7
    
    if sensitivity == "2":
        products["APPLICATION_CONTROL"] += 3
        products["DLP"] += 3


    # If security department not exist, only "out of the box" products are relevant
    if sec_department.lower() == "not exist":
        products_to_filter = [k for k in products.keys() if k not in EASY_TO_OPERATE]
        for k in products_to_filter:
            products[k] = 0

    return products
