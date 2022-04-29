from pyairtable import Table
from instascrape import Profile
from pyairtable import Table
def run():
    table = getTableReference('appRRypaOL2sWGWy0', 'Stores')
    records = table.all();
    count = 0;
    for store in records:
        if len(store['fields']) != 0:
            if store['fields']['Tienda']:
                try:
                    print(count, store['fields']['Tienda']);
                    if 'description_store' in store['fields'] and (len(store['fields']['description_store']) == 0 or store['fields']['description_store'] == 'Canal oficial de mi música.'):
                        saveInfoStore(store['fields']['Tienda'], store)
                    elif not('description_store' in store['fields']):
                        store['fields']['description_store'] = '';
                        saveInfoStore(store['fields']['Tienda'], store)
                except:
                    print(store['fields']['Tienda'], 'error')
                    continue
        count += 1
    pass

def saveInfoStore(storeName, row):
    profile = getProfile(storeName)
    print(profile['biography']);
    table = getTableReference('appRRypaOL2sWGWy0', 'Stores')
    if profile['biography']:
       table.update(row['id'], {"description_store": profile['biography']})

def getProfile(storeName='@candela.col'):
    try:
        profile = Profile(storeName.replace('@', ''))
        profile.scrape()
        return profile;
    except:
        return {'biography': ''}
    
def getTableReference(baseId = 'appRRypaOL2sWGWy0', tableName = ''):
    return Table('<api-key>', baseId, tableName)
# Punto de entrada de cualquien aplicación de python
if __name__ == "__main__":
    run()