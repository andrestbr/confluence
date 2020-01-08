from dashboard.confluence.convert_to_storage_format import convert_to_storage_format


def create_status(content, color, subtle=False):
    '''Create status bar as a structured makro in a confluence page.
    [...]

    Args:
        content(str): text for the status bar
        color(str): color for the status bar
        subtle(boolean): default False, creates a status bar with background color

    Returns:
        status: code for a status object wraped in a <p> tag

    '''
    '''
        structure:
        <p><ac:structured-macro ac:name='status'>
        <ac:parameter ac:name='colour'>Green</ac:parameter>
        <ac:parameter ac:name='title'>aktualisiert: 13.07.2016</ac:parameter>
        <ac:parameter ac:name='subtle'>true</ac:parameter>
        </ac:structured-macro></p>

    '''

    # list of colors available
    colors = ['Grey', 'Red', 'Yellow', 'Green', 'Blue']

    if color not in colors:
        raise Exception ('color not available')

    # convert boolean value (True or False) into a string and sets it to lower case
    subtle_value = str.lower(str(subtle))
    
    # creates a string for the status object as wiki format
    wiki_format = '{status:colour=' + color + '|title=' + content + '|subtle=' + subtle_value + '}'

    storage_format = convert_to_storage_format(wiki_format)
    
    return storage_format


def create_pagetree(reverse=False):
    '''Create a page tree as a structured makro in a confluence page.
    [...]

    Args:
        reverse(boolean): default True, [...]

    Returns:
        pagetree: code for a page tree object wraped in a <p> tag

    '''
    '''
        structure:
        <ac:structured-macro ac:name="pagetree"><ac:parameter ac:name="reverse">false</ac:parameter><ac:parameter ac:name="sort">natural</ac:parameter>
        <ac:parameter ac:name="root"><ac:link>@self</ac:link></ac:parameter><ac:parameter ac:name="startDepth">3</ac:parameter>
        <ac:parameter ac:name="excerpt">false</ac:parameter><ac:parameter ac:name="searchBox">false</ac:parameter><ac:parameter ac:name="expandCollapseAll">false</ac:parameter></ac:structured-macro>


    '''

    # convert boolean value (True or False) into a string and sets it to lower case
    reverse_value = str.lower(str(reverse))
   
    wiki_format = '{pagetree:root=@self|sort=natural|excerpt=false|reverse=' + reverse_value + '|startDepth=3|expandCollapseAll=true|searchBox=false}'
    storage_format = convert_to_storage_format(wiki_format)

    return storage_format

def create_info(content, icon=False):
    '''Create an info box as a structured makro in a confluence page.
    [...]

    Args:
        content(str): content for the info box
        icon(Boolean): show symbol for icon. Default False

    Returns:
        infobox: code for an info box object wraped in a <p> tag

    '''
    icon_value = str.lower(str(icon))
    wiki_format = '{info:icon=' + icon_value + '}*' + content + '*{info}'
    storage_format = convert_to_storage_format(wiki_format)

    return storage_format


