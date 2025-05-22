import reflex as rx

from rxconfig import config

class State(rx.State):
    ...

def memes() -> rx.Component:
    return rx.box("Hi")

