import colorama
import dash
import requests
from dash import html, Dash, dcc
from dash.dependencies import Output, Input, State
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import dcc
from dash_iconify import DashIconify
from flask import Flask, render_template, request, make_response

server = Flask(__name__)

app = Dash(
    __name__,
    assets_url_path="assets",
    # transforms=[MultiplexerTransform()],
    external_stylesheets=[
        "https://use.fontawesome.com/releases/v6.2.1/css/all.css",
        dbc.themes.SKETCHY,
    ],
    external_scripts=[
    ],
    # plugins=[dash_labs.plugins.pages],
    use_pages=True,
    server=server,
    # prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
)


side_bar_u = html.Div(
    [
        dbc.Button(
            dmc.Burger(
                id="burger-button",
                opened=False,
            ),
            style={"height": "80%"},
            color="secondary",
            outline=True,
        ),
        html.Div(id="burger-state"),
    ]
)

navbar = html.Div(
    dmc.Grid(
        [
            dmc.Col(span=1),
            dmc.Col(
                [
                    dmc.Menu(
                        [
                            dmc.MenuTarget(
                                dmc.Button(
                                    dmc.Avatar(
                                        src=dash.get_asset_url(
                                            "branding/Schiff-Animation.gif"
                                        ),
                                    ),
                                    variant="subtle",
                                    size="lg",
                                )
                            ),
                            dmc.MenuDropdown(
                                children=[
                                    dmc.MenuLabel("Account Logged In"),
                                    # MenuItem is being called to open login modal
                                    dmc.MenuItem(
                                        "Login",
                                        id="login-modal-button",
                                        icon=DashIconify(icon="mdi:user-lock"),
                                    ),
                                    dmc.MenuItem(
                                        "Register",
                                        href="/register_user",
                                        icon=DashIconify(
                                            icon="simple-icons:theregister"
                                        ),
                                    ),
                                    dmc.MenuDivider(),
                                    dmc.MenuItem(href="/about", children=["About"]),
                                    # account-menu-dropdown is being called to change the above to a logged in vs logged out state
                                ],
                                id="render-navbar-based-on-logged-in-status",
                            ),
                        ],
                        trigger="hover",
                    )
                ],
                span=1,
            ),
            dmc.Col(
                html.Center(
                    html.A(
                        href="/",
                        children=[
                            dmc.Space(h=3),
                            html.H2(
                                "Pip - Dash Frontend Components",
                            ),
                        ],
                    )
                ),
                span=8,
            ),
            dmc.Col(
                children=[
                    side_bar_u,
                ],
                ml="auto",
                span=1,
            ),
            dmc.Col(span=1),
        ],
        gutter="sm",
    ),
    id="dynamic-navbar",
    style={"z-index": "26", 'background': 'linear-gradient(to bottom, #ecf0f1 0%, #515960 100%)'},
)


login_form = dbc.Form(
    [
        dbc.Col(
            [
                dmc.Stack(
                    children=[
                        dmc.TextInput(
                            label="Your Username or Email:",
                            style={"width": "100%"},
                            id="login-username",
                        ),
                    ],
                )
            ]
        ),
        dbc.Col(
            [
                dmc.PasswordInput(
                    label="Your password:",
                    style={"width": "100%"},
                    placeholder="Your password",
                    icon=DashIconify(icon="bi:shield-lock"),
                    id="login-password",
                )
            ]
        ),
    ],
    className="mb-5",
)


