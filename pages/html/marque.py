from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify

# Base Navbar
marque_navbar = dmc.MantineProvider(
        theme={"colorScheme": "dark"},
        children=[dmc.Paper([
            dmc.Space(h=10),
            dmc.Group([
                dmc.Tooltip(
                    label="Simulator",
                    position="bottom",
                    offset=3,
                    children=[dmc.ActionIcon(
                        DashIconify(icon="logos:python", width=30, ), variant='transparent',
                        id='card_marque_simulator', n_clicks=1,
                    )]
                ),
                dmc.Tooltip(
                    label="Showcase",
                    position="bottom",
                    offset=3,
                    children=[
                        dmc.ActionIcon(
                            DashIconify(icon="streamline-emojis:open-book", width=30, ),
                            variant='transparent', id='card_marque_showcase', n_clicks=1,
                        ),
                    ]),
                dmc.Tooltip(
                    label="Example Code",
                    position="bottom",
                    offset=3,
                    children=[
                        dmc.ActionIcon(
                            DashIconify(icon="vscode-icons:folder-type-python-opened", width=30, ), color="gray",
                            n_clicks=1,
                            variant='transparent', id='card_marque_simulator_code'
                        ),
                    ]),
                dmc.Tooltip(
                    label="Attributes",
                    position="bottom",
                    offset=3,
                    children=[
                        dmc.ActionIcon(
                            DashIconify(icon="vscode-icons:file-type-poedit", width=30, ), variant='transparent',
                            n_clicks=1,
                            id='card_marque_attributes'
                        ),
                    ])
            ], position='center'),
            html.Hr(),
        ], style={'margin': 0,
                  'padding': 0})])



marque_simulator_navbar = html.Div(dmc.MantineProvider(
    theme={"colorScheme": "dark"},
    children=[dmc.Paper([
        dmc.Space(h=10),
        dmc.Group([
            dmc.Tooltip(
                label="Simulator",
                position="bottom",
                offset=3,
                children=[dmc.ActionIcon(
                    DashIconify(icon="logos:python", width=30, ), variant='transparent',
                    id='card_marque_simulator', n_clicks=1,
                )]
            ),
            dmc.Tooltip(
                label="Showcase",
                position="bottom",
                offset=3,
                children=[
                    dmc.ActionIcon(
                        DashIconify(icon="streamline-emojis:open-book", width=30, ), color="blue",
                        variant='transparent', id='card_marque_showcase', n_clicks=1,
                    ),
                ]),
            dmc.Tooltip(
                label="Example Code",
                position="bottom",
                offset=3,
                children=[
                    dmc.ActionIcon(
                        DashIconify(icon="vscode-icons:folder-type-python-opened", width=30, ), color="blue",
                        variant='transparent', id='card_marque_simulator_code', n_clicks=1,
                    ),
                ]),
            dmc.Tooltip(
                label="Attributes",
                position="bottom",
                offset=3,
                children=[
                    dmc.ActionIcon(
                        DashIconify(icon="vscode-icons:file-type-poedit", width=30, ), variant='transparent',
                        id='card_marque_attributes', n_clicks=1,
                    ),
                ])
        ], position='center'),
        html.Hr(),
        html.Div([
            dmc.Container([
                dmc.Title("Custom html.Marquee() Simulator",
                          order=2),
                dmc.Select(label="Direction",
                           placeholder="Select direction",
                           data=[
                               {"value": "left",
                                "label": "Left"},
                               {"value": "right",
                                "label": "Right"},
                               {"value": "up",
                                "label": "Up"},
                               {"value": "down",
                                "label": "Down"},
                           ],
                           id="direction-select"),
                dmc.NumberInput(
                    label="Scroll Amount (px)",
                    value=6, id="scroll-amount"),
                dmc.NumberInput(
                    label="Scroll Delay (ms)",
                    value=85, id="scroll-delay"),
                dmc.Switch(label="True Speed",
                           id="true-speed-switch"),
                dmc.Button("Start", id="start-btn",
                           color="green", style={
                        "marginRight": "10px"}),
                dmc.Button("Stop", id="stop-btn",
                           color="red"),
                html.Div(id="marquee-container",
                         children=[
                             html.Div(
                                 "🌊🌊🌊🌊⛵🌊🌊🌊🌊",
                                 id="marquee-text",
                                 style={
                                     "whiteSpace": "nowrap",
                                     "fontSize": "27px"})
                         ],
                         style={"overflow": "hidden",
                                "whiteSpace": "nowrap",
                                "margin": "20px 0"})
            ],
                style={"maxWidth": 500})
        ], style={"padding": "20px"})
    ])]), id='card_display_marque')

