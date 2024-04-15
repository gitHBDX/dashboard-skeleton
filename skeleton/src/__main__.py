from dash_prometheus import add_middleware

#  dash_prometheus has to be imported before dash

from argparse import ArgumentParser
from pathlib import Path

import dash
import dash_mantine_components as dmc
import dash_hummingbird_components as dhc
import diskcache
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import yaml
from dash import html


plotly_template = yaml.load((Path(__file__).parent / "assets" / "plotly_template.yaml").read_text(), Loader=yaml.FullLoader)
pio.templates["hbdx"] = go.layout.Template(plotly_template)
pio.templates.default = "plotly_white+hbdx"
px.defaults.template = "plotly_white+hbdx"


app = dash.Dash(
    "{app_name}",
    background_callback_manager=dash.DiskcacheManager(diskcache.Cache("./cache")),
    title="{app_name}",
    assets_folder=Path(__file__).parent / "assets",
    pages_folder=Path(__file__).parent / "pages",
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Work+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap",
    ],
    use_pages=True,
)
server = app.server

add_middleware(app)

dhc.make_url_params_callback()

app.layout = dmc.MantineProvider(
    theme={{
        "white": "#f2f2f2",
        "black": "#212121",
        "colors": {{
            "blue": ["#ebf7ff", "#d6ebfa", "#a6d6f7", "#75c0f6", "#53aef5", "#41a2f5", "#389cf6", "#2c88db", "#2079c4", "#0068ad"],
            "green": ["#edfce9", "#e0f4d8", "#c1e6b3", "#a0d88b", "#84cd69", "#72c553", "#67c247", "#56aa38", "#4a972e", "#3b8322"],
        }},
        "primaryColor": "green",
        "defaultRadius": "xs",
        "fontFamily": "Work Sans, sans-serif",
        "headings": {{
            "sizes": {{
                "h1": {{
                    "fontSize": "30px",
                }},
            }},
        }},
        "components": {{
            "Paper": {{
                "defaultProps": {{
                    "bg": "white",
                    "withBorder": True,
                    "p": "md",
                    "shadow": "xs",
                }},

            }}}}
    }},
    inherit=True,
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=dmc.Stack(
        [
            dmc.Header(
                [
                    dmc.Group(
                        [
                            dmc.Image(src=app.get_asset_url("favicon.ico"), height=50, width="auto"),
                            html.Div(
                                [
                                    dmc.Title("{app_name}", order=1),
                                    dmc.Text("{description}", size="xs"),
                                ]
                            ),
                        ],
                        spacing="lg",
                        align="center",
                    )
                ],
                p="md",
                height="auto",
                bg="white",
                withBorder=True,
            ),
            dmc.Group([
                dash.page_container
            ], align="start", style={{"flexGrow": 1}}, px="md"),
            dmc.Footer(
                [
                    dmc.Container(
                        [
                            dmc.Stack(
                                [
                                    html.Div(
                                        [
                                            dmc.Image(src=app.get_asset_url("Logo-Hummingbird.png"), height="40px", width="auto"),
                                        ]
                                    ),
                                    dmc.Group(
                                        [
                                            dmc.Text("© Hummingbird Diagnostics GmbH", color="gray", size="xs"),
                                            dmc.Text("Im Neuenheimer Feld 583", color="gray", size="xs"),
                                            dmc.Text("D-69120 Heidelberg", color="gray", size="xs"),
                                        ],
                                        spacing="xs",
                                    ),
                                    dmc.Group([
                                            dmc.Text("Germany Telephone: +49 (0) 6221 91433-10", color="gray", size="xs"),
                                            dmc.Text("Fax: +49 (0) 6221 91433-12", color="gray", size="xs"),
                                            dmc.Text("E-mail: info (at) hb-dx.com", color="gray", size="xs"),
                                        ],
                                        spacing="xs",
                                    ),
                                    dmc.Group(
                                        [
                                            dmc.Anchor("Imprint", href="https://www.hummingbird-diagnostics.com/imprint/"),
                                            dmc.Anchor("Privacy Policy", href="https://www.hummingbird-diagnostics.com/privacy-policy/"),
                                        ]
                                    ),
                                ]
                            ),
                        ],
                    ),
                ],
                p="md",
                height="auto",
                mt="md",
                bg="white",
                withBorder=True,
            ),
        ],
        mih="100vh",
    ),
)

def main():
    parser = ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--port", type=int, default={port})

    args = parser.parse_args()

    app.run(
        debug=args.debug,
        port=args.port,
        host="0.0.0.0",
    )

if __name__ == "__main__":
    main()