# Create the layout for the login screen
login_modal = dmc.Card(
    children=[
        dmc.CardSection(
            dmc.Image(
                src=dash.get_asset_url("branding/banner_login.png"),
                height=180,
            )
        ),
        dmc.Group(
            [
                dmc.Text("Access Account", weight=500),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        login_form,
        dmc.Button(
            "Login",
            variant="light",
            color="blue",
            fullWidth=True,
            mt="md",
            radius="md",
            id="login-button",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
    id="login-modal-form",
)


login_to_account = dmc.Modal(
    children=[
        # html.Div(id="User-Avatar"),
        login_modal,
    ],
    id="login-account-modal",
    overflow="outside",
    opened=False,
    size="sm",
)

app.layout = html.Div(
    [
        login_to_account,
        navbar,
        dash.page_container,
        dcc.Location(id="url", refresh=True),
    ],
    style={"height": "100vh"},
)


@app.callback(Output("dynamic-navbar", "children"), [Input('auth-store', 'data')])
def dynamic_navbar(data):
    if data:
        return dmc.Grid(
            [
                dmc.Col(span=1),
                dmc.Col(
                    [
                        dmc.Menu(
                            [
                                dmc.MenuTarget(
                                    dmc.Button(
                                        dmc.Avatar(
                                            src=dash.get_asset_url(
                                                "branding/Schiff-Animation.gif"
                                            ),
                                        ),
                                        variant="subtle",
                                        size="lg",
                                    )
                                ),
                                dmc.MenuDropdown(
                                    children=[
                                        dmc.MenuLabel("Account Logged In"),
                                        # MenuItem is being called to open login modal
                                        # dmc.MenuItem(
                                        #     "Login",
                                        #     id="login-modal-button",
                                        #     icon=DashIconify(icon="mdi:user-lock"),
                                        # ),
                                        dmc.MenuItem(
                                            html.A(
                                                href="/profile",
                                                children=["Profile"],
                                            ),
                                            icon=DashIconify(
                                                icon="icon-park:avatar"
                                            ),
                                        ),
                                        dmc.MenuDivider(),
                                        dmc.MenuItem(
                                            html.A(
                                                href="/about", children=["About"]
                                            )
                                        ),
                                        # account-menu-dropdown is being called to change the above to a logged in vs logged out state
                                    ],
                                    id="render-navbar-based-on-logged-in-status",
                                ),
                            ],
                            trigger="hover",
                        )
                    ],
                    span=1,
                ),
                dmc.Col(
                    html.Center(
                        html.A(
                            href="/",
                            children=[
                                dmc.Space(h=3),
                                html.H2(
                                    "Maply.io",
                                ),
                            ],
                        )
                    ),
                    span=8,
                ),
                dmc.Col(
                    children=[
                        side_bar_u,
                    ],
                    ml="auto",
                    span=1,
                ),
                dmc.Col(span=1),
            ],
            gutter="sm",
        )
    else:
        return dmc.Grid(
            [
                dmc.Col(span=1),
                dmc.Col(
                    [
                        dmc.Menu(
                            [
                                dmc.MenuTarget(
                                    dmc.Button(
                                        dmc.Avatar(
                                            src=dash.get_asset_url(
                                                "branding/Schiff-Animation.gif"
                                            ),
                                        ),
                                        variant="subtle",
                                        size="lg",
                                    )
                                ),
                                dmc.MenuDropdown(
                                    children=[
                                        dmc.MenuLabel("Account Logged In"),
                                        # MenuItem is being called to open login modal
                                        dmc.MenuItem(
                                            "Login",
                                            id="login-modal-button",
                                            icon=DashIconify(icon="mdi:user-lock"),
                                        ),
                                        dmc.MenuItem(
                                            "Register",
                                            href="/register_user",
                                            icon=DashIconify(
                                                icon="simple-icons:theregister"
                                            ),
                                        ),
                                        dmc.MenuDivider(),
                                        dmc.MenuItem(
                                            href="/about", children=["About"]
                                        ),
                                        # account-menu-dropdown is being called to change the above to a logged in vs logged out state
                                    ],
                                    id="render-navbar-based-on-logged-in-status",
                                ),
                            ],
                            trigger="hover",
                        )
                    ],
                    span=1,
                ),
                dmc.Col(
                    html.Center(
                        html.A(
                            href="/",
                            children=[
                                dmc.Space(h=3),
                                html.H2(
                                    "Maply.io",
                                ),
                            ],
                        )
                    ),
                    span=8,
                ),
                dmc.Col(
                    children=[
                        side_bar_u,
                    ],
                    ml="auto",
                    span=1,
                ),
                dmc.Col(span=1),
            ],
            style={"z-index": "26"},
            gutter="sm",
        )


# Burger modal for lower navigation
@app.callback(Output("burger-state", "children"), Input("burger-button", "opened"))
def open(b_opened):
    if b_opened:
        return dmc.Footer(
            height=60,
            fixed=True,
            children=[
                dmc.Group(
                    [
                        # html.A(
                        #     href="/upgrade_boat",
                        #     children=[
                        #         html.Center(
                        #             DashIconify(icon="game-icons:armor-upgrade", width=45)
                        #         )
                        #     ],
                        # ),
                        # dmc.Button(
                        #     id="post-location-modal-button",
                        #     children=[
                        #         html.Center(
                        #             DashIconify(
                        #                 icon="logos:shipit", width=45
                        #             )
                        #         )
                        #     ],
                        #     variant="subtle",
                        # ),
                        html.A(
                            href="/trade_route",
                            children=[
                                dmc.ActionIcon(
                                    DashIconify(icon="openmoji:location-indicator-red", width=50),
                                    size=55,
                                    variant="transparent",
                                )
                            ],
                        ),

                        html.A(
                            href="/updates",
                            children=[
                                html.Center(
                                    DashIconify(icon="noto:globe-showing-americas", width=45)
                                )
                            ],
                        ),
                    ],
                    position="center",
                ),
            ],
            style={'background': 'linear-gradient(to bottom, #515960 0%, #ecf0f1 100%)'
},
        )
    else:
        pass


@app.callback(
    Output("login-account-modal", "opened"),
    Input("login-modal-button", "n_clicks"),
    State("login-account-modal", "opened"),
    prevent_initial_call=True,
)
def toggle_register_modal(n_clicks, opened):
    if n_clicks:
        return not opened


if __name__ == "__main__":
    app.run_server(
        debug=True,
        port=8319,
        threaded=True,
    )