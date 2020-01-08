import requests
import json

from dashboard.confluence.settings import cookie


'''Get page from confluence.

Get page from confluence by its id and return a list with type, title,
space, body, version and link associated with the page.

Args:
    id (int): Integer with the value of the id.

Returns:
    list: type, title, space key, body, version, link.

'''


def get_page(id):

    api_url = 'https://confluence.dw.com/rest/api/content/'
    
    # create a url to request the page data and expand body.storage, version space and children.page
    url = api_url + str(id) + '?expand=body.storage,version,space,children.page'

    # initiate session object s
    s = requests.Session()

    # use method get to request the page data from the api
    # store the results in the variable r
    # cookie is imported from settings.py
    r = s.get(url, headers=({'Content-Type':'application/json'}), cookies=cookie)

    r_dictionary = json.loads(r.text)

    if 'message' in r_dictionary.keys():
        raise Exception(r_dictionary['message'])
    
    result = {}

    # type
    type = r_dictionary['type']

    # title
    title = r_dictionary['title']

    # space
    # the dictionary structure of space is space.name and space.key                
    space = r_dictionary['space']['key']

    # body
    # the dictionary structure of body is body.storage.value    
    body = r_dictionary['body']['storage']['value']

    # version
    # the dictionary structure of version is version.number
    version = r_dictionary['version']['number']

    # link
    # the dictionary structure of links is _links.base and _links.webui
    base_url = r_dictionary['_links']['base']

    # the link consists of the base url 'base' and the weblink 'webui'
    weblink = base_url + r_dictionary['_links']['webui']

    ancestors = r_dictionary['children']['page']['results']
    ancestors = [e['id'] for e in ancestors]

    result = {'type': type, 'title': title, 'space': space, 'body': body, 'version': version, 'weblink': weblink, 'ancestors': ancestors}

    return result, id
