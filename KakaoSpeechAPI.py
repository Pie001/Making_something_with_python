#!/usr/bin/env PYTHONIOENCODING=UTF-8 python3
# -*- coding: utf-8 -*-
# reference : https://www.youtube.com/watch?v=PLAq297bCdw
import requests
import subprocess

url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
headers = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK {rest-api-key}"
}

def make_data(x):
    data = """
    <speak>
    <voice>%s</voice>
    </speak>
    """ % x

    return data.encode("utf-8")

while True:
    cmd = input("말씀하세요 : ")
    data = make_data(cmd)
    r = requests.post(url, data=data, headers=headers)
    with open("audio.mp3", "wb") as f:
        f.write(r.content)
    subprocess.run(["afplay", "audio.mp3"])
