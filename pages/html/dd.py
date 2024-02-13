from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc

# Base dd Navbar
dd_navbar = dmc.MantineProvider(
    theme={"colorScheme": "dark"},
    children=[
        dmc.Paper(
            [
                dmc.Space(h=10),
                dmc.Group(
                    [
                        dmc.Tooltip(
                            label="Simulator",
                            position="bottom",
                            offset=3,
                            children=[
                                dmc.ActionIcon(
                                    DashIconify(
                                        icon="logos:python",
                                        width=30,
                                    ),
                                    variant="transparent",
                                    id="card_dd_simulator",
                                    n_clicks=1,
                                )
                            ],
                        ),
                        dmc.Tooltip(
                            label="Showcase",
                            position="bottom",
                            offset=3,
                            children=[
                                dmc.ActionIcon(
                                    DashIconify(
                                        icon="streamline-emojis:open-book",
                                        width=30,
                                    ),
                                    variant="transparent",
                                    id="card_dd_showcase",
                                    n_clicks=1,
                                ),
                            ],
                        ),
                        dmc.Tooltip(
                            label="Example Code",
                            position="bottom",
                            offset=3,
                            children=[
                                dmc.ActionIcon(
                                    DashIconify(
                                        icon="vscode-icons:folder-type-python-opened",
                                        width=30,
                                    ),
                                    color="gray",
                                    n_clicks=1,
                                    variant="transparent",
                                    id="card_dd_simulator_code",
                                ),
                            ],
                        ),
                        dmc.Tooltip(
                            label="Attributes",
                            position="bottom",
                            offset=3,
                            children=[
                                dmc.ActionIcon(
                                    DashIconify(
                                        icon="vscode-icons:file-type-poedit",
                                        width=30,
                                    ),
                                    variant="transparent",
                                    n_clicks=1,
                                    id="card_dd_attributes",
                                ),
                            ],
                        ),
                    ],
                    position="center",
                ),
                html.Hr(),
            ],
            style={"margin": 0, "padding": 0},
        )
    ],
)

dd_simulator_navbar = html.Div(
    # dd Simulator
    dmc.MantineProvider(
        theme={"colorScheme": "dark"},
        children=[
            dmc.Paper(
                [
                    dmc.Space(h=10),
                    dmc.Group(
                        [
                            dmc.Tooltip(
                                label="Simulator",
                                position="bottom",
                                offset=3,
                                children=[
                                    dmc.ActionIcon(
                                        DashIconify(
                                            icon="logos:python",
                                            width=30,
                                        ),
                                        variant="transparent",
                                        id="card_dd_simulator",
                                        n_clicks=1,
                                    )
                                ],
                            ),
                            dmc.Tooltip(
                                label="Showcase",
                                position="bottom",
                                offset=3,
                                children=[
                                    dmc.ActionIcon(
                                        DashIconify(
                                            icon="streamline-emojis:open-book",
                                            width=30,
                                        ),
                                        color="blue",
                                        variant="transparent",
                                        id="card_dd_showcase",
                                        n_clicks=1,
                                    ),
                                ],
                            ),
                            dmc.Tooltip(
                                label="Example Code",
                                position="bottom",
                                offset=3,
                                children=[
                                    dmc.ActionIcon(
                                        DashIconify(
                                            icon="vscode-icons:folder-type-python-opened",
                                            width=30,
                                        ),
                                        color="blue",
                                        variant="transparent",
                                        id="card_dd_simulator_code",
                                        n_clicks=1,
                                    ),
                                ],
                            ),
                            dmc.Tooltip(
                                label="Attributes",
                                position="bottom",
                                offset=3,
                                children=[
                                    dmc.ActionIcon(
                                        DashIconify(
                                            icon="vscode-icons:file-type-poedit",
                                            width=30,
                                        ),
                                        variant="transparent",
                                        id="card_dd_attributes",
                                        n_clicks=1,
                                    ),
                                ],
                            ),
                        ],
                        position="center",
                    ),
                    html.Hr(),
                    html.Div(
                        [
                            dmc.Container(
                                [
                                    dmc.Title("Custom html.Dd() Simulator", order=2),
                                    html.Div(
                                        [
                                            html.Label(
                                                "The dash.html.Dd() component is used to create hyperlinks. Here are some examples:",
                                                style={
                                                    "font-size": "14px",
                                                    "font-family": '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji"',
                                                },
                                            ),
                                            # Example of a simple link
                                            html.A(
                                                "A Tag Homepage #",
                                                href="#",
                                                target="_blank",
                                            ),
                                            # Adding some spacing
                                            html.Br(),
                                            html.Br(),
                                            # Example of a link with additional attributes
                                            html.A(
                                                children="Go to Google",
                                                href="https://google.com",
                                                target="_blank",
                                                style={
                                                    "color": "red",
                                                    "textDecoration": "none",
                                                },
                                            ),
                                            # Adding some spacing
                                            html.Br(),
                                            html.Br(),
                                            # Example of nesting other components within an A component
                                            html.A(
                                                children=[
                                                    html.Button(
                                                        "Click Me",
                                                        style={
                                                            "border": "none",
                                                            "padding": "10px",
                                                            "borderRadius": "5px",
                                                            "backgroundColor": "lightblue",
                                                        },
                                                    )
                                                ],
                                                href="https://example.com",
                                                target="_blank",
                                            ),
                                        ]
                                    ),
                                ]
                            )
                        ],
                        style={"padding": "20px"},
                    ),
                ]
            ),
        ],
    ),
    id="card_display_dd",
)

