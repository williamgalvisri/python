from selenium.webdriver import Chrome 
from instascrape import *
from pyairtable import Table


def run():
    table = getTableReference('appRRypaOL2sWGWy0', 'Stores')
    records = table.all();
    count = 0;
    for store in records:
        # if count <= 3:
        print(count)
        if len(store['fields']) != 0:
            if store['fields']['Tienda']: 
                try:
                    if 'description' in store['fields'] and len(store['fields']['description']) == 0:
                        saveInfoStore(store['fields']['Tienda'], store)
                    elif not 'description' in store['fields']:
                        store['fields']['description'] = '';
                        saveInfoStore(store['fields']['Tienda'], store)
                except:
                    print(store['fields']['Tienda'], 'error')
                    continue
        count += 1
    
    pass

def saveInfoStore(storeName, row):
    print(storeName)
    # Instantiate the scraper objects 
    profile = Profile(storeName.replace('@', ''))
    profile.scrape()

    recents = profile.get_recent_posts();
    chris_photos = [post for post in recents if not post.is_video]
    table = getTableReference('appRRypaOL2sWGWy0', 'Stores')

    # Concat all description from post's
    description = ''
    for post in chris_photos: 
        if len(post.source['edge_media_to_caption']['edges']) > 0:
            description += post.source['edge_media_to_caption']['edges'][0]['node']['text']
        elif len(post.source['edge_media_to_caption']['edges']) == 0:
            description = '';
    table.update(row['id'], {"description": description})

def getTableReference(baseId = 'appRRypaOL2sWGWy0', tableName = ''):
    return Table('key5RmxjCDpFu5xUy', baseId, tableName)
# Punto de entrada de cualquien aplicación de python
if __name__ == "__main__":
    run()