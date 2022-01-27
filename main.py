import requests
import urllib

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
url = "https://api.imgflip.com/get_memes"

usr = 'YourUsername'
pwrd = 'YourPassword'

get = requests.get(url).json()['data']['memes']

images=[{'name':data['name'], 'url':data['url'], 'id':data['id']} for data in get]

def verLista():
    ctr = 1
    for i in images:
        print(ctr, i['name'])
        ctr = ctr + 1

verLista()

id = int(input("Ingresa el numero del meme que quieres editar: "))
text0 = input("Ingresa el primer texto: ")
text1 = input("Ingresa el segundo texto: ")
text2 = input("Ingresa el tercer texto: ")


URL = 'https://api.imgflip.com/caption_image'
params = {
    'username':usr,
    'password':pwrd,
    'template_id':images[id-1]['id'],
    'text0':text0,
    'text1':text1,
    'text2':text2
}

response = requests.request('POST', URL, params=params).json()


opener = urllib.request.URLopener()
opener.addheader('User-Agent', useragent)
filename, headers = opener.retrieve(response['data']['url'], images[id-1]['name']+'.jpg')