marque_showcase = html.Div([
    dmc.Prism(
        """from dash import html

html.Marquee(html.H1('🌊🌊🌊🌊⛵🌊🌊🌊🌊'),
                style={})""",
        language="python",
        colorScheme="dark",
    ), ],
    style={'margin': 0,
           'padding': 0,
           'position': 'relative',
           'top': -20,
           },
)

marque_example_code = html.Div([
    dmc.Prism(
        """html.Div([
dmc.Container([
   dmc.Title("Custom html.Marquee() Simulator",
             order=2),
   dmc.Select(label="Direction",
              placeholder="Select direction",
              data=[
                  {"value": "left",
                   "label": "Left"},
                  {"value": "right",
                   "label": "Right"},
                  {"value": "up",
                   "label": "Up"},
                  {"value": "down",
                   "label": "Down"},
              ],
              id="direction-select"),
   dmc.NumberInput(
       label="Scroll Amount (px)",
       value=6, id="scroll-amount"),
   dmc.NumberInput(
       label="Scroll Delay (ms)",
       value=85, id="scroll-delay"),
   dmc.Switch(label="True Speed",
              id="true-speed-switch"),
   dmc.Button("Start", id="start-btn",
              color="green", style={
           "marginRight": "10px"}),
   dmc.Button("Stop", id="stop-btn",
              color="red"),
   html.Div(id="marquee-container",
            children=[
                html.Div(
                    "🌊🌊🌊🌊⛵🌊🌊🌊🌊",
                    id="marquee-text",
                    style={
                        "whiteSpace": "nowrap",
                        "fontSize": "27px"})
            ],
            style={"overflow": "hidden",
                   "whiteSpace": "nowrap",
                   "margin": "20px 0"})
], style={"maxWidth": 500})
], style={"padding": "20px"})""",
        language="python",
        colorScheme="dark",
    ), ],
    style={'margin': 0,
           'padding': 0,
           'position': 'relative',
           'top': -20,
           'height': '60vh',
           'overflow-y': 'scroll'
           },
)

marque_attributes = html.Div([
    dmc.Prism(
        """
Styling Attributes                

'behavior':'Deprecated'
/* Sets how the text is scrolled within the marquee. 
Possible values are scroll, slide and alternate. 
If no value is specified, the default value is scroll. */ 

'bgcolor':'Deprecated'
/* Sets the background color through color name or hexadecimal value. */ 

'direction':'Deprecated'
/* Sets the direction of the scrolling within the marquee. 
Possible values are left, right, up and down. 
If no value is specified, the default value is left. */ 

'height':'Deprecated'
/* Sets the height in pixels or percentage value. */ 

'hspace':'Deprecated'
/* Sets the horizontal margin */ 

'loop':'Deprecated'
/* Sets the number of times the marquee will scroll. 
If no value is specified, the default value is −1,
which means the marquee will scroll continuously. */ 

'scrollamount':'Deprecated'
/* Sets the amount of scrolling at each interval in pixels. 
The default value is 6. */ 

'scrolldelay':'Deprecated'
/* Sets the interval between each scroll movement in milliseconds. 
The default value is 85. Note that any value smaller than 60 is ignored,
and the value 60 is used instead unless truespeed is specified. */ 

'truespeed':'Deprecated'
/* By default, scrolldelay values lower than 60 are ignored. 
If truespeed is present, those values are not ignored. */ 

'vspace':'Deprecated'
/* Sets the vertical margin in pixels or percentage value. */ 

'width':'Deprecated'
/* Sets the width in pixels or percentage value. */ 
""",
        language="css",
        colorScheme="dark",
    ), ],
    style={'margin': 0,
           'padding': 0,
           'position': 'relative',
           'top': -20,
           'height': '60vh',
           'overflow-y': 'scroll'
           },
)