
import os
import dash

from dash import Dash, html

from flask import Flask

from app.utils.app_cards import create_app_card




server=Flask(__name__)

app = Dash(
    __name__,
    server=server,
    use_pages=False,
    url_base_pathname="/",
)


app.title = "Crosslinking App"
app._favicon = "solution.png"

baselink = (
    "crossling/"
    if os.getenv("LOCAL_RUN") == "True"
    else "my_base_link.somerwhere.com/"
)





app_header = html.Header(
    [
        html.A(
            html.Img(
                src="./assets/solution.png",
                alt="Crosslinking App Logo",
                className="app_header_logo",
            ),
            href=f"https://{baselink}",
        ),
        html.Span("Analytic Applications")
    ],
    className="app_header",
)




app.layout = html.Div(
    [
        app_header,
        html.Div(
            [
                create_app_card(
                    app_title="AI Mate",
                    app_icon_filename="ai1.png",
                    app_description="AI Mate is a tool that allows you to upload and analyze your data using machine learning.",
                    app_link=f"https://{baselink}ai_mate",
                ),
                # create_app_card(
                #     app_title="testing the app card",
                #     app_icon_filename="ai1.png",
                #     app_description="a short description.",
                #     app_link="#",
                # ),
            ],
            className="app_card_wrapper",
        )
    ],
    className="app_body",
)


