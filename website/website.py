import reflex as rx
from website.memes import memes
from rxconfig import config


class State(rx.State):
    ...


def index() -> rx.Component:
    return rx.container(
        rx.box(
            rx.heading("Awoo!", size="7"),
            rx.heading("I'm Wolfiii🐺", size="5"),
            rx.grid(
                rx.card(
                    rx.heading("Memes", size="3"),
                    on_click=rx.redirect("/memes"),
                    cursor="pointer",
                    style={
                        "transition": "all 0.2s",
                        ":hover": {
                            "boxShadow": "0 0 0 4px #3182ce55",
                            "transform": "scale(1.03)",
                        }
                    }
                ),
                spacing="4",
                columns="6",
                width="100%",
            ),
            background_color="rgba(50,50,50,0.5)",
            padding="1rem",
            border_radius="0.5rem",
        ),
        background="center/cover url('/image.jpg')",
        height="100vh",
        backdrop_filter="blur(15px)",
    )


app = rx.App()
app.add_page(index, title="Home", description="Wolfiii's Web")
app.add_page(memes, title="Memes", description="Wolfiii's Memes")