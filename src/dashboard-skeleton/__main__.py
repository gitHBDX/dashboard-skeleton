from dash_prometheus import add_middleware

#  dash_prometheus has to be imported before dash

from argparse import ArgumentParser
from pathlib import Path
import random

import dash
import dash_mantine_components as dmc
import dash_hummingbird_components as dhc
import diskcache
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import yaml
from dash import html

stylesheets = [
    "https://unpkg.com/@mantine/dates@7/styles.css",
    "https://unpkg.com/@mantine/code-highlight@7/styles.css",
    "https://unpkg.com/@mantine/charts@7/styles.css",
    "https://unpkg.com/@mantine/carousel@7/styles.css",
    "https://unpkg.com/@mantine/notifications@7/styles.css",
    "https://unpkg.com/@mantine/nprogress@7/styles.css",
    "https://fonts.googleapis.com/css2?family=Work+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap",
]


plotly_template = yaml.load((Path(__file__).parent / "assets" / "plotly_template.yaml").read_text(), Loader=yaml.FullLoader)
pio.templates["hbdx"] = go.layout.Template(plotly_template)
pio.templates.default = "plotly_white+hbdx"
px.defaults.template = "plotly_white+hbdx"

app_name = "{app_name}"
dash._dash_renderer._set_react_version('18.2.0')

app = dash.Dash(
    f"{app_name}",
    background_callback_manager=dash.DiskcacheManager(diskcache.Cache("./cache")),
    title=f"{app_name}",
    assets_folder=Path(__file__).parent / "assets",
    pages_folder=Path(__file__).parent / "pages",
    external_stylesheets=stylesheets,
    use_pages=True,
)
application = app.server

add_middleware(app)

dhc.make_url_params_callback()


app.layout = dmc.MantineProvider(
    theme={
        "white": "#f2f2f2",
        "black": "#212121",
        "colors": {
            "blue": ["#ebf7ff", "#d6ebfa", "#a6d6f7", "#75c0f6", "#53aef5", "#41a2f5", "#389cf6", "#2c88db", "#2079c4", "#0068ad"],
            "green": ["#edfce9", "#e0f4d8", "#c1e6b3", "#a0d88b", "#84cd69", "#72c553", "#67c247", "#56aa38", "#4a972e", "#3b8322"],
        },
        "primaryColor": "green",
        "defaultRadius": "xs",
        "fontFamily": "Work Sans, sans-serif",
        "headings": {
            "sizes": {
                "h1": {
                    "fontSize": "30px",
                },
            },
        },
        "components": {
            "Paper": {
                "defaultProps": {
                    "bg": "white",
                    "withBorder": True,
                    "p": "md",
                    "shadow": "xs",
                },

            }}
    },
    # inherit=True, #NOTE these do not work in 1.4.0
    # withGlobalStyles=True,
    # withNormalizeCSS=True,
    children=dmc.AppShell(
        children = [
            dmc.AppShellHeader(
                [
                    dmc.Group(
                        [
                            dmc.Image(src=app.get_asset_url("favicon.ico"), h=50, w="auto"),
                            html.Div(
                                [
                                    dmc.Title(f"{app_name}", order=1),
                                    dmc.Text("{description}", size="xs"),
                                ]
                            ),
                        ],
                        gap="lg",
                        align="center",
                    )
                ],
                # p="md",
                # h="auto",
                # bg="white",
                # withBorder=True,
            ),
            dmc.AppShellMain(children=[
                dash.page_container
            ], style={"flexGrow": 1, "marginTop": "80px"}, px="md", align="start"), 
            dmc.AppShellFooter(
                [
                    dmc.Container(
                        [
                            dmc.Stack(
                                [
                                    html.Div(
                                        [
                                            dmc.Image(src=app.get_asset_url("Logo-Hummingbird.png"), h="40px", w="auto"),
                                        ]
                                    ),
                                    dmc.Group(
                                        [
                                            dmc.Text("© Hummingbird Diagnostics GmbH", c="gray", size="xs"),
                                            dmc.Text("Im Neuenheimer Feld 583", c="gray", size="xs"),
                                            dmc.Text("D-69120 Heidelberg", c="gray", size="xs"),
                                        ],
                                        gap="xs",
                                    ),
                                    dmc.Group([
                                            dmc.Text("Germany Telephone: +49 (0) 6221 91433-10", c="gray", size="xs"),
                                            dmc.Text("Fax: +49 (0) 6221 91433-12", c="gray", size="xs"),
                                            dmc.Text("E-mail: info (at) hb-dx.com", c="gray", size="xs"),
                                        ],
                                        gap="xs",
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
                # p="md",
                # h="auto",
                # mt="md",
                # bg="white",
                # withBorder=True,
            ),
        ],
        header={"height": 70, "background": "white"}, #TODO these should not be magic numbers
        footer={"height": 150}, #TODO these should not be magic numbers
        padding="xl",
        zIndex=1400,
    ),
)

def main():
    parser = ArgumentParser()
    parser.add_argument("--prod", action="store_true")
    parser.add_argument("--port", type=int)

    args = parser.parse_args()

    port = args.port
    if not port:
        port = random.randint(8000, 9000)
        print(f"Running on random port {{port}}")
    
    app.run(
        debug=not args.prod,
        port=port,
        host="0.0.0.0",
    )

if __name__ == "__main__":
    main()