from dash import Dash, html
from dash.dependencies import Output, Input, State
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_resizable_panels import PanelGroup, Panel, PanelResizeHandle
import dash
from dash_iconify import DashIconify
from pages.html.a import a_simulator_navbar, a_navbar, a_showcase, a_example_code, a_attributes
from pages.html.marque import marque_navbar, marque_simulator_navbar, marque_showcase, marque_example_code, marque_attributes
from pages.html.address import global_attributes, address_navbar, address_simulator_navbar, address_showcase, address_example_code
from pages.html.abbr import abbr_simulator_navbar, abbr_navbar, abbr_showcase, abbr_example_code

dash.register_page(__name__, path="/")

layout = html.Div([
    dbc.Row([
        dmc.Tabs(
            [
                dmc.TabsList(
                    [
                        dmc.Tab("HTML Components", value="html"),
                        dmc.Tab("Dash Bootstrap Components", value="dbc"),
                        dmc.Tab("Dash Mantine Components", value="dmc"),
                    ]
                ),
                dmc.TabsPanel(html.Div(
                    dbc.Row(
                        [
                            dbc.Col(PanelGroup(
                                            id='panel-group-1',
                                            children=[
                                                Panel(
                                                    id='panel-1',
                                                    children=[
                                                        marque_simulator_navbar,
                                                        dmc.Space(h=10),

                                                    ],
                                                ),
                                                PanelResizeHandle(html.Div(
                                                    style={"backgroundColor": "grey", "height": "100%",
                                                           "width": "5px"})),
                                                Panel(
                                                    id='panel-2',
                                                    children=[a_simulator_navbar],
                                                ),
                                                PanelResizeHandle(html.Div(
                                                    style={"backgroundColor": "grey", "height": "100%",
                                                           "width": "5px"})),
                                                Panel(
                                                    id='panel-3',
                                                    children=[
                                                            abbr_simulator_navbar
                                                        ],
                                                ),
                                                PanelResizeHandle(html.Div(
                                                    style={"backgroundColor": "grey", "height": "100%",
                                                           "width": "5px"})),
                                                Panel(
                                                    id='panel-4',
                                                    children=[address_simulator_navbar],
                                                )

                                            ],
                                            direction='horizontal'
                                        ),sm=12),

                        ]
                    )

                ), value="html"),
                dmc.TabsPanel("Dash bootstrap output", value="dbc"),
                dmc.TabsPanel("dash mantine components", value="dmc"),
            ],
            color="red",
            orientation="outline",
            value='html'
        )
    ])
])

# Card Marquee Simulator
@dash.callback(
    Output("marquee-text", "style"),
    [Input("start-btn", "n_clicks"), Input("stop-btn", "n_clicks")],
    [State("direction-select", "value"),
     State("scroll-amount", "value"),
     State("scroll-delay", "value"),
     State("true-speed-switch", "checked")],
    prevent_initial_call=True
)
def update_marquee_style(start_n_clicks, stop_n_clicks, direction, scroll_amount, scroll_delay, true_speed):
    ctx = dash.callback_context
    if not ctx.triggered or ctx.triggered[0]['prop_id'] == 'stop-btn.n_clicks':
        return {"animation": "none"}

    animation_direction = "normal" if direction in ["left", "up"] else "reverse"
    animation_name = "scrollHorizontal" if direction in ["left", "right"] else "scrollVertical"
    # Ensure true_speed and scroll_delay are respected
    scroll_delay = max(scroll_delay, 60) if true_speed else scroll_delay
    animation_duration = f"{scroll_delay / max(1, scroll_amount)}s"

    return {
        "animation": f"{animation_name} {animation_duration} linear infinite",
        "animationDirection": animation_direction,
        "whiteSpace": "nowrap",
        "fontSize": "27px"
    }

# Card Marquee html.marquee Simulator Code
@dash.callback(
    Output('card_display_marque', 'children'),
    Input('card_marque_simulator', 'n_clicks'),
    Input('card_marque_showcase', 'n_clicks'),
    Input('card_marque_simulator_code', 'n_clicks'),
    Input('card_marque_attributes', 'n_clicks')
)
def return_markque_simulator_code(card_marque_simulator, card_marque_showcase,
                                  card_marque_simulator_code, card_marque_attributes):
    if card_marque_simulator % 2 == 0:
        return marque_simulator_navbar
    elif card_marque_showcase % 2 == 0:
        return html.Div([
            marque_navbar,
            html.Marquee(html.H1('🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊⛵🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊'),
                         style={}),
            marque_showcase
        ], style={'margin': 0,
            'padding': 0}, id='card_display_marque')
    elif card_marque_simulator_code % 2 == 0:
        return html.Div([
            marque_navbar,
            marque_example_code
        ], style={'margin': 0,
            'padding': 0}, id='card_display_marque')
    elif card_marque_attributes % 2 == 0:
        return html.Div([
            marque_navbar,
            marque_attributes
        ], id='card_display_marque')
    else:
        return dash.no_update

# Card A html.A Simulator Code
@dash.callback(
    Output('card_display_a', 'children'),
    Input('card_a_simulator', 'n_clicks'),
    Input('card_a_showcase', 'n_clicks'),
    Input('card_a_simulator_code', 'n_clicks'),
    Input('card_a_attributes', 'n_clicks')
)
def return_a_simulator_code(card_a_simulator, card_a_showcase,
                                  card_a_simulator_code, card_a_attributes):

    if card_a_simulator % 2 == 0:
        return a_simulator_navbar
    elif card_a_showcase % 2 == 0:
        return a_showcase
    elif card_a_simulator_code % 2 == 0:
        return html.Div([
            a_navbar,
            a_example_code
        ], style={'margin': 0,
                  'padding': 0}, id='card_display_a')
    elif card_a_attributes % 2 == 0:
        return html.Div([
            a_navbar,
            a_attributes
        ], id='card_display_a')
    else:
        return dash.no_update

# Card abbr html.Abbr Simulator Code
@dash.callback(
    Output('card_display_abbr', 'children'),
    Input('card_abbr_simulator', 'n_clicks'),
    Input('card_abbr_showcase', 'n_clicks'),
    Input('card_abbr_simulator_code', 'n_clicks'),
    Input('card_abbr_attributes', 'n_clicks')
)
def return_abbr_simulator_code(card_abbr_simulator, card_abbr_showcase,
                            card_abbr_simulator_code, card_abbr_attributes):

    if card_abbr_simulator % 2 == 0:
        return abbr_simulator_navbar
    elif card_abbr_showcase % 2 == 0:
        return html.Div([
            abbr_navbar,
            abbr_showcase
        ], style={'margin': 0,
                  'padding': 0}, id='card_display_abbr')
    elif card_abbr_simulator_code % 2 == 0:
        return html.Div([
            abbr_navbar,
            abbr_example_code
            # example_code
        ], style={'margin': 0,
                  'padding': 0}, id='card_display_abbr')
    elif card_abbr_attributes % 2 == 0:
        return html.Div([
            abbr_navbar,
            global_attributes
        ], id='card_display_abbr')
    else:
        return dash.no_update

# Card address html.Address Simulator Code
@dash.callback(
    Output('card_display_address', 'children'),
    Input('card_address_simulator', 'n_clicks'),
    Input('card_address_showcase', 'n_clicks'),
    Input('card_address_simulator_code', 'n_clicks'),
    Input('card_address_attributes', 'n_clicks')
)
def return_address_simulator_code(card_address_simulator, card_address_showcase,
                            card_address_simulator_code, card_address_attributes):
    if card_address_simulator % 2 == 0:
        return address_simulator_navbar
    elif card_address_showcase % 2 == 0:
        return html.Div([
            address_navbar,
            address_showcase
            # example_code
        ], style={'margin': 0,
                  'padding': 0}, id='card_display_address')
    elif card_address_simulator_code % 2 == 0:
        return html.Div([
            address_navbar,
            address_example_code
            # example_code
        ], style={'margin': 0,
                  'padding': 0}, id='card_display_address')
    elif card_address_attributes % 2 == 0:
        return html.Div([
            address_navbar,
            global_attributes
        ], id='card_display_address')
    else:
        return dash.no_update

# Card area html.Area Simulator Code