dd_showcase = html.Div(
    [
        dd_navbar,
        html.Div(
            [
                html.Div(
                    [
                        dmc.Prism(
                            """from dash import html

html.A("A Tag Homepage #",
          href="#",
          target="_blank")""",
                            language="python",
                            colorScheme="dark",
                        ),
                    ],
                    style={
                        "margin": 0,
                        "padding": 0,
                        "position": "relative",
                        "top": -20,
                    },
                ),
                html.Div(
                    html.Center(html.A("A Tag Homepage #", href="#", target="_blank")),
                    style={
                        "margin": 0,
                        "padding": 0,
                        "position": "relative",
                        "top": -20,
                    },
                ),
                html.Div(
                    dmc.MantineProvider(
                        theme={"colorScheme": "dark"},
                        children=[
                            dmc.Paper(
                                dbc.Container(
                                    [
                                        html.H1("Understanding the HTML <a> Element"),
                                        html.P(
                                            [
                                                "The ",
                                                html.Code("<a>"),
                                                " HTML element (or anchor element), with its ",
                                                html.Code("href"),
                                                " attribute, creates a hyperlink to web pages, files, email addresses, locations in the same page, or anything else a URL can address.",
                                            ]
                                        ),
                                        html.P(
                                            [
                                                "Content within each ",
                                                html.Code("<a>"),
                                                " should indicate the link's destination. If the ",
                                                html.Code("href"),
                                                " attribute is present, pressing the enter key while focused on the ",
                                                html.Code("<a>"),
                                                " element will activate it.",
                                            ]
                                        ),
                                    ]
                                )
                            )
                        ],
                    ),
                    style={
                        "margin": 0,
                        "padding": 0,
                        "position": "relative",
                        "top": -20,
                    },
                ),
            ],
            style={
                "position": "relative",
                "top": -20,
                "height": "60vh",
                "overflow-y": "scroll",
            },
        ),
    ],
    style={"margin": 0, "padding": 0},
    id="card_display_dd",
)

