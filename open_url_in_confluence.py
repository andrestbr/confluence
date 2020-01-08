import platform
import webbrowser


def open_url_in_confluence(id=None, url=None):

    if not id and not url:
        raise Exception('id or url required')
    
    if id:
        url = 'https://confluence.dw.com/?pageId=' + str(id)
            
    # check if code is running in windows or macos
    if platform.system() == "Windows":
        # open url in standard browser
        webbrowser.open(url)
    else:
        # open url in chrome
        webbrowser.get('chrome').open(url)