# @dash.callback(
#     Output('card_display_area', 'children'),
#     Input('card_area_simulator', 'n_clicks'),
#     Input('card_area_showcase', 'n_clicks'),
#     Input('card_area_simulator_code', 'n_clicks'),
#     Input('card_area_attributes', 'n_clicks')
# )
# def return_area_simulator_code(card_area_simulator, card_area_showcase,
#                             card_area_simulator_code, card_area_attributes):
#     if card_area_simulator % 2 == 0:
#         return area_simulator_navbar
#     elif card_area_showcase % 2 == 0:
#         return html.Div([
#             # area_navbar,
#             # area_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_area')
#     elif card_area_simulator_code % 2 == 0:
#         return html.Div([
#             # area_navbar,
#             # area_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_area')
#     elif card_area_attributes % 2 == 0:
#         return html.Div([
#             # area_navbar,
#             global_attributes
#         ], id='card_display_area')
#     else:
#         return dash.no_update
# # Card article html.Article Simulator Code
# @dash.callback(
#     Output('card_display_article', 'children'),
#     Input('card_article_simulator', 'n_clicks'),
#     Input('card_article_showcase', 'n_clicks'),
#     Input('card_article_simulator_code', 'n_clicks'),
#     Input('card_article_attributes', 'n_clicks')
# )
# def return_article_simulator_code(card_article_simulator, card_article_showcase,
#                             card_article_simulator_code, card_article_attributes):
#     if card_article_simulator % 2 == 0:
#         return article_simulator_navbar
#     elif card_article_showcase % 2 == 0:
#         return html.Div([
#             # article_navbar,
#             # article_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_article')
#     elif card_article_simulator_code % 2 == 0:
#         return html.Div([
#             # article_navbar,
#             # area_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_article')
#     elif card_article_attributes % 2 == 0:
#         return html.Div([
#             # article_navbar,
#             global_attributes
#         ], id='card_display_article')
#     else:
#         return dash.no_update
# # Card aside html.Aside Simulator Code
# @dash.callback(
#     Output('card_display_aside', 'children'),
#     Input('card_aside_simulator', 'n_clicks'),
#     Input('card_aside_showcase', 'n_clicks'),
#     Input('card_aside_simulator_code', 'n_clicks'),
#     Input('card_aside_attributes', 'n_clicks')
# )
# def return_aside_simulator_code(card_aside_simulator, card_aside_showcase,
#                             card_aside_simulator_code, card_aside_attributes):
#     if card_aside_simulator % 2 == 0:
#         return aside_simulator_navbar
#     elif card_aside_showcase % 2 == 0:
#         return html.Div([
#             # aside_navbar,
#             # aside_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_aside')
#     elif card_aside_simulator_code % 2 == 0:
#         return html.Div([
#             # aside_navbar,
#             # aside_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_aside')
#     elif card_aside_attributes % 2 == 0:
#         return html.Div([
#             # aside_navbar,
#             global_attributes
#         ], id='card_display_aside')
#     else:
#         return dash.no_update
# # Card audio html.Audio Simulator Code
# @dash.callback(
#     Output('card_display_audio', 'children'),
#     Input('card_audio_simulator', 'n_clicks'),
#     Input('card_audio_showcase', 'n_clicks'),
#     Input('card_audio_simulator_code', 'n_clicks'),
#     Input('card_audio_attributes', 'n_clicks')
# )
# def return_audio_simulator_code(card_audio_simulator, card_audio_showcase,
#                             card_audio_simulator_code, card_audio_attributes):
#     if card_audio_simulator % 2 == 0:
#         return audio_simulator_navbar
#     elif card_audio_showcase % 2 == 0:
#         return html.Div([
#             # audio_navbar,
#             # audio_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_audio')
#     elif card_audio_simulator_code % 2 == 0:
#         return html.Div([
#             # audio_navbar,
#             # audio_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_audio')
#     elif card_audio_attributes % 2 == 0:
#         return html.Div([
#             # audio_navbar,
#             global_attributes
#         ], id='card_display_audio')
#     else:
#         return dash.no_update
# # Card b html.B Simulator Code
# @dash.callback(
#     Output('card_display_b', 'children'),
#     Input('card_b_simulator', 'n_clicks'),
#     Input('card_b_showcase', 'n_clicks'),
#     Input('card_b_simulator_code', 'n_clicks'),
#     Input('card_b_attributes', 'n_clicks')
# )
# def return_b_simulator_code(card_b_simulator, card_b_showcase,
#                             card_b_simulator_code, card_b_attributes):
#     if card_b_simulator % 2 == 0:
#         return area_b_navbar
#     elif card_b_showcase % 2 == 0:
#         return html.Div([
#             # b_navbar,
#             # b_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_b')
#     elif card_b_simulator_code % 2 == 0:
#         return html.Div([
#             # b_navbar,
#             # b_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_b')
#     elif card_b_attributes % 2 == 0:
#         return html.Div([
#             # b_navbar,
#             global_attributes
#         ], id='card_display_b')
#     else:
#         return dash.no_update
# # Card base html.Base Simulator Code
# @dash.callback(
#     Output('card_display_base', 'children'),
#     Input('card_base_simulator', 'n_clicks'),
#     Input('card_base_showcase', 'n_clicks'),
#     Input('card_base_simulator_code', 'n_clicks'),
#     Input('card_base_attributes', 'n_clicks')
# )
# def return_base_simulator_code(card_base_simulator, card_base_showcase,
#                             card_base_simulator_code, card_base_attributes):
#     if card_base_simulator % 2 == 0:
#         return area_base_navbar
#     elif card_base_showcase % 2 == 0:
#         return html.Div([
#             # b_navbar,
#             # b_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_base')
#     elif card_base_simulator_code % 2 == 0:
#         return html.Div([
#             # base_navbar,
#             # base_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_base')
#     elif card_base_attributes % 2 == 0:
#         return html.Div([
#             # base_navbar,
#             global_attributes
#         ], id='card_display_base')
#     else:
#         return dash.no_update
# # Card bdi html.Bdi Simulator Code
# @dash.callback(
#     Output('card_display_bdi', 'children'),
#     Input('card_bdi_simulator', 'n_clicks'),
#     Input('card_bdi_showcase', 'n_clicks'),
#     Input('card_bdi_simulator_code', 'n_clicks'),
#     Input('card_bdi_attributes', 'n_clicks')
# )
# def return_bdi_simulator_code(card_bdi_simulator, card_bdi_showcase,
#                             card_bdi_simulator_code, card_bdi_attributes):
#     if card_bdi_simulator % 2 == 0:
#         return area_bdi_navbar
#     elif card_bdi_showcase % 2 == 0:
#         return html.Div([
#             # bdi_navbar,
#             # bdi_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_bdi')
#     elif card_bdi_simulator_code % 2 == 0:
#         return html.Div([
#             # bdi_navbar,
#             # bdi_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_bdi')
#     elif card_bdi_attributes % 2 == 0:
#         return html.Div([
#             # bdi_navbar,
#             global_attributes
#         ], id='card_display_bdi')
#     else:
#         return dash.no_update
# # Card bdo html.Bdo Simulator Code
# @dash.callback(
#     Output('card_display_bdo', 'children'),
#     Input('card_bdo_simulator', 'n_clicks'),
#     Input('card_bdo_showcase', 'n_clicks'),
#     Input('card_bdo_simulator_code', 'n_clicks'),
#     Input('card_bdo_attributes', 'n_clicks')
# )
# def return_bdo_simulator_code(card_bdo_simulator, card_bdo_showcase,
#                             card_bdo_simulator_code, card_bdo_attributes):
#     if card_bdo_simulator % 2 == 0:
#         return area_bdo_navbar
#     elif card_bdo_showcase % 2 == 0:
#         return html.Div([
#             # bdo_navbar,
#             # bdo_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_bdo')
#     elif card_bdo_simulator_code % 2 == 0:
#         return html.Div([
#             # bdo_navbar,
#             # bdo_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_bdo')
#     elif card_bdo_attributes % 2 == 0:
#         return html.Div([
#             # bdo_navbar,
#             global_attributes
#         ], id='card_display_bdo')
#     else:
#         return dash.no_update
# # Card big html.Big Simulator Code
# @dash.callback(
#     Output('card_display_big', 'children'),
#     Input('card_big_simulator', 'n_clicks'),
#     Input('card_big_showcase', 'n_clicks'),
#     Input('card_big_simulator_code', 'n_clicks'),
#     Input('card_big_attributes', 'n_clicks')
# )
# def return_big_simulator_code(card_big_simulator, card_big_showcase,
#                             card_big_simulator_code, card_big_attributes):
#     if card_big_simulator % 2 == 0:
#         return area_big_navbar
#     elif card_big_showcase % 2 == 0:
#         return html.Div([
#             # big_navbar,
#             # big_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_big')
#     elif card_big_simulator_code % 2 == 0:
#         return html.Div([
#             # big_navbar,
#             # big_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_big')
#     elif card_big_attributes % 2 == 0:
#         return html.Div([
#             # big_navbar,
#             global_attributes
#         ], id='card_display_big')
#     else:
#         return dash.no_update
# # Card blockquote html.Blockquote Simulator Code
# @dash.callback(
#     Output('card_display_blockquote', 'children'),
#     Input('card_blockquote_simulator', 'n_clicks'),
#     Input('card_blockquote_showcase', 'n_clicks'),
#     Input('card_blockquote_simulator_code', 'n_clicks'),
#     Input('card_blockquote_attributes', 'n_clicks')
# )
# def return_blockquote_simulator_code(card_blockquote_simulator, card_blockquote_showcase,
#                             card_blockquote_simulator_code, card_blockquote_attributes):
#     if card_blockquote_simulator % 2 == 0:
#         return area_blockquote_navbar
#     elif card_blockquote_showcase % 2 == 0:
#         return html.Div([
#             # blockquote_navbar,
#             # blockquote_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_blockquote')
#     elif card_blockquote_simulator_code % 2 == 0:
#         return html.Div([
#             # blockquote_navbar,
#             # blockquote_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_blockquote')
#     elif card_blockquote_attributes % 2 == 0:
#         return html.Div([
#             # blockquote_navbar,
#             global_attributes
#         ], id='card_display_blockquote')
#     else:
#         return dash.no_update
# # Card br html.Br Simulator Code
# @dash.callback(
#     Output('card_display_br', 'children'),
#     Input('card_br_simulator', 'n_clicks'),
#     Input('card_br_showcase', 'n_clicks'),
#     Input('card_br_simulator_code', 'n_clicks'),
#     Input('card_br_attributes', 'n_clicks')
# )
# def return_br_simulator_code(card_br_simulator, card_br_showcase,
#                             card_br_simulator_code, card_br_attributes):
#     if card_br_simulator % 2 == 0:
#         return area_br_navbar
#     elif card_br_showcase % 2 == 0:
#         return html.Div([
#             # br_navbar,
#             # br_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_b')
#     elif card_br_simulator_code % 2 == 0:
#         return html.Div([
#             # br_navbar,
#             # br_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_br')
#     elif card_br_attributes % 2 == 0:
#         return html.Div([
#             # br_navbar,
#             global_attributes
#         ], id='card_display_br')
#     else:
#         return dash.no_update
# # Card button html.Button Simulator Code
# @dash.callback(
#     Output('card_display_button', 'children'),
#     Input('card_button_simulator', 'n_clicks'),
#     Input('card_button_showcase', 'n_clicks'),
#     Input('card_button_simulator_code', 'n_clicks'),
#     Input('card_button_attributes', 'n_clicks')
# )
# def return_b_simulator_code(card_button_simulator, card_button_showcase,
#                             card_button_simulator_code, card_button_attributes):
#     if card_button_simulator % 2 == 0:
#         return area_button_navbar
#     elif card_button_showcase % 2 == 0:
#         return html.Div([
#             # button_navbar,
#             # button_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_button')
#     elif card_button_simulator_code % 2 == 0:
#         return html.Div([
#             # button_navbar,
#             # button_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_button')
#     elif card_button_attributes % 2 == 0:
#         return html.Div([
#             # button_navbar,
#             global_attributes
#         ], id='card_display_button')
#     else:
#         return dash.no_update
# # Card canvas html.Canvas Simulator Code
# @dash.callback(
#     Output('card_display_canvas', 'children'),
#     Input('card_canvas_simulator', 'n_clicks'),
#     Input('card_canvas_showcase', 'n_clicks'),
#     Input('card_canvas_simulator_code', 'n_clicks'),
#     Input('card_canvas_attributes', 'n_clicks')
# )
# def return_canvas_simulator_code(card_canvas_simulator, card_canvas_showcase,
#                             card_canvas_simulator_code, card_canvas_attributes):
#     if card_canvas_simulator % 2 == 0:
#         return area_canvas_navbar
#     elif card_canvas_showcase % 2 == 0:
#         return html.Div([
#             # canvas_navbar,
#             # canvas_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_canvas')
#     elif card_canvas_simulator_code % 2 == 0:
#         return html.Div([
#             # canvas_navbar,
#             # canvas_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_canvas')
#     elif card_canvas_attributes % 2 == 0:
#         return html.Div([
#             # canvas_navbar,
#             global_attributes
#         ], id='card_display_canvas')
#     else:
#         return dash.no_update
# # Card caption html.Caption Simulator Code
# @dash.callback(
#     Output('card_display_caption', 'children'),
#     Input('card_caption_simulator', 'n_clicks'),
#     Input('card_caption_showcase', 'n_clicks'),
#     Input('card_caption_simulator_code', 'n_clicks'),
#     Input('card_caption_attributes', 'n_clicks')
# )
# def return_caption_simulator_code(card_caption_simulator, card_caption_showcase,
#                             card_caption_simulator_code, card_caption_attributes):
#     if card_caption_simulator % 2 == 0:
#         return area_caption_navbar
#     elif card_caption_showcase % 2 == 0:
#         return html.Div([
#             # caption_navbar,
#             # caption_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_caption')
#     elif card_caption_simulator_code % 2 == 0:
#         return html.Div([
#             # caption_navbar,
#             # caption_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_caption')
#     elif card_caption_attributes % 2 == 0:
#         return html.Div([
#             # caption_navbar,
#             global_attributes
#         ], id='card_display_caption')
#     else:
#         return dash.no_update
# # Card center html.Center Simulator Code
# @dash.callback(
#     Output('card_display_center', 'children'),
#     Input('card_center_simulator', 'n_clicks'),
#     Input('card_center_showcase', 'n_clicks'),
#     Input('card_center_simulator_code', 'n_clicks'),
#     Input('card_center_attributes', 'n_clicks')
# )
# def return_center_simulator_code(card_center_simulator, card_center_showcase,
#                             card_center_simulator_code, card_center_attributes):
#     if card_center_simulator % 2 == 0:
#         return area_center_navbar
#     elif card_c_showcase % 2 == 0:
#         return html.Div([
#             # center_navbar,
#             # center_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_center')
#     elif card_center_simulator_code % 2 == 0:
#         return html.Div([
#             # center_navbar,
#             # center_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_center')
#     elif card_center_attributes % 2 == 0:
#         return html.Div([
#             # center_navbar,
#             global_attributes
#         ], id='card_display_center')
#     else:
#         return dash.no_update
# # Card cite html.Cite Simulator Code
# @dash.callback(
#     Output('card_display_cite', 'children'),
#     Input('card_cite_simulator', 'n_clicks'),
#     Input('card_cite_showcase', 'n_clicks'),
#     Input('card_cite_simulator_code', 'n_clicks'),
#     Input('card_cite_attributes', 'n_clicks')
# )
# def return_cite_simulator_code(card_cite_simulator, card_cite_showcase,
#                             card_cite_simulator_code, card_cite_attributes):
#     if card_cite_simulator % 2 == 0:
#         return area_cite_navbar
#     elif card_cite_showcase % 2 == 0:
#         return html.Div([
#             # cite_navbar,
#             # cite_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_cite')
#     elif card_cite_simulator_code % 2 == 0:
#         return html.Div([
#             # cite_navbar,
#             # cite_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_cite')
#     elif card_cite_attributes % 2 == 0:
#         return html.Div([
#             # cite_navbar,
#             global_attributes
#         ], id='card_display_cite')
#     else:
#         return dash.no_update
# # Card code html.Code Simulator Code
# @dash.callback(
#     Output('card_display_code', 'children'),
#     Input('card_code_simulator', 'n_clicks'),
#     Input('card_code_showcase', 'n_clicks'),
#     Input('card_code_simulator_code', 'n_clicks'),
#     Input('card_code_attributes', 'n_clicks')
# )
# def return_code_simulator_code(card_code_simulator, card_code_showcase,
#                             card_code_simulator_code, card_code_attributes):
#     if card_code_simulator % 2 == 0:
#         return area_code_navbar
#     elif card_code_showcase % 2 == 0:
#         return html.Div([
#             # code_navbar,
#             # code_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_code')
#     elif card_code_simulator_code % 2 == 0:
#         return html.Div([
#             # code_navbar,
#             # code_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_code')
#     elif card_code_attributes % 2 == 0:
#         return html.Div([
#             # code_navbar,
#             global_attributes
#         ], id='card_display_code')
#     else:
#         return dash.no_update
# # Card col html.Col Simulator Code
# @dash.callback(
#     Output('card_display_col', 'children'),
#     Input('card_col_simulator', 'n_clicks'),
#     Input('card_col_showcase', 'n_clicks'),
#     Input('card_col_simulator_code', 'n_clicks'),
#     Input('card_col_attributes', 'n_clicks')
# )
# def return_c_simulator_code(card_col_simulator, card_col_showcase,
#                             card_col_simulator_code, card_col_attributes):
#     if card_col_simulator % 2 == 0:
#         return area_col_navbar
#     elif card_col_showcase % 2 == 0:
#         return html.Div([
#             # col_navbar,
#             # col_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_col')
#     elif card_col_simulator_code % 2 == 0:
#         return html.Div([
#             # col_navbar,
#             # col_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_col')
#     elif card_col_attributes % 2 == 0:
#         return html.Div([
#             # col_navbar,
#             global_attributes
#         ], id='card_display_col')
#     else:
#         return dash.no_update
# # Card colgroup html.Colgroup Simulator Code
# @dash.callback(
#     Output('card_display_colgroup', 'children'),
#     Input('card_colgroup_simulator', 'n_clicks'),
#     Input('card_colgroup_showcase', 'n_clicks'),
#     Input('card_colgroup_simulator_code', 'n_clicks'),
#     Input('card_colgroup_attributes', 'n_clicks')
# )
# def return_colgroup_simulator_code(card_colgroup_simulator, card_colgroup_showcase,
#                             card_colgroup_simulator_code, card_colgroup_attributes):
#     if card_colgroup_simulator % 2 == 0:
#         return area_colgroup_navbar
#     elif card_colgroup_showcase % 2 == 0:
#         return html.Div([
#             # colgroup_navbar,
#             # colgroup_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_colgroup')
#     elif card_colgroup_simulator_code % 2 == 0:
#         return html.Div([
#             # colgroup_navbar,
#             # colgroup_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_colgroup')
#     elif card_colgroup_attributes % 2 == 0:
#         return html.Div([
#             # colgroup_navbar,
#             global_attributes
#         ], id='card_display_colgroup')
#     else:
#         return dash.no_update
# # Card data html.Data Simulator Code
# @dash.callback(
#     Output('card_display_data', 'children'),
#     Input('card_data_simulator', 'n_clicks'),
#     Input('card_data_showcase', 'n_clicks'),
#     Input('card_data_simulator_code', 'n_clicks'),
#     Input('card_data_attributes', 'n_clicks')
# )
# def return_data_simulator_code(card_data_simulator, card_data_showcase,
#                             card_data_simulator_code, card_data_attributes):
#     if card_data_simulator % 2 == 0:
#         return area_data_navbar
#     elif card_data_showcase % 2 == 0:
#         return html.Div([
#             # data_navbar,
#             # data_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_data')
#     elif card_data_simulator_code % 2 == 0:
#         return html.Div([
#             # data_navbar,
#             # data_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_data')
#     elif card_data_attributes % 2 == 0:
#         return html.Div([
#             # data_navbar,
#             global_attributes
#         ], id='card_display_data')
#     else:
#         return dash.no_update
# # Card datalist html.Datalist Simulator Code
# @dash.callback(
#     Output('card_display_datalist', 'children'),
#     Input('card_datalist_simulator', 'n_clicks'),
#     Input('card_datalist_showcase', 'n_clicks'),
#     Input('card_datalist_simulator_code', 'n_clicks'),
#     Input('card_datalist_attributes', 'n_clicks')
# )
# def return_datalist_simulator_code(card_datalist_simulator, card_datalist_showcase,
#                             card_datalist_simulator_code, card_datalist_attributes):
#     if card_datalist_simulator % 2 == 0:
#         return area_datalist_navbar
#     elif card_datalist_showcase % 2 == 0:
#         return html.Div([
#             # datalist_navbar,
#             # datalist_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_datalist')
#     elif card_datalist_simulator_code % 2 == 0:
#         return html.Div([
#             # datalist_navbar,
#             # datalist_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_datalist')
#     elif card_datalist_attributes % 2 == 0:
#         return html.Div([
#             # datalist_navbar,
#             global_attributes
#         ], id='card_display_datalist')
#     else:
#         return dash.no_update
# # Card dd html.DD Simulator Code
# @dash.callback(
#     Output('card_display_dd', 'children'),
#     Input('card_dd_simulator', 'n_clicks'),
#     Input('card_dd_showcase', 'n_clicks'),
#     Input('card_dd_simulator_code', 'n_clicks'),
#     Input('card_dd_attributes', 'n_clicks')
# )
# def return_dd_simulator_code(card_dd_simulator, card_dd_showcase,
#                             card_dd_simulator_code, card_dd_attributes):
#     if card_dd_simulator % 2 == 0:
#         return area_dd_navbar
#     elif card_dd_showcase % 2 == 0:
#         return html.Div([
#             # dd_navbar,
#             # dd_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_dd')
#     elif card_dd_simulator_code % 2 == 0:
#         return html.Div([
#             # dd_navbar,
#             # dd_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_dd')
#     elif card_dd_attributes % 2 == 0:
#         return html.Div([
#             # dd_navbar,
#             global_attributes
#         ], id='card_display_dd')
#     else:
#         return dash.no_update
# # Card del html.Del Simulator Code
# @dash.callback(
#     Output('card_display_del', 'children'),
#     Input('card_del_simulator', 'n_clicks'),
#     Input('card_del_showcase', 'n_clicks'),
#     Input('card_del_simulator_code', 'n_clicks'),
#     Input('card_del_attributes', 'n_clicks')
# )
# def return_del_simulator_code(card_del_simulator, card_del_showcase,
#                             card_del_simulator_code, card_del_attributes):
#     if card_del_simulator % 2 == 0:
#         return area_del_navbar
#     elif card_del_showcase % 2 == 0:
#         return html.Div([
#             # del_navbar,
#             # del_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_del')
#     elif card_del_simulator_code % 2 == 0:
#         return html.Div([
#             # del_navbar,
#             # del_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_del')
#     elif card_del_attributes % 2 == 0:
#         return html.Div([
#             # del_navbar,
#             global_attributes
#         ], id='card_display_del')
#     else:
#         return dash.no_update
# # Card details html.Details Simulator Code
# @dash.callback(
#     Output('card_display_details', 'children'),
#     Input('card_details_simulator', 'n_clicks'),
#     Input('card_details_showcase', 'n_clicks'),
#     Input('card_details_simulator_code', 'n_clicks'),
#     Input('card_details_attributes', 'n_clicks')
# )
# def return_details_simulator_code(card_details_simulator, card_details_showcase,
#                             card_details_simulator_code, card_details_attributes):
#     if card_details_simulator % 2 == 0:
#         return area_details_navbar
#     elif card_details_showcase % 2 == 0:
#         return html.Div([
#             # details_navbar,
#             # details_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_details')
#     elif card_details_simulator_code % 2 == 0:
#         return html.Div([
#             # details_navbar,
#             # details_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_details')
#     elif card_details_attributes % 2 == 0:
#         return html.Div([
#             # details_navbar,
#             global_attributes
#         ], id='card_display_details')
#     else:
#         return dash.no_update
# # Card dfn html.Dfn Simulator Code
# @dash.callback(
#     Output('card_display_dfn', 'children'),
#     Input('card_dfn_simulator', 'n_clicks'),
#     Input('card_dfn_showcase', 'n_clicks'),
#     Input('card_dfn_simulator_code', 'n_clicks'),
#     Input('card_dfn_attributes', 'n_clicks')
# )
# def return_dfn_simulator_code(card_dfn_simulator, card_dfn_showcase,
#                             card_dfn_simulator_code, card_dfn_attributes):
#     if card_dfn_simulator % 2 == 0:
#         return area_dfn_navbar
#     elif card_dfn_showcase % 2 == 0:
#         return html.Div([
#             # dfn_navbar,
#             # dfn_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_dfn')
#     elif card_dfn_simulator_code % 2 == 0:
#         return html.Div([
#             # dfn_navbar,
#             # dfn_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_dfn')
#     elif card_dfn_attributes % 2 == 0:
#         return html.Div([
#             # dfn_navbar,
#             global_attributes
#         ], id='card_display_dfn')
#     else:
#         return dash.no_update
# # Card dialog html.Dialog Simulator Code
# @dash.callback(
#     Output('card_display_dialog', 'children'),
#     Input('card_dialog_simulator', 'n_clicks'),
#     Input('card_dialog_showcase', 'n_clicks'),
#     Input('card_dialog_simulator_code', 'n_clicks'),
#     Input('card_dialog_attributes', 'n_clicks')
# )
# def return_dialog_simulator_code(card_dialog_simulator, card_dialog_showcase,
#                             card_dialog_simulator_code, card_dialog_attributes):
#     if card_dialog_simulator % 2 == 0:
#         return area_dialog_navbar
#     elif card_dialog_showcase % 2 == 0:
#         return html.Div([
#             # dialog_navbar,
#             # dialog_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_dialog')
#     elif card_dialog_simulator_code % 2 == 0:
#         return html.Div([
#             # dialog_navbar,
#             # dialog_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_dialog')
#     elif card_dialog_attributes % 2 == 0:
#         return html.Div([
#             # dialog_navbar,
#             global_attributes
#         ], id='card_display_dialog')
#     else:
#         return dash.no_update
# # Card dir html.Dir Simulator Code
# @dash.callback(
#     Output('card_display_dir', 'children'),
#     Input('card_dir_simulator', 'n_clicks'),
#     Input('card_dir_showcase', 'n_clicks'),
#     Input('card_dir_simulator_code', 'n_clicks'),
#     Input('card_dir_attributes', 'n_clicks')
# )
# def return_dir_simulator_code(card_dir_simulator, card_dir_showcase,
#                             card_dir_simulator_code, card_dir_attributes):
#     if card_dir_simulator % 2 == 0:
#         return area_dir_navbar
#     elif card_dir_showcase % 2 == 0:
#         return html.Div([
#             # dir_navbar,
#             # dir_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_dir')
#     elif card_dir_simulator_code % 2 == 0:
#         return html.Div([
#             # dir_navbar,
#             # dir_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_dir')
#     elif card_dir_attributes % 2 == 0:
#         return html.Div([
#             # dir_navbar,
#             global_attributes
#         ], id='card_display_dir')
#     else:
#         return dash.no_update
# # Card div html.Div Simulator Code
# @dash.callback(
#     Output('card_display_div', 'children'),
#     Input('card_div_simulator', 'n_clicks'),
#     Input('card_div_showcase', 'n_clicks'),
#     Input('card_div_simulator_code', 'n_clicks'),
#     Input('card_div_attributes', 'n_clicks')
# )
# def return_div_simulator_code(card_div_simulator, card_div_showcase,
#                             card_div_simulator_code, card_div_attributes):
#     if card_div_simulator % 2 == 0:
#         return area_div_navbar
#     elif card_div_showcase % 2 == 0:
#         return html.Div([
#             # div_navbar,
#             # div_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_div')
#     elif card_div_simulator_code % 2 == 0:
#         return html.Div([
#             # div_navbar,
#             # div_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_div')
#     elif card_div_attributes % 2 == 0:
#         return html.Div([
#             # div_navbar,
#             global_attributes
#         ], id='card_display_div')
#     else:
#         return dash.no_update
# # Card dl html.Dl Simulator Code
# @dash.callback(
#     Output('card_display_dl', 'children'),
#     Input('card_dl_simulator', 'n_clicks'),
#     Input('card_dl_showcase', 'n_clicks'),
#     Input('card_dl_simulator_code', 'n_clicks'),
#     Input('card_dl_attributes', 'n_clicks')
# )
# def return_dl_simulator_code(card_dl_simulator, card_dl_showcase,
#                             card_dl_simulator_code, card_dl_attributes):
#     if card_dl_simulator % 2 == 0:
#         return area_dl_navbar
#     elif card_dl_showcase % 2 == 0:
#         return html.Div([
#             # dl_navbar,
#             # dl_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_dl')
#     elif card_dl_simulator_code % 2 == 0:
#         return html.Div([
#             # dl_navbar,
#             # dl_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_dl')
#     elif card_dl_attributes % 2 == 0:
#         return html.Div([
#             # dl_navbar,
#             global_attributes
#         ], id='card_display_dl')
#     else:
#         return dash.no_update
# # Card dt html.Dt Simulator Code
# @dash.callback(
#     Output('card_display_dt', 'children'),
#     Input('card_dt_simulator', 'n_clicks'),
#     Input('card_dt_showcase', 'n_clicks'),
#     Input('card_dt_simulator_code', 'n_clicks'),
#     Input('card_dt_attributes', 'n_clicks')
# )
# def return_dt_simulator_code(card_dt_simulator, card_dt_showcase,
#                             card_dt_simulator_code, card_dt_attributes):
#     if card_dt_simulator % 2 == 0:
#         return area_dt_navbar
#     elif card_dt_showcase % 2 == 0:
#         return html.Div([
#             # dt_navbar,
#             # dt_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_dt')
#     elif card_dt_simulator_code % 2 == 0:
#         return html.Div([
#             # dt_navbar,
#             # dt_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_dt')
#     elif card_dt_attributes % 2 == 0:
#         return html.Div([
#             # dt_navbar,
#             global_attributes
#         ], id='card_display_dt')
#     else:
#         return dash.no_update
# # Card em html.Em Simulator Code
# @dash.callback(
#     Output('card_display_em', 'children'),
#     Input('card_em_simulator', 'n_clicks'),
#     Input('card_em_showcase', 'n_clicks'),
#     Input('card_em_simulator_code', 'n_clicks'),
#     Input('card_em_attributes', 'n_clicks')
# )
# def return_em_simulator_code(card_em_simulator, card_em_showcase,
#                             card_em_simulator_code, card_em_attributes):
#     if card_em_simulator % 2 == 0:
#         return em_simulator_navbar
#     elif card_em_showcase % 2 == 0:
#         return html.Div([
#             # em_navbar,
#             # em_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_em')
#     elif card_em_simulator_code % 2 == 0:
#         return html.Div([
#             # em_navbar,
#             # em_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_em')
#     elif card_em_attributes % 2 == 0:
#         return html.Div([
#             # em_navbar,
#             global_attributes
#         ], id='card_display_em')
#     else:
#         return dash.no_update
# # Card embed html.Embed Simulator Code
# @dash.callback(
#     Output('card_display_embed', 'children'),
#     Input('card_embed_simulator', 'n_clicks'),
#     Input('card_embed_showcase', 'n_clicks'),
#     Input('card_embed_simulator_code', 'n_clicks'),
#     Input('card_embed_attributes', 'n_clicks')
# )
# def return_embed_simulator_code(card_embed_simulator, card_embed_showcase,
#                             card_embed_simulator_code, card_embed_attributes):
#     if card_embed_simulator % 2 == 0:
#         return embed_simulator_navbar
#     elif card_embed_showcase % 2 == 0:
#         return html.Div([
#             # embed_navbar,
#             # embed_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_embed')
#     elif card_embed_simulator_code % 2 == 0:
#         return html.Div([
#             # embed_navbar,
#             # embed_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_embed')
#     elif card_embed_attributes % 2 == 0:
#         return html.Div([
#             # embed_navbar,
#             global_attributes
#         ], id='card_display_embed')
#     else:
#         return dash.no_update
# # Card fieldset html.Fieldset Simulator Code
# @dash.callback(
#     Output('card_display_fieldset', 'children'),
#     Input('card_fieldset_simulator', 'n_clicks'),
#     Input('card_fieldset_showcase', 'n_clicks'),
#     Input('card_fieldset_simulator_code', 'n_clicks'),
#     Input('card_fieldset_attributes', 'n_clicks')
# )
# def return_fieldset_simulator_code(card_fieldset_simulator, card_fieldset_showcase,
#                             card_fieldset_simulator_code, card_fieldset_attributes):
#     if card_fieldset_simulator % 2 == 0:
#         return fieldset_simulator_navbar
#     elif card_fieldset_showcase % 2 == 0:
#         return html.Div([
#             # fieldset_navbar,
#             # fieldset_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_fieldset')
#     elif card_fieldset_simulator_code % 2 == 0:
#         return html.Div([
#             # fieldset_navbar,
#             # fieldset_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_fieldset')
#     elif card_fieldset_attributes % 2 == 0:
#         return html.Div([
#             # fieldset_navbar,
#             global_attributes
#         ], id='card_display_fieldset')
#     else:
#         return dash.no_update
# # Card figcaption html.Figcaption Simulator Code
# @dash.callback(
#     Output('card_display_figcaption', 'children'),
#     Input('card_figcaption_simulator', 'n_clicks'),
#     Input('card_figcaption_showcase', 'n_clicks'),
#     Input('card_figcaption_simulator_code', 'n_clicks'),
#     Input('card_figcaption_attributes', 'n_clicks')
# )
# def return_figcaption_simulator_code(card_figcaption_simulator, card_figcaption_showcase,
#                             card_figcaption_simulator_code, card_figcaption_attributes):
#     if card_figcaption_simulator % 2 == 0:
#         return figcaption_simulator_navbar
#     elif card_figcaption_showcase % 2 == 0:
#         return html.Div([
#             # figcaption_navbar,
#             # figcaption_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_figcaption')
#     elif card_figcaption_simulator_code % 2 == 0:
#         return html.Div([
#             # figcaption_navbar,
#             # figcaption_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_figcaption')
#     elif card_figcaption_attributes % 2 == 0:
#         return html.Div([
#             # figcaption_navbar,
#             global_attributes
#         ], id='card_display_figcaption')
#     else:
#         return dash.no_update
# # Card figure html.Figure Simulator Code
# @dash.callback(
#     Output('card_display_figure', 'children'),
#     Input('card_figure_simulator', 'n_clicks'),
#     Input('card_figure_showcase', 'n_clicks'),
#     Input('card_figure_simulator_code', 'n_clicks'),
#     Input('card_figure_attributes', 'n_clicks')
# )
# def return_figure_simulator_code(card_figure_simulator, card_figure_showcase,
#                             card_figure_simulator_code, card_figure_attributes):
#     if card_figure_simulator % 2 == 0:
#         return figure_simulator_navbar
#     elif card_figure_showcase % 2 == 0:
#         return html.Div([
#             # figure_navbar,
#             # figure_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_figure')
#     elif card_figure_simulator_code % 2 == 0:
#         return html.Div([
#             # figure_navbar,
#             # figure_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_figure')
#     elif card_figure_attributes % 2 == 0:
#         return html.Div([
#             # figure_navbar,
#             global_attributes
#         ], id='card_display_figure')
#     else:
#         return dash.no_update
# # Card font html.Font Simulator Code
# @dash.callback(
#     Output('card_display_font', 'children'),
#     Input('card_font_simulator', 'n_clicks'),
#     Input('card_font_showcase', 'n_clicks'),
#     Input('card_font_simulator_code', 'n_clicks'),
#     Input('card_font_attributes', 'n_clicks')
# )
# def return_font_simulator_code(card_font_simulator, card_font_showcase,
#                             card_font_simulator_code, card_font_attributes):
#     if card_font_simulator % 2 == 0:
#         return font_simulator_navbar
#     elif card_font_showcase % 2 == 0:
#         return html.Div([
#             # font_navbar,
#             # font_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_font')
#     elif card_font_simulator_code % 2 == 0:
#         return html.Div([
#             # font_navbar,
#             # font_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_font')
#     elif card_font_attributes % 2 == 0:
#         return html.Div([
#             # font_navbar,
#             global_attributes
#         ], id='card_display_font')
#     else:
#         return dash.no_update
# # Card frameset html.Frameset Simulator Code
# @dash.callback(
#     Output('card_display_frameset', 'children'),
#     Input('card_frameset_simulator', 'n_clicks'),
#     Input('card_frameset_showcase', 'n_clicks'),
#     Input('card_frameset_simulator_code', 'n_clicks'),
#     Input('card_frameset_attributes', 'n_clicks')
# )
# def return_frameset_simulator_code(card_frameset_simulator, card_frameset_showcase,
#                             card_frameset_simulator_code, card_frameset_attributes):
#     if card_frameset_simulator % 2 == 0:
#         return frameset_simulator_navbar
#     elif card_frameset_showcase % 2 == 0:
#         return html.Div([
#             # frameset_navbar,
#             # frameset_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_frameset')
#     elif card_frameset_simulator_code % 2 == 0:
#         return html.Div([
#             # frameset_navbar,
#             # frameset_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_frameset')
#     elif card_frameset_attributes % 2 == 0:
#         return html.Div([
#             # frameset_navbar,
#             global_attributes
#         ], id='card_display_frameset')
#     else:
#         return dash.no_update
# # Card h1 html.H1 Simulator Code
# @dash.callback(
#     Output('card_display_h1', 'children'),
#     Input('card_h1_simulator', 'n_clicks'),
#     Input('card_h1_showcase', 'n_clicks'),
#     Input('card_h_simulator_code', 'n_clicks'),
#     Input('card_h_attributes', 'n_clicks')
# )
# def return_h1_simulator_code(card_h1_simulator, card_h1_showcase,
#                             card_h1_simulator_code, card_h1_attributes):
#     if card_h1_simulator % 2 == 0:
#         return h1_simulator_navbar
#     elif card_h1_showcase % 2 == 0:
#         return html.Div([
#             # h1_navbar,
#             # h1_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_h1')
#     elif card_h1_simulator_code % 2 == 0:
#         return html.Div([
#             # h1_navbar,
#             # h1_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_h1')
#     elif card_h1_attributes % 2 == 0:
#         return html.Div([
#             # h1_navbar,
#             global_attributes
#         ], id='card_display_h')
#     else:
#         return dash.no_update
# # Card head html.Head Simulator Code
# @dash.callback(
#     Output('card_display_head', 'children'),
#     Input('card_head_simulator', 'n_clicks'),
#     Input('card_head_showcase', 'n_clicks'),
#     Input('card_head_simulator_code', 'n_clicks'),
#     Input('card_head_attributes', 'n_clicks')
# )
# def return_head_simulator_code(card_head_simulator, card_head_showcase,
#                             card_head_simulator_code, card_head_attributes):
#     if card_head_simulator % 2 == 0:
#         return head_simulator_navbar
#     elif card_head_showcase % 2 == 0:
#         return html.Div([
#             # head_navbar,
#             # head_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_head')
#     elif card_head_simulator_code % 2 == 0:
#         return html.Div([
#             # head_navbar,
#             # head_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_head')
#     elif card_head_attributes % 2 == 0:
#         return html.Div([
#             # head_navbar,
#             global_attributes
#         ], id='card_display_head')
#     else:
#         return dash.no_update
# # Card header html.Header Simulator Code
# @dash.callback(
#     Output('card_display_header', 'children'),
#     Input('card_header_simulator', 'n_clicks'),
#     Input('card_header_showcase', 'n_clicks'),
#     Input('card_header_simulator_code', 'n_clicks'),
#     Input('card_header_attributes', 'n_clicks')
# )
# def return_header_simulator_code(card_header_simulator, card_header_showcase,
#                             card_header_simulator_code, card_header_attributes):
#     if card_header_simulator % 2 == 0:
#         return header_simulator_navbar
#     elif card_header_showcase % 2 == 0:
#         return html.Div([
#             # header_navbar,
#             # header_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_header')
#     elif card_header_simulator_code % 2 == 0:
#         return html.Div([
#             # header_navbar,
#             # header_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_header')
#     elif card_header_attributes % 2 == 0:
#         return html.Div([
#             # header_navbar,
#             global_attributes
#         ], id='card_display_header')
#     else:
#         return dash.no_update
# # Card hgroup html.Hgroup Simulator Code
# @dash.callback(
#     Output('card_display_hgroup', 'children'),
#     Input('card_hgroup_simulator', 'n_clicks'),
#     Input('card_hgroup_showcase', 'n_clicks'),
#     Input('card_hgroup_simulator_code', 'n_clicks'),
#     Input('card_hgroup_attributes', 'n_clicks')
# )
# def return_hgroup_simulator_code(card_hgroup_simulator, card_hgroup_showcase,
#                             card_hgroup_simulator_code, card_hgroup_attributes):
#     if card_hgroup_simulator % 2 == 0:
#         return hgroup_simulator_navbar
#     elif card_hgroup_showcase % 2 == 0:
#         return html.Div([
#             # hgroup_navbar,
#             # hgroup_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_h')
#     elif card_hgroup_simulator_code % 2 == 0:
#         return html.Div([
#             # hgroup_navbar,
#             # hgroup_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_hgroup')
#     elif card_hgroup_attributes % 2 == 0:
#         return html.Div([
#             # hgroup_navbar,
#             global_attributes
#         ], id='card_display_hgroup')
#     else:
#         return dash.no_update
# # Card hr html.Hr Simulator Code
# @dash.callback(
#     Output('card_display_hr', 'children'),
#     Input('card_hr_simulator', 'n_clicks'),
#     Input('card_hr_showcase', 'n_clicks'),
#     Input('card_hr_simulator_code', 'n_clicks'),
#     Input('card_hr_attributes', 'n_clicks')
# )
# def return_hr_simulator_code(card_hr_simulator, card_hr_showcase,
#                             card_hr_simulator_code, card_hr_attributes):
#     if card_hr_simulator % 2 == 0:
#         return hr_simulator_navbar
#     elif card_hr_showcase % 2 == 0:
#         return html.Div([
#             # hr_navbar,
#             # hr_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_hr')
#     elif card_hr_simulator_code % 2 == 0:
#         return html.Div([
#             # hr_navbar,
#             # hr_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_hr')
#     elif card_hr_attributes % 2 == 0:
#         return html.Div([
#             # hr_navbar,
#             global_attributes
#         ], id='card_display_hr')
#     else:
#         return dash.no_update
# # Card i html.I Simulator Code
# @dash.callback(
#     Output('card_display_i', 'children'),
#     Input('card_i_simulator', 'n_clicks'),
#     Input('card_i_showcase', 'n_clicks'),
#     Input('card_i_simulator_code', 'n_clicks'),
#     Input('card_i_attributes', 'n_clicks')
# )
# def return_i_simulator_code(card_i_simulator, card_i_showcase,
#                             card_i_simulator_code, card_i_attributes):
#     if card_i_simulator % 2 == 0:
#         return i_simulator_navbar
#     elif card_i_showcase % 2 == 0:
#         return html.Div([
#             # i_navbar,
#             # i_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_i')
#     elif card_i_simulator_code % 2 == 0:
#         return html.Div([
#             # i_navbar,
#             # i_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_i')
#     elif card_i_attributes % 2 == 0:
#         return html.Div([
#             # i_navbar,
#             global_attributes
#         ], id='card_display_i')
#     else:
#         return dash.no_update
# # Card iframe html.Iframe Simulator Code
# @dash.callback(
#     Output('card_display_iframe', 'children'),
#     Input('card_iframe_simulator', 'n_clicks'),
#     Input('card_iframe_showcase', 'n_clicks'),
#     Input('card_iframe_simulator_code', 'n_clicks'),
#     Input('card_iframe_attributes', 'n_clicks')
# )
# def return_iframe_simulator_code(card_iframe_simulator, card_iframe_showcase,
#                             card_iframe_simulator_code, card_iframe_attributes):
#     if card_iframe_simulator % 2 == 0:
#         return iframe_simulator_navbar
#     elif card_iframe_showcase % 2 == 0:
#         return html.Div([
#             # iframe_navbar,
#             # iframe_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_iframe')
#     elif card_iframe_simulator_code % 2 == 0:
#         return html.Div([
#             # iframe_navbar,
#             # iframe_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_iframe')
#     elif card_iframe_attributes % 2 == 0:
#         return html.Div([
#             # iframe_navbar,
#             global_attributes
#         ], id='card_display_iframe')
#     else:
#         return dash.no_update
# # Card img html.Img Simulator Code
# @dash.callback(
#     Output('card_display_img', 'children'),
#     Input('card_img_simulator', 'n_clicks'),
#     Input('card_img_showcase', 'n_clicks'),
#     Input('card_img_simulator_code', 'n_clicks'),
#     Input('card_img_attributes', 'n_clicks')
# )
# def return_img_simulator_code(card_img_simulator, card_img_showcase,
#                             card_img_simulator_code, card_img_attributes):
#     if card_img_simulator % 2 == 0:
#         return img_simulator_navbar
#     elif card_img_showcase % 2 == 0:
#         return html.Div([
#             # img_navbar,
#             # img_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_img')
#     elif card_img_simulator_code % 2 == 0:
#         return html.Div([
#             # img_navbar,
#             # img_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_img')
#     elif card_img_attributes % 2 == 0:
#         return html.Div([
#             # img_navbar,
#             global_attributes
#         ], id='card_display_img')
#     else:
#         return dash.no_update
# # Card input html.Input Simulator Code
# @dash.callback(
#     Output('card_display_input', 'children'),
#     Input('card_input_simulator', 'n_clicks'),
#     Input('card_input_showcase', 'n_clicks'),
#     Input('card_input_simulator_code', 'n_clicks'),
#     Input('card_input_attributes', 'n_clicks')
# )
# def return_input_simulator_code(card_input_simulator, card_input_showcase,
#                             card_input_simulator_code, card_input_attributes):
#     if card_input_simulator % 2 == 0:
#         return input_simulator_navbar
#     elif card_input_showcase % 2 == 0:
#         return html.Div([
#             # input_navbar,
#             # input_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_input')
#     elif card_input_simulator_code % 2 == 0:
#         return html.Div([
#             # input_navbar,
#             # input_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_input')
#     elif card_input_attributes % 2 == 0:
#         return html.Div([
#             # input_navbar,
#             global_attributes
#         ], id='card_display_input')
#     else:
#         return dash.no_update
# # Card ins html.Ins Simulator Code
# @dash.callback(
#     Output('card_display_ins', 'children'),
#     Input('card_ins_simulator', 'n_clicks'),
#     Input('card_ins_showcase', 'n_clicks'),
#     Input('card_ins_simulator_code', 'n_clicks'),
#     Input('card_ins_attributes', 'n_clicks')
# )
# def return_ins_simulator_code(card_ins_simulator, card_ins_showcase,
#                             card_ins_simulator_code, card_ins_attributes):
#     if card_ins_simulator % 2 == 0:
#         return ins_simulator_navbar
#     elif card_ins_showcase % 2 == 0:
#         return html.Div([
#             # ins_navbar,
#             # ins_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_ins')
#     elif card_ins_simulator_code % 2 == 0:
#         return html.Div([
#             # ins_navbar,
#             # ins_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_ins')
#     elif card_ins_attributes % 2 == 0:
#         return html.Div([
#             # ins_navbar,
#             global_attributes
#         ], id='card_display_ins')
#     else:
#         return dash.no_update
# # Card kbd html.Kbd Simulator Code
# @dash.callback(
#     Output('card_display_k', 'children'),
#     Input('card_k_simulator', 'n_clicks'),
#     Input('card_k_showcase', 'n_clicks'),
#     Input('card_k_simulator_code', 'n_clicks'),
#     Input('card_k_attributes', 'n_clicks')
# )
# def return_k_simulator_code(card_k_simulator, card_k_showcase,
#                             card_k_simulator_code, card_k_attributes):
#     if card_k_simulator % 2 == 0:
#         return k_simulator_navbar
#     elif card_k_showcase % 2 == 0:
#         return html.Div([
#             # k_navbar,
#             # k_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_k')
#     elif card_k_simulator_code % 2 == 0:
#         return html.Div([
#             # k_navbar,
#             # k_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_k')
#     elif card_k_attributes % 2 == 0:
#         return html.Div([
#             # k_navbar,
#             global_attributes
#         ], id='card_display_k')
#     else:
#         return dash.no_update
# # Card label html.Label Simulator Code
# @dash.callback(
#     Output('card_display_l', 'children'),
#     Input('card_l_simulator', 'n_clicks'),
#     Input('card_l_showcase', 'n_clicks'),
#     Input('card_l_simulator_code', 'n_clicks'),
#     Input('card_l_attributes', 'n_clicks')
# )
# def return_l_simulator_code(card_l_simulator, card_l_showcase,
#                             card_l_simulator_code, card_l_attributes):
#     if card_l_simulator % 2 == 0:
#         return l_simulator_navbar
#     elif card_l_showcase % 2 == 0:
#         return html.Div([
#             # l_navbar,
#             # l_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_l')
#     elif card_l_simulator_code % 2 == 0:
#         return html.Div([
#             # l_navbar,
#             # l_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_l')
#     elif card_l_attributes % 2 == 0:
#         return html.Div([
#             # l_navbar,
#             global_attributes
#         ], id='card_display_l')
#     else:
#         return dash.no_update
# # Card legend html.Legend Simulator Code
# @dash.callback(
#     Output('card_display_l', 'children'),
#     Input('card_l_simulator', 'n_clicks'),
#     Input('card_l_showcase', 'n_clicks'),
#     Input('card_l_simulator_code', 'n_clicks'),
#     Input('card_l_attributes', 'n_clicks')
# )
# def return_l_simulator_code(card_l_simulator, card_l_showcase,
#                             card_l_simulator_code, card_l_attributes):
#     if card_l_simulator % 2 == 0:
#         return l_simulator_navbar
#     elif card_l_showcase % 2 == 0:
#         return html.Div([
#             # l_navbar,
#             # l_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_l')
#     elif card_l_simulator_code % 2 == 0:
#         return html.Div([
#             # l_navbar,
#             # l_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_l')
#     elif card_l_attributes % 2 == 0:
#         return html.Div([
#             # l_navbar,
#             global_attributes
#         ], id='card_display_l')
#     else:
#         return dash.no_update
# # Card li html.Li Simulator Code
# @dash.callback(
#     Output('card_display_l', 'children'),
#     Input('card_l_simulator', 'n_clicks'),
#     Input('card_l_showcase', 'n_clicks'),
#     Input('card_l_simulator_code', 'n_clicks'),
#     Input('card_l_attributes', 'n_clicks')
# )
# def return_l_simulator_code(card_l_simulator, card_l_showcase,
#                             card_l_simulator_code, card_l_attributes):
#     if card_l_simulator % 2 == 0:
#         return l_simulator_navbar
#     elif card_l_showcase % 2 == 0:
#         return html.Div([
#             # l_navbar,
#             # l_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_l')
#     elif card_l_simulator_code % 2 == 0:
#         return html.Div([
#             # l_navbar,
#             # l_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_l')
#     elif card_l_attributes % 2 == 0:
#         return html.Div([
#             # l_navbar,
#             global_attributes
#         ], id='card_display_l')
#     else:
#         return dash.no_update
# # Card link html.Link Simulator Code
# @dash.callback(
#     Output('card_display_l', 'children'),
#     Input('card_l_simulator', 'n_clicks'),
#     Input('card_l_showcase', 'n_clicks'),
#     Input('card_l_simulator_code', 'n_clicks'),
#     Input('card_l_attributes', 'n_clicks')
# )
# def return_l_simulator_code(card_l_simulator, card_l_showcase,
#                             card_l_simulator_code, card_l_attributes):
#     if card_l_simulator % 2 == 0:
#         return l_simulator_navbar
#     elif card_l_showcase % 2 == 0:
#         return html.Div([
#             # l_navbar,
#             # l_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_l')
#     elif card_l_simulator_code % 2 == 0:
#         return html.Div([
#             # l_navbar,
#             # l_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_l')
#     elif card_l_attributes % 2 == 0:
#         return html.Div([
#             # l_navbar,
#             global_attributes
#         ], id='card_display_l')
#     else:
#         return dash.no_update
# # Card main html.Main Simulator Code
# @dash.callback(
#     Output('card_display_m', 'children'),
#     Input('card_m_simulator', 'n_clicks'),
#     Input('card_m_showcase', 'n_clicks'),
#     Input('card_m_simulator_code', 'n_clicks'),
#     Input('card_m_attributes', 'n_clicks')
# )
# def return_m_simulator_code(card_m_simulator, card_m_showcase,
#                             card_m_simulator_code, card_m_attributes):
#     if card_m_simulator % 2 == 0:
#         return m_simulator_navbar
#     elif card_m_showcase % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             # m_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_m')
#     elif card_m_simulator_code % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             # m_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_m')
#     elif card_m_attributes % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             global_attributes
#         ], id='card_display_m')
#     else:
#         return dash.no_update
# # Card map html.Map Simulator Code
# @dash.callback(
#     Output('card_display_m', 'children'),
#     Input('card_m_simulator', 'n_clicks'),
#     Input('card_m_showcase', 'n_clicks'),
#     Input('card_m_simulator_code', 'n_clicks'),
#     Input('card_m_attributes', 'n_clicks')
# )
# def return_m_simulator_code(card_m_simulator, card_m_showcase,
#                             card_m_simulator_code, card_m_attributes):
#     if card_m_simulator % 2 == 0:
#         return m_simulator_navbar
#     elif card_m_showcase % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             # m_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_m')
#     elif card_m_simulator_code % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             # m_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_m')
#     elif card_m_attributes % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             global_attributes
#         ], id='card_display_m')
#     else:
#         return dash.no_update
# # Card mark html.Mark Simulator Code
# @dash.callback(
#     Output('card_display_m', 'children'),
#     Input('card_m_simulator', 'n_clicks'),
#     Input('card_m_showcase', 'n_clicks'),
#     Input('card_m_simulator_code', 'n_clicks'),
#     Input('card_m_attributes', 'n_clicks')
# )
# def return_m_simulator_code(card_m_simulator, card_m_showcase,
#                             card_m_simulator_code, card_m_attributes):
#     if card_m_simulator % 2 == 0:
#         return m_simulator_navbar
#     elif card_m_showcase % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             # m_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_m')
#     elif card_m_simulator_code % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             # m_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_m')
#     elif card_m_attributes % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             global_attributes
#         ], id='card_display_m')
#     else:
#         return dash.no_update
# # Card marque html.Marque Simulator Code
# @dash.callback(
#     Output('card_display_m', 'children'),
#     Input('card_m_simulator', 'n_clicks'),
#     Input('card_m_showcase', 'n_clicks'),
#     Input('card_m_simulator_code', 'n_clicks'),
#     Input('card_m_attributes', 'n_clicks')
# )
# def return_m_simulator_code(card_m_simulator, card_m_showcase,
#                             card_m_simulator_code, card_m_attributes):
#     if card_m_simulator % 2 == 0:
#         return m_simulator_navbar
#     elif card_m_showcase % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             # m_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_m')
#     elif card_m_simulator_code % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             # m_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_m')
#     elif card_m_attributes % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             global_attributes
#         ], id='card_display_m')
#     else:
#         return dash.no_update
# # Card meta html.Meta Simulator Code
# @dash.callback(
#     Output('card_display_m', 'children'),
#     Input('card_m_simulator', 'n_clicks'),
#     Input('card_m_showcase', 'n_clicks'),
#     Input('card_m_simulator_code', 'n_clicks'),
#     Input('card_m_attributes', 'n_clicks')
# )
# def return_m_simulator_code(card_m_simulator, card_m_showcase,
#                             card_m_simulator_code, card_m_attributes):
#     if card_m_simulator % 2 == 0:
#         return m_simulator_navbar
#     elif card_m_showcase % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             # m_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_m')
#     elif card_m_simulator_code % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             # m_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_m')
#     elif card_m_attributes % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             global_attributes
#         ], id='card_display_m')
#     else:
#         return dash.no_update
# # Card meter html.Meter Simulator Code
# @dash.callback(
#     Output('card_display_m', 'children'),
#     Input('card_m_simulator', 'n_clicks'),
#     Input('card_m_showcase', 'n_clicks'),
#     Input('card_m_simulator_code', 'n_clicks'),
#     Input('card_m_attributes', 'n_clicks')
# )
# def return_m_simulator_code(card_m_simulator, card_m_showcase,
#                             card_m_simulator_code, card_m_attributes):
#     if card_m_simulator % 2 == 0:
#         return m_simulator_navbar
#     elif card_m_showcase % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             # m_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_m')
#     elif card_m_simulator_code % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             # m_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_m')
#     elif card_m_attributes % 2 == 0:
#         return html.Div([
#             # m_navbar,
#             global_attributes
#         ], id='card_display_m')
#     else:
#         return dash.no_update
# # Card nav html.Nav Simulator Code
# @dash.callback(
#     Output('card_display_n', 'children'),
#     Input('card_n_simulator', 'n_clicks'),
#     Input('card_n_showcase', 'n_clicks'),
#     Input('card_n_simulator_code', 'n_clicks'),
#     Input('card_n_attributes', 'n_clicks')
# )
# def return_n_simulator_code(card_n_simulator, card_n_showcase,
#                             card_n_simulator_code, card_n_attributes):
#     if card_n_simulator % 2 == 0:
#         return n_simulator_navbar
#     elif card_n_showcase % 2 == 0:
#         return html.Div([
#             # n_navbar,
#             # n_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_n')
#     elif card_n_simulator_code % 2 == 0:
#         return html.Div([
#             # n_navbar,
#             # n_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_n')
#     elif card_n_attributes % 2 == 0:
#         return html.Div([
#             # n_navbar,
#             global_attributes
#         ], id='card_display_n')
#     else:
#         return dash.no_update
# # Card noscript html.noscript Simulator Code
# @dash.callback(
#     Output('card_display_n', 'children'),
#     Input('card_n_simulator', 'n_clicks'),
#     Input('card_n_showcase', 'n_clicks'),
#     Input('card_n_simulator_code', 'n_clicks'),
#     Input('card_n_attributes', 'n_clicks')
# )
# def return_n_simulator_code(card_n_simulator, card_n_showcase,
#                             card_n_simulator_code, card_n_attributes):
#     if card_n_simulator % 2 == 0:
#         return n_simulator_navbar
#     elif card_n_showcase % 2 == 0:
#         return html.Div([
#             # n_navbar,
#             # n_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_n')
#     elif card_n_simulator_code % 2 == 0:
#         return html.Div([
#             # n_navbar,
#             # n_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_n')
#     elif card_n_attributes % 2 == 0:
#         return html.Div([
#             # n_navbar,
#             global_attributes
#         ], id='card_display_n')
#     else:
#         return dash.no_update
# # Card ol html.Ol Simulator Code
# @dash.callback(
#     Output('card_display_o', 'children'),
#     Input('card_o_simulator', 'n_clicks'),
#     Input('card_o_showcase', 'n_clicks'),
#     Input('card_o_simulator_code', 'n_clicks'),
#     Input('card_o_attributes', 'n_clicks')
# )
# def return_o_simulator_code(card_o_simulator, card_o_showcase,
#                             card_o_simulator_code, card_o_attributes):
#     if card_o_simulator % 2 == 0:
#         return o_simulator_navbar
#     elif card_o_showcase % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             # o_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_o')
#     elif card_o_simulator_code % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             # o_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_o')
#     elif card_o_attributes % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             global_attributes
#         ], id='card_display_o')
#     else:
#         return dash.no_update
# # Card object html.ObjectEl Simulator Code
# @dash.callback(
#     Output('card_display_o', 'children'),
#     Input('card_o_simulator', 'n_clicks'),
#     Input('card_o_showcase', 'n_clicks'),
#     Input('card_o_simulator_code', 'n_clicks'),
#     Input('card_o_attributes', 'n_clicks')
# )
# def return_o_simulator_code(card_o_simulator, card_o_showcase,
#                             card_o_simulator_code, card_o_attributes):
#     if card_o_simulator % 2 == 0:
#         return o_simulator_navbar
#     elif card_o_showcase % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             # o_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_o')
#     elif card_o_simulator_code % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             # o_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_o')
#     elif card_o_attributes % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             global_attributes
#         ], id='card_display_o')
#     else:
#         return dash.no_update
# # Card optgroup html.Optgroup Simulator Code
# @dash.callback(
#     Output('card_display_o', 'children'),
#     Input('card_o_simulator', 'n_clicks'),
#     Input('card_o_showcase', 'n_clicks'),
#     Input('card_o_simulator_code', 'n_clicks'),
#     Input('card_o_attributes', 'n_clicks')
# )
# def return_o_simulator_code(card_o_simulator, card_o_showcase,
#                             card_o_simulator_code, card_o_attributes):
#     if card_o_simulator % 2 == 0:
#         return o_simulator_navbar
#     elif card_o_showcase % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             # o_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_o')
#     elif card_o_simulator_code % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             # o_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_o')
#     elif card_o_attributes % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             global_attributes
#         ], id='card_display_o')
#     else:
#         return dash.no_update
# # Card option html.Option Simulator Code
# @dash.callback(
#     Output('card_display_o', 'children'),
#     Input('card_o_simulator', 'n_clicks'),
#     Input('card_o_showcase', 'n_clicks'),
#     Input('card_o_simulator_code', 'n_clicks'),
#     Input('card_o_attributes', 'n_clicks')
# )
# def return_o_simulator_code(card_o_simulator, card_o_showcase,
#                             card_o_simulator_code, card_o_attributes):
#     if card_o_simulator % 2 == 0:
#         return o_simulator_navbar
#     elif card_o_showcase % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             # o_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_o')
#     elif card_o_simulator_code % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             # o_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_o')
#     elif card_o_attributes % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             global_attributes
#         ], id='card_display_o')
#     else:
#         return dash.no_update
# # Card output html.Output Simulator Code
# @dash.callback(
#     Output('card_display_o', 'children'),
#     Input('card_o_simulator', 'n_clicks'),
#     Input('card_o_showcase', 'n_clicks'),
#     Input('card_o_simulator_code', 'n_clicks'),
#     Input('card_o_attributes', 'n_clicks')
# )
# def return_o_simulator_code(card_o_simulator, card_o_showcase,
#                             card_o_simulator_code, card_o_attributes):
#     if card_o_simulator % 2 == 0:
#         return o_simulator_navbar
#     elif card_o_showcase % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             # o_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_o')
#     elif card_o_simulator_code % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             # o_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_o')
#     elif card_o_attributes % 2 == 0:
#         return html.Div([
#             # o_navbar,
#             global_attributes
#         ], id='card_display_o')
#     else:
#         return dash.no_update
# # Card p html.P Simulator Code
# @dash.callback(
#     Output('card_display_p', 'children'),
#     Input('card_p_simulator', 'n_clicks'),
#     Input('card_p_showcase', 'n_clicks'),
#     Input('card_p_simulator_code', 'n_clicks'),
#     Input('card_p_attributes', 'n_clicks')
# )
# def return_p_simulator_code(card_p_simulator, card_p_showcase,
#                             card_p_simulator_code, card_p_attributes):
#     if card_p_simulator % 2 == 0:
#         return p_simulator_navbar
#     elif card_p_showcase % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             # p_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_p')
#     elif card_p_simulator_code % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             # p_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_p')
#     elif card_p_attributes % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             global_attributes
#         ], id='card_display_o')
#     else:
#         return dash.no_update
# # Card param html.Param Simulator Code
# @dash.callback(
#     Output('card_display_p', 'children'),
#     Input('card_p_simulator', 'n_clicks'),
#     Input('card_p_showcase', 'n_clicks'),
#     Input('card_p_simulator_code', 'n_clicks'),
#     Input('card_p_attributes', 'n_clicks')
# )
# def return_p_simulator_code(card_p_simulator, card_p_showcase,
#                             card_p_simulator_code, card_p_attributes):
#     if card_p_simulator % 2 == 0:
#         return p_simulator_navbar
#     elif card_p_showcase % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             # p_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_p')
#     elif card_p_simulator_code % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             # p_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_p')
#     elif card_p_attributes % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             global_attributes
#         ], id='card_display_o')
#     else:
#         return dash.no_update
# # Card picture html.Picture Simulator Code
# @dash.callback(
#     Output('card_display_p', 'children'),
#     Input('card_p_simulator', 'n_clicks'),
#     Input('card_p_showcase', 'n_clicks'),
#     Input('card_p_simulator_code', 'n_clicks'),
#     Input('card_p_attributes', 'n_clicks')
# )
# def return_p_simulator_code(card_p_simulator, card_p_showcase,
#                             card_p_simulator_code, card_p_attributes):
#     if card_p_simulator % 2 == 0:
#         return p_simulator_navbar
#     elif card_p_showcase % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             # p_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_p')
#     elif card_p_simulator_code % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             # p_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_p')
#     elif card_p_attributes % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             global_attributes
#         ], id='card_display_o')
#     else:
#         return dash.no_update
# # Card plaintext html.Plaintext Simulator Code
# @dash.callback(
#     Output('card_display_p', 'children'),
#     Input('card_p_simulator', 'n_clicks'),
#     Input('card_p_showcase', 'n_clicks'),
#     Input('card_p_simulator_code', 'n_clicks'),
#     Input('card_p_attributes', 'n_clicks')
# )
# def return_p_simulator_code(card_p_simulator, card_p_showcase,
#                             card_p_simulator_code, card_p_attributes):
#     if card_p_simulator % 2 == 0:
#         return p_simulator_navbar
#     elif card_p_showcase % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             # p_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_p')
#     elif card_p_simulator_code % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             # p_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_p')
#     elif card_p_attributes % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             global_attributes
#         ], id='card_display_o')
#     else:
#         return dash.no_update
# # Card pre html.Pre Simulator Code
# @dash.callback(
#     Output('card_display_p', 'children'),
#     Input('card_p_simulator', 'n_clicks'),
#     Input('card_p_showcase', 'n_clicks'),
#     Input('card_p_simulator_code', 'n_clicks'),
#     Input('card_p_attributes', 'n_clicks')
# )
# def return_p_simulator_code(card_p_simulator, card_p_showcase,
#                             card_p_simulator_code, card_p_attributes):
#     if card_p_simulator % 2 == 0:
#         return p_simulator_navbar
#     elif card_p_showcase % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             # p_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_p')
#     elif card_p_simulator_code % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             # p_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_p')
#     elif card_p_attributes % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             global_attributes
#         ], id='card_display_o')
#     else:
#         return dash.no_update
# # Card progress html.Progress Simulator Code
# @dash.callback(
#     Output('card_display_p', 'children'),
#     Input('card_p_simulator', 'n_clicks'),
#     Input('card_p_showcase', 'n_clicks'),
#     Input('card_p_simulator_code', 'n_clicks'),
#     Input('card_p_attributes', 'n_clicks')
# )
# def return_p_simulator_code(card_p_simulator, card_p_showcase,
#                             card_p_simulator_code, card_p_attributes):
#     if card_p_simulator % 2 == 0:
#         return p_simulator_navbar
#     elif card_p_showcase % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             # p_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_p')
#     elif card_p_simulator_code % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             # p_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_p')
#     elif card_p_attributes % 2 == 0:
#         return html.Div([
#             # p_navbar,
#             global_attributes
#         ], id='card_display_o')
#     else:
#         return dash.no_update
# # Card q html.Q Simulator Code
# @dash.callback(
#     Output('card_display_q', 'children'),
#     Input('card_q_simulator', 'n_clicks'),
#     Input('card_q_showcase', 'n_clicks'),
#     Input('card_q_simulator_code', 'n_clicks'),
#     Input('card_q_attributes', 'n_clicks')
# )
# def return_p_simulator_code(card_q_simulator, card_q_showcase,
#                             card_q_simulator_code, card_q_attributes):
#     if card_q_simulator % 2 == 0:
#         return q_simulator_navbar
#     elif card_q_showcase % 2 == 0:
#         return html.Div([
#             # q_navbar,
#             # q_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_q')
#     elif card_q_simulator_code % 2 == 0:
#         return html.Div([
#             # q_navbar,
#             # q_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_q')
#     elif card_q_attributes % 2 == 0:
#         return html.Div([
#             # q_navbar,
#             global_attributes
#         ], id='card_display_q')
#     else:
#         return dash.no_update
# # Card rb html.Rb Simulator Code
# @dash.callback(
#     Output('card_display_rb', 'children'),
#     Input('card_rb_simulator', 'n_clicks'),
#     Input('card_rb_showcase', 'n_clicks'),
#     Input('card_rb_simulator_code', 'n_clicks'),
#     Input('card_rb_attributes', 'n_clicks')
# )
# def return_rb_simulator_code(card_rb_simulator, card_rb_showcase,
#                             card_rb_simulator_code, card_rb_attributes):
#     if card_rb_simulator % 2 == 0:
#         return rb_simulator_navbar
#     elif card_rb_showcase % 2 == 0:
#         return html.Div([
#             # rb_navbar,
#             # rb_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_rb')
#     elif card_rb_simulator_code % 2 == 0:
#         return html.Div([
#             # rb_navbar,
#             # rb_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_rb')
#     elif card_rb_attributes % 2 == 0:
#         return html.Div([
#             # rb_navbar,
#             global_attributes
#         ], id='card_display_rb')
#     else:
#         return dash.no_update
# # Card rt html.Rt Simulator Code
# @dash.callback(
#     Output('card_display_rb', 'children'),
#     Input('card_rb_simulator', 'n_clicks'),
#     Input('card_rb_showcase', 'n_clicks'),
#     Input('card_rb_simulator_code', 'n_clicks'),
#     Input('card_rb_attributes', 'n_clicks')
# )
# def return_rb_simulator_code(card_rb_simulator, card_rb_showcase,
#                             card_rb_simulator_code, card_rb_attributes):
#     if card_rb_simulator % 2 == 0:
#         return rb_simulator_navbar
#     elif card_rb_showcase % 2 == 0:
#         return html.Div([
#             # rb_navbar,
#             # rb_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_rb')
#     elif card_rb_simulator_code % 2 == 0:
#         return html.Div([
#             # rb_navbar,
#             # rb_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_rb')
#     elif card_rb_attributes % 2 == 0:
#         return html.Div([
#             # rb_navbar,
#             global_attributes
#         ], id='card_display_rb')
#     else:
#         return dash.no_update
# # Card rtc html.Rtc Simulator Code
# @dash.callback(
#     Output('card_display_rb', 'children'),
#     Input('card_rb_simulator', 'n_clicks'),
#     Input('card_rb_showcase', 'n_clicks'),
#     Input('card_rb_simulator_code', 'n_clicks'),
#     Input('card_rb_attributes', 'n_clicks')
# )
# def return_rb_simulator_code(card_rb_simulator, card_rb_showcase,
#                             card_rb_simulator_code, card_rb_attributes):
#     if card_rb_simulator % 2 == 0:
#         return rb_simulator_navbar
#     elif card_rb_showcase % 2 == 0:
#         return html.Div([
#             # rb_navbar,
#             # rb_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_rb')
#     elif card_rb_simulator_code % 2 == 0:
#         return html.Div([
#             # rb_navbar,
#             # rb_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_rb')
#     elif card_rb_attributes % 2 == 0:
#         return html.Div([
#             # rb_navbar,
#             global_attributes
#         ], id='card_display_rb')
#     else:
#         return dash.no_update
# # Card ruby html.Ruby Simulator Code
# @dash.callback(
#     Output('card_display_rb', 'children'),
#     Input('card_rb_simulator', 'n_clicks'),
#     Input('card_rb_showcase', 'n_clicks'),
#     Input('card_rb_simulator_code', 'n_clicks'),
#     Input('card_rb_attributes', 'n_clicks')
# )
# def return_rb_simulator_code(card_rb_simulator, card_rb_showcase,
#                             card_rb_simulator_code, card_rb_attributes):
#     if card_rb_simulator % 2 == 0:
#         return rb_simulator_navbar
#     elif card_rb_showcase % 2 == 0:
#         return html.Div([
#             # rb_navbar,
#             # rb_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_rb')
#     elif card_rb_simulator_code % 2 == 0:
#         return html.Div([
#             # rb_navbar,
#             # rb_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_rb')
#     elif card_rb_attributes % 2 == 0:
#         return html.Div([
#             # rb_navbar,
#             global_attributes
#         ], id='card_display_rb')
#     else:
#         return dash.no_update
# # Card s html.S Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card samp html.Samp Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card script html.Script Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card search html.Search Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card section html.Section Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card select html.Select Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card slot html.Slot Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card small html.Small Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card source html.Source Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card span html.Span Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card strong html.Strong Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card style html.Style Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card sub html.Sub Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card summary html.Summary Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card sup html.Sup Simulator Code
# @dash.callback(
#     Output('card_display_s', 'children'),
#     Input('card_s_simulator', 'n_clicks'),
#     Input('card_s_showcase', 'n_clicks'),
#     Input('card_s_simulator_code', 'n_clicks'),
#     Input('card_s_attributes', 'n_clicks')
# )
# def return_s_simulator_code(card_s_simulator, card_s_showcase,
#                             card_s_simulator_code, card_s_attributes):
#     if card_s_simulator % 2 == 0:
#         return s_simulator_navbar
#     elif card_s_showcase % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             # s_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_s')
#     elif card_s_attributes % 2 == 0:
#         return html.Div([
#             # s_navbar,
#             global_attributes
#         ], id='card_display_s')
#     else:
#         return dash.no_update
# # Card table html.Table Simulator Code
# @dash.callback(
#     Output('card_display_t', 'children'),
#     Input('card_t_simulator', 'n_clicks'),
#     Input('card_t_showcase', 'n_clicks'),
#     Input('card_t_simulator_code', 'n_clicks'),
#     Input('card_t_attributes', 'n_clicks')
# )
# def return_t_simulator_code(card_t_simulator, card_t_showcase,
#                             card_t_simulator_code, card_t_attributes):
#     if card_t_simulator % 2 == 0:
#         return t_simulator_navbar
#     elif card_t_showcase % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_t_attributes % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             global_attributes
#         ], id='card_display_t')
#     else:
#         return dash.no_update
# # Card tbody html.tbody Simulator Code
# @dash.callback(
#     Output('card_display_t', 'children'),
#     Input('card_t_simulator', 'n_clicks'),
#     Input('card_t_showcase', 'n_clicks'),
#     Input('card_t_simulator_code', 'n_clicks'),
#     Input('card_t_attributes', 'n_clicks')
# )
# def return_t_simulator_code(card_t_simulator, card_t_showcase,
#                             card_t_simulator_code, card_t_attributes):
#     if card_t_simulator % 2 == 0:
#         return t_simulator_navbar
#     elif card_t_showcase % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_t_attributes % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             global_attributes
#         ], id='card_display_t')
#     else:
#         return dash.no_update
# # Card td html.Td Simulator Code
# @dash.callback(
#     Output('card_display_t', 'children'),
#     Input('card_t_simulator', 'n_clicks'),
#     Input('card_t_showcase', 'n_clicks'),
#     Input('card_t_simulator_code', 'n_clicks'),
#     Input('card_t_attributes', 'n_clicks')
# )
# def return_t_simulator_code(card_t_simulator, card_t_showcase,
#                             card_t_simulator_code, card_t_attributes):
#     if card_t_simulator % 2 == 0:
#         return t_simulator_navbar
#     elif card_t_showcase % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_t_attributes % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             global_attributes
#         ], id='card_display_t')
#     else:
#         return dash.no_update
# # Card template html.Template Simulator Code
# @dash.callback(
#     Output('card_display_t', 'children'),
#     Input('card_t_simulator', 'n_clicks'),
#     Input('card_t_showcase', 'n_clicks'),
#     Input('card_t_simulator_code', 'n_clicks'),
#     Input('card_t_attributes', 'n_clicks')
# )
# def return_t_simulator_code(card_t_simulator, card_t_showcase,
#                             card_t_simulator_code, card_t_attributes):
#     if card_t_simulator % 2 == 0:
#         return t_simulator_navbar
#     elif card_t_showcase % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_t_attributes % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             global_attributes
#         ], id='card_display_t')
#     else:
#         return dash.no_update
# # Card textarea html.Textarea Simulator Code
# @dash.callback(
#     Output('card_display_t', 'children'),
#     Input('card_t_simulator', 'n_clicks'),
#     Input('card_t_showcase', 'n_clicks'),
#     Input('card_t_simulator_code', 'n_clicks'),
#     Input('card_t_attributes', 'n_clicks')
# )
# def return_t_simulator_code(card_t_simulator, card_t_showcase,
#                             card_t_simulator_code, card_t_attributes):
#     if card_t_simulator % 2 == 0:
#         return t_simulator_navbar
#     elif card_t_showcase % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_t_attributes % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             global_attributes
#         ], id='card_display_t')
#     else:
#         return dash.no_update
# # Card tfoot html.Tfoot Simulator Code
# @dash.callback(
#     Output('card_display_t', 'children'),
#     Input('card_t_simulator', 'n_clicks'),
#     Input('card_t_showcase', 'n_clicks'),
#     Input('card_t_simulator_code', 'n_clicks'),
#     Input('card_t_attributes', 'n_clicks')
# )
# def return_t_simulator_code(card_t_simulator, card_t_showcase,
#                             card_t_simulator_code, card_t_attributes):
#     if card_t_simulator % 2 == 0:
#         return t_simulator_navbar
#     elif card_t_showcase % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_t_attributes % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             global_attributes
#         ], id='card_display_t')
#     else:
#         return dash.no_update
# # Card th html.Th Simulator Code
# @dash.callback(
#     Output('card_display_t', 'children'),
#     Input('card_t_simulator', 'n_clicks'),
#     Input('card_t_showcase', 'n_clicks'),
#     Input('card_t_simulator_code', 'n_clicks'),
#     Input('card_t_attributes', 'n_clicks')
# )
# def return_t_simulator_code(card_t_simulator, card_t_showcase,
#                             card_t_simulator_code, card_t_attributes):
#     if card_t_simulator % 2 == 0:
#         return t_simulator_navbar
#     elif card_t_showcase % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_t_attributes % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             global_attributes
#         ], id='card_display_t')
#     else:
#         return dash.no_update
# # Card thread html.Thread Simulator Code
# @dash.callback(
#     Output('card_display_t', 'children'),
#     Input('card_t_simulator', 'n_clicks'),
#     Input('card_t_showcase', 'n_clicks'),
#     Input('card_t_simulator_code', 'n_clicks'),
#     Input('card_t_attributes', 'n_clicks')
# )
# def return_t_simulator_code(card_t_simulator, card_t_showcase,
#                             card_t_simulator_code, card_t_attributes):
#     if card_t_simulator % 2 == 0:
#         return t_simulator_navbar
#     elif card_t_showcase % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_t_attributes % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             global_attributes
#         ], id='card_display_t')
#     else:
#         return dash.no_update
# # Card time html.Time Simulator Code
# @dash.callback(
#     Output('card_display_t', 'children'),
#     Input('card_t_simulator', 'n_clicks'),
#     Input('card_t_showcase', 'n_clicks'),
#     Input('card_t_simulator_code', 'n_clicks'),
#     Input('card_t_attributes', 'n_clicks')
# )
# def return_t_simulator_code(card_t_simulator, card_t_showcase,
#                             card_t_simulator_code, card_t_attributes):
#     if card_t_simulator % 2 == 0:
#         return t_simulator_navbar
#     elif card_t_showcase % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_t_attributes % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             global_attributes
#         ], id='card_display_t')
#     else:
#         return dash.no_update
# # Card title html.title Simulator Code
# @dash.callback(
#     Output('card_display_t', 'children'),
#     Input('card_t_simulator', 'n_clicks'),
#     Input('card_t_showcase', 'n_clicks'),
#     Input('card_t_simulator_code', 'n_clicks'),
#     Input('card_t_attributes', 'n_clicks')
# )
# def return_t_simulator_code(card_t_simulator, card_t_showcase,
#                             card_t_simulator_code, card_t_attributes):
#     if card_t_simulator % 2 == 0:
#         return t_simulator_navbar
#     elif card_t_showcase % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_t_attributes % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             global_attributes
#         ], id='card_display_t')
#     else:
#         return dash.no_update
# # Card tr html.Tr Simulator Code
# @dash.callback(
#     Output('card_display_t', 'children'),
#     Input('card_t_simulator', 'n_clicks'),
#     Input('card_t_showcase', 'n_clicks'),
#     Input('card_t_simulator_code', 'n_clicks'),
#     Input('card_t_attributes', 'n_clicks')
# )
# def return_t_simulator_code(card_t_simulator, card_t_showcase,
#                             card_t_simulator_code, card_t_attributes):
#     if card_t_simulator % 2 == 0:
#         return t_simulator_navbar
#     elif card_t_showcase % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_t_attributes % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             global_attributes
#         ], id='card_display_t')
#     else:
#         return dash.no_update
# # Card track html.Track Simulator Code
# @dash.callback(
#     Output('card_display_t', 'children'),
#     Input('card_t_simulator', 'n_clicks'),
#     Input('card_t_showcase', 'n_clicks'),
#     Input('card_t_simulator_code', 'n_clicks'),
#     Input('card_t_attributes', 'n_clicks')
# )
# def return_t_simulator_code(card_t_simulator, card_t_showcase,
#                             card_t_simulator_code, card_t_attributes):
#     if card_t_simulator % 2 == 0:
#         return t_simulator_navbar
#     elif card_t_showcase % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_s_simulator_code % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             # t_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_t')
#     elif card_t_attributes % 2 == 0:
#         return html.Div([
#             # t_navbar,
#             global_attributes
#         ], id='card_display_t')
#     else:
#         return dash.no_update
# # Card u html.U Simulator Code
# @dash.callback(
#     Output('card_display_u', 'children'),
#     Input('card_u_simulator', 'n_clicks'),
#     Input('card_u_showcase', 'n_clicks'),
#     Input('card_u_simulator_code', 'n_clicks'),
#     Input('card_u_attributes', 'n_clicks')
# )
# def return_u_simulator_code(card_u_simulator, card_u_showcase,
#                             card_u_simulator_code, card_u_attributes):
#     if card_u_simulator % 2 == 0:
#         return u_simulator_navbar
#     elif card_u_showcase % 2 == 0:
#         return html.Div([
#             # u_navbar,
#             # u_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_u')
#     elif card_u_simulator_code % 2 == 0:
#         return html.Div([
#             # u_navbar,
#             # u_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_u')
#     elif card_u_attributes % 2 == 0:
#         return html.Div([
#             # u_navbar,
#             global_attributes
#         ], id='card_display_u')
#     else:
#         return dash.no_update
# # Card ul html.Ul Simulator Code
# @dash.callback(
#     Output('card_display_u', 'children'),
#     Input('card_u_simulator', 'n_clicks'),
#     Input('card_u_showcase', 'n_clicks'),
#     Input('card_u_simulator_code', 'n_clicks'),
#     Input('card_u_attributes', 'n_clicks')
# )
# def return_u_simulator_code(card_u_simulator, card_u_showcase,
#                             card_u_simulator_code, card_u_attributes):
#     if card_u_simulator % 2 == 0:
#         return u_simulator_navbar
#     elif card_u_showcase % 2 == 0:
#         return html.Div([
#             # u_navbar,
#             # u_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_u')
#     elif card_u_simulator_code % 2 == 0:
#         return html.Div([
#             # u_navbar,
#             # u_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_u')
#     elif card_u_attributes % 2 == 0:
#         return html.Div([
#             # u_navbar,
#             global_attributes
#         ], id='card_display_u')
#     else:
#         return dash.no_update
# # Card var html.Var Simulator Code
# @dash.callback(
#     Output('card_display_var', 'children'),
#     Input('card_var_simulator', 'n_clicks'),
#     Input('card_var_showcase', 'n_clicks'),
#     Input('card_var_simulator_code', 'n_clicks'),
#     Input('card_var_attributes', 'n_clicks')
# )
# def return_var_simulator_code(card_var_simulator, card_var_showcase,
#                             card_var_simulator_code, card_var_attributes):
#     if card_var_simulator % 2 == 0:
#         return var_simulator_navbar
#     elif card_var_showcase % 2 == 0:
#         return html.Div([
#             # var_navbar,
#             # var_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_var')
#     elif card_var_simulator_code % 2 == 0:
#         return html.Div([
#             # var_navbar,
#             # var_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_var')
#     elif card_var_attributes % 2 == 0:
#         return html.Div([
#             # var_navbar,
#             global_attributes
#         ], id='card_display_var')
#     else:
#         return dash.no_update
# # Card video html.Video Simulator Code
# @dash.callback(
#     Output('card_display_var', 'children'),
#     Input('card_var_simulator', 'n_clicks'),
#     Input('card_var_showcase', 'n_clicks'),
#     Input('card_var_simulator_code', 'n_clicks'),
#     Input('card_var_attributes', 'n_clicks')
# )
# def return_var_simulator_code(card_var_simulator, card_var_showcase,
#                             card_var_simulator_code, card_var_attributes):
#     if card_var_simulator % 2 == 0:
#         return var_simulator_navbar
#     elif card_var_showcase % 2 == 0:
#         return html.Div([
#             # var_navbar,
#             # var_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_var')
#     elif card_var_simulator_code % 2 == 0:
#         return html.Div([
#             # var_navbar,
#             # var_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_var')
#     elif card_var_attributes % 2 == 0:
#         return html.Div([
#             # var_navbar,
#             global_attributes
#         ], id='card_display_var')
#     else:
#         return dash.no_update
# # Card wbr html.Wbr Simulator Code
# @dash.callback(
#     Output('card_display_wbr', 'children'),
#     Input('card_wbr_simulator', 'n_clicks'),
#     Input('card_wbr_showcase', 'n_clicks'),
#     Input('card_wbr_simulator_code', 'n_clicks'),
#     Input('card_wbr_attributes', 'n_clicks')
# )
# def return_wbr_simulator_code(card_wbr_simulator, card_wbr_showcase,
#                             card_wbr_simulator_code, card_wbr_attributes):
#     if card_wbr_simulator % 2 == 0:
#         return wbr_simulator_navbar
#     elif card_wbr_showcase % 2 == 0:
#         return html.Div([
#             # wbr_navbar,
#             # wbr_showcase
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_wbr')
#     elif card_wbr_simulator_code % 2 == 0:
#         return html.Div([
#             # wbr_navbar,
#             # wbr_example_code
#         ], style={'margin': 0,
#                   'padding': 0}, id='card_display_wbr')
#     elif card_wbr_attributes % 2 == 0:
#         return html.Div([
#             # wbr_navbar,
#             global_attributes
#         ], id='card_display_wbr')
#     else:
#         return dash.no_update