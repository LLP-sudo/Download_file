#!/usr/bin/env python

import requests


def download(url):
    get_response = requests.get(url)
    with open("homer.jpg", "wb") as out_file:
        out_file.write(get_response.content)

download("https://abrilveja.files.wordpress.com/2017/12/homer-simpson-1-264a0.jpg?quality=70&strip=info&w=1024")