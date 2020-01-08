import requests
import json

from dashboard.confluence.settings import cookie
from dashboard.confluence.get_page import get_page

'''Update page in confluence.

Updates a page by its id with info from a json object.

Args:
    type (int): 1: blogpost
                2: page
                
    title (str): 'any title'
    space (int): 1: Persönliche Bereich
                 2: Wettbewebermonitoring
                 3: Trendmonitoring
                 4: Koordination
                 5: DW Datenanalyse
                 
    body (str): 'any content"
    
    version (int): 'any version number'
    
    id (int): integer with the value of the id

Returns:
    True
    Error message from the API

'''


def update_page(body, id, title=None):

    api_url = 'https://confluence.dw.com/rest/api/content/'
    url = api_url + str(id)

    # call get_page and passes the id
    # store the results in a variable

    try:
        page, r = get_page(id)
    except Exception as e:
        raise Exception(e)        

    type = page['type']
    if not title:
        title = page['title']
    
    body_to_update = page['body']
    space = page['space']

    # add 1 to the current version
    version = page['version'] + 1

    # initiate session object s
    s = requests.Session()

    # use this format when creating a json file or a json object
    page = {'type': type, 'title': title, 'space': {'key': space}, 'body': {'storage': {'value': body, 'representation': 'storage'}}, 'version': {'number': version}, 'id':id}

    #if ancestors:
        #page['ancestors'] =	[{'id':ancestors}]

    # the method json.dumps creates a json object
    page_json = json.dumps(page)  

    # use method post to send data to the api
    r = s.put(url, data=page_json, headers=({'Content-Type':'application/json; charset=UTF-8'}), cookies=cookie)

    # store the json api response as a dictionary in a varible
    r_updated = json.loads(r.text)

    # to check if the page was sucessfuly updated, the updated body is compared with the given function parameter
    # the dictionary structure of body is body.storage.value
    # the dictionary elements must be called one by one, otherwise the function get_value would become too complex
   
    updated_body = r_updated['body']['storage']['value']

    if updated_body != body_to_update:
        print('check if content is updated')
        
    return True, id

    
