import requests
import json

from dashboard.confluence.settings import cookie

'''Create new page in confluence.

Create a new page or blog post.

Args:
    type (str):  1: blogpost
                 2: post
    
    title (str): 'any title'

    space:  1: Persönlicher Bereich
            2: Wettbewebermonitoring
            3: Trendmonitoring
            4: Koordination
    
    body (str): 'any content'

Returns:
    id of the created page

'''


def create_page(type, title, space, body, ancestors=None):

    api_url = 'https://confluence.dw.com/rest/api/content/'

    # initiate session object s
    s = requests.Session()

    if type != 'page' and type != 'blogpost':
        raise Exception('type should be page or blogpost')
    
    # use this format when creating a json file or a json object
    page = {'type': type, 'title': title, 'space': {'key': space}, 'body': {'storage': {'value': body, 'representation': 'storage'}}}

    if ancestors:
        page['ancestors'] =	[{'id':ancestors}]

    # the method json.dumps creates a json object
    page_json = json.dumps(page)  

    # use method post to send data to the api
    r = s.post(api_url, data=page_json, headers=({'Content-Type':'application/json; charset=UTF-8'}), cookies=cookie)

    r_dictionary = json.loads(r.text)

    if 'message' in r_dictionary:
        # if the page already exists raise an exception returning the error message from the api
        raise Exception(r_dictionary['message'])

    # if the page is sucessfuly created the function returns the id
    return True, r_dictionary['id']
