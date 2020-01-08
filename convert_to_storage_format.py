from dashboard.confluence.settings import cookie

import json
import requests


'''Convert content from wiki to storage format.

Args:
    wiki (str): content in wiki format

Returns:
    content in storage format

'''


def convert_to_storage_format(wiki_format):

    api_url = 'https://confluence.dw.com/rest/api/contentbody/convert/storage'

    # initiate session object s
    s = requests.Session()

    data = {'value': wiki_format, 'representation':'wiki'}
    data_json = json.dumps(data)


    # use method post to send data to the api
    r = s.post(api_url, data=data_json, headers=({'Content-Type':'application/json'}), cookies=cookie)

    r_dictionary = json.loads(r.text)

    return (r_dictionary['value'])
