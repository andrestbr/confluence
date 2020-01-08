import requests
import json

from dashboard.confluence.settings import cookie

'''Delete a page in confluence.

Args:
    id: integer with the id value from page to be deleted

Returns:
    False and text from the api response
    True and text with api response

'''


def delete_page(id):

    api_url = 'https://confluence.dw.com/rest/api/content/'

    url = api_url + str(id)

    # initiate session object s
    s = requests.Session()

    # use method post to send data to the api
    r = s.delete(url, cookies=cookie)

    if not r.text:
        return True, id
    else:
        r_dictionary = json.loads(r.text)
        return False, r_dictionary['message']
