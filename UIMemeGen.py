from tkinter import ttk
from tkinter import *
import requests
import urllib
import webbrowser
from ttkbootstrap import Style

urlBMC = 'https://www.buymeacoffee.com/jesusartz/'


root = Tk()
estilo = Style(theme='cosmo')
ventana = estilo.master
root.title("Meme Generator - By: Jesus Artz")
root.geometry("500x350")
Label(root, text="MemeGen").pack(pady=5)

def BuyMeaCoffee():
    webbrowser.open_new_tab(urlBMC)

username = ""
password = ""

selection = 0
texto0 = ""
texto1 = ""

def Main(pwrd, usr, t0, t1):
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    url = "https://api.imgflip.com/get_memes"

    get = requests.get(url).json()['data']['memes']

    images = [{'name': data['name'], 'url': data['url'], 'id': data['id']} for data in get]


    ctr = 1
    for i in images:
        print(ctr, i['name'])
        ctr = ctr + 1

    URL = 'https://api.imgflip.com/caption_image'
    params = {
        'username': usr,
        'password': pwrd,
        'template_id': images[int(selection.get()) - 1]['id'],
        'text0': t0,
        'text1': t1,
    }

    response = requests.request('POST', URL, params=params).json()

    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', useragent)
    filename, headers = opener.retrieve(response['data']['url'], images[id - 1]['name'] + '.jpg')



UserName = Entry(root, textvariable=username)
UserName.place(x=130, y=70)
LUSR = Label(root, text="Username")
LUSR.place(x=30, y=70)
Password = Entry(root, textvariable=password)
Password.place(x=130, y=100)
LPWD = Label(root, text="Password")
LPWD.place(x=30, y=100)

selection = Entry(root, textvariable=selection)
selection.place(x=200, y=170)
Lselect = Label(root, text="Ingresa el numero del meme")
Lselect.place(x=30, y=170)



Text0 = Entry(root, textvariable=texto0)
Text0.place(x=130, y=200)
LTexto0 = Label(root, text="Texto 1")
LTexto0.place(x=30, y=200)
Text1 = Entry(root, textvariable=texto1)
Text1.place(x=130, y=230)
LTexto1 = Label(root, text="Texto 2")
LTexto1.place(x=30, y=230)


botonStart = Button(text="Generate Meme", command=lambda:Main(password, username, texto0, texto1))
botonStart.place(x=205, y=300)

root.mainloop()