dd_example_code = html.Div(
    [
        dmc.Prism(
            """# Dash html.A() Simulator
from dash import Dash, html, dcc, callback, Input, Output, State

html.Div([
dmc.Container([
dmc.Title("Custom html.A() Simulator",
         order=2),
html.Div([
   html.Label(
       "The dash.html.A() component is used to create hyperlinks. Here are some examples:", style={'font-size': '14px', "font-family": '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji"'}),

   # Example of a simple link
   html.A("A Tag Homepage #",
          href="#",
          target="_blank"),

   # Adding some spacing
   html.Br(), html.Br(),

   # Example of a link with additional attributes
   html.A(
       children="Go to Google",
       href="https://google.com",
       target="_blank",
       style={'color': 'red',
              'textDecoration': 'none'}
   ),

   # Adding some spacing
   html.Br(), html.Br(),

   # Example of nesting other components within an A component
   html.A(
       children=[
           html.Button('Click Me',
                       style={
                           'border': 'none',
                           'padding': '10px',
                           'borderRadius': '5px',
                           'backgroundColor': 'lightblue'})],
       href="https://example.com",
       target="_blank"
   )
])

])
], style={"padding": "20px"})
""",
            language="python",
            colorScheme="dark",
        ),
    ],
    style={
        "margin": 0,
        "padding": 0,
        "position": "relative",
        "top": -20,
        "height": "60vh",
        "overflow-y": "scroll",
    },
)

dd_attributes = html.Div(
    [
        dmc.Prism(
            """
Attributes
This element's attributes include the global attributes.

'download'
/* Causes the browser to treat the linked URL as a download. Can be used with or without a filename value: */ 

/* Without a value, the browser will suggest a filename/extension, generated from various sources:
- The Content-Disposition HTTP header
- The final segment in the URL path
- The media type (from the Content-Type header, the start of a data: URL, or Blob.type for a blob: URL)
filename: defining a value suggests it as the filename.
/ and \ characters are converted to underscores (_). 
Filesystems may forbid other characters in filenames,
so browsers will adjust the suggested name if necessary. */ 

'href':'url'
/* The URL that the hyperlink points to. 
Links are not restricted to HTTP-based URLs — they can use any URL scheme supported by browsers: 
- Sections of a page with document fragments
- Specific text portions with text fragments
- Pieces of media files with media fragments
- Telephone numbers with tel: URLs
- Email addresses with mailto: URLs
- SMS text messages with sms: URLs
While web browsers may not support other URL schemes, websites can with registerProtocolHandler() */ 

'hreflang':'english'
/* Hints at the human language of the linked URL.
No built-in functionality. 
Allowed values are the same as the global lang attribute. */ 

'ping':[]
/* A space-separated list of URLs. 
When the link is followed, the browser will send POST requests with the body PING to the URLs.
Typically for tracking. */

'referrerpolicy'
/* How much of the referrer to send when following the link.

- no-referrer: The Referer header will not be sent.
- no-referrer-when-downgrade: The Referer header will not be sent to origins without TLS (HTTPS).
- origin: The sent referrer will be limited to the origin of the referring page: its scheme, host, and port.
- origin-when-cross-origin: The referrer sent to other origins will be limited to the scheme, the host, and the port. 
Navigations on the same origin will still include the path.
- same-origin: A referrer will be sent for same origin, but cross-origin requests will contain no referrer information.
- strict-origin: Only send the origin of the document as the referrer when the protocol security level stays the same
(HTTPS→HTTPS), but don't send it to a less secure destination (HTTPS→HTTP).
- strict-origin-when-cross-origin (default): Send a full URL when performing a same-origin request,
only send the origin when the protocol security level stays the same (HTTPS→HTTPS),
and send no header to a less secure destination (HTTPS→HTTP).
- unsafe-url: The referrer will include the origin and the path (but not the fragment, password, or username).
This value is unsafe, because it leaks origins and paths from TLS-protected resources to insecure origins. */ 

'rel'
/* The relationship of the linked URL as space-separated link types. */ 

'target'
/* Where to display the linked URL, as the name for a browsing context (a tab, window, or <iframe>).
The following keywords have special meanings for where to load the URL:

_self: the current browsing context. (Default)
_blank: usually a new tab, but users can configure browsers to open a new window instead.
_parent: the parent browsing context of the current one. If no parent, behaves as _self.
_top: the topmost browsing context (the "highest" context that's an ancestor of the current one).
If no ancestors, behaves as _self. */ 

'type'
/* Hints at the linked URL's format with a MIME type. No built-in functionality. */
""",
            language="css",
            colorScheme="dark",
        ),
    ],
    style={
        "margin": 0,
        "padding": 0,
        "position": "relative",
        "top": -20,
        "height": "60vh",
        "overflow-y": "scroll",
    },
)
