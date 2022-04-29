from instascrape import *
import requests

def run():
    STORENAME = 'lliancover';
    profile = Profile(STORENAME)
    profile.scrape()
    with open("pic/"+STORENAME+".jpg", 'wb') as handle:
        response = requests.get(profile.profile_pic_url_hd, stream=True)
        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
    pass
# Punto de entrada de cualquien aplicación de python
if __name__ == "__main__":
    run()