
from dash import html

def create_app_card(app_title, app_icon_filename, app_description, app_link):

    app_card=html.Div(
        [
            html.Img(
                className="app_card_icon",
                src=f"../assets/{app_icon_filename}",
                alt=f"App Icon {app_title}",
            ),
            html.H2(app_title, className="app_card_title"),
            html.P(app_description, className="app_card_description"),
            html.Div(
                [
                    html.A(
                        [
                            html.Span("Learn"),
                            html.Img(
                                src="./assets/get_started.png",
                                style={"width": "1rem"},
                            )
                        ],
                        href="#",
                        className="app_card_link",
                    ),
                    html.A(
                        [
                            html.Span("Start"),
                            html.Img(
                                src="./assets/finish.png",
                                style={"width": "1rem"},
                            )
                        ],
                        href=app_link,
                        className="app_card_link",
                    )
                ],
                className="app_card_links_wrapper",
            ),
        ],
        className="app_card",
    )

    return app_card




def create_ai_app_card(app_title, app_icon_filename, app_description, app_link):

    app_card=html.Div(
        [
            html.Img(
                className="ai_app_card_icon",
                src=f"../assets/{app_icon_filename}",
                alt=f"App Icon {app_title}",
            ),
            html.H2(app_title, className="ai_app_card_title"),
            html.P(app_description, className="ai_app_card_description"),
            html.Div(
                [
                    html.A(
                        [
                            html.Span("Learn"),
                            html.Img(
                                src="./assets/get_started.png",
                                style={"width": "1rem"},
                            )
                        ],
                        href="#",
                        className="ai_app_card_link",
                    ),
                    html.A(
                        [
                            html.Span("Start"),
                            html.Img(
                                src="./assets/finish.png",
                                style={"width": "1rem"},
                            )
                        ],
                        href=app_link,
                        className="ai_app_card_link",
                    )
                ],
                className="ai_app_card_links_wrapper",
            ),
        ],
        className="ai_app_card",
    )

    return app_card












