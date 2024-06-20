import json

import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottiefile("./animations/animation.json")  # replace link to local lottie file
# lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")

st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",  # medium ; high
    renderer="svg",  # canvas
    height=None,
    width=None,
    key=None,
)
