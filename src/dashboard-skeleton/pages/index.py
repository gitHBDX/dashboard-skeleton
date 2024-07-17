import dash
import dash_mantine_components as dmc


layout = dmc.Group(
    [
        dmc.Stack(
            [
                dmc.Paper(
                    [
                        dmc.Title("Hello World", order=1),
                        dmc.Text("This is a text", size="xs"),
                    ]
                ),
                dmc.Paper(
                    [
                        dmc.Stack(
                            [
                                dmc.Text("The most useful elements are dmc.Stack, dmc.Group and dmc.Paper", size="xs"),
                                dmc.Text("dmc.Stack is a vertical stack of elements", size="xs", c="blue"),
                                dmc.Text("dmc.Group is a horizontal stack of elements", size="xs", c="green"),
                                dmc.Text("dmc.Paper is a box with a shadow", size="xs", c="dimmed"),
                            ]
                        )
                    ]
                ),
            ]
        ),
        dmc.Stack(
            [
                dmc.Paper(
                    [
                        dmc.TextInput("This is a text input", label="Easy inputs", description="This is a description"),
                        dmc.RadioGroup(
                            [
                                dmc.Radio(l, value=k)
                                for k, l in [["react", "React"], ["ng", "Angular"], ["svelte", "Svelte"], ["vue", "Vue"]]
                            ],
                            id="radiogroup-simple",
                            value="react",
                            label="Select your favorite framework/library",
                            size="sm",
                            mt=10,
                        ),
                    ],
                ),
                dmc.Group(
                    [
                        dmc.Card(
                            [
                                dmc.CardSection(
                                    dmc.Image(
                                        src="https://images.unsplash.com/photo-1527004013197-933c4bb611b3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=720&q=80",
                                        h=160,
                                    )
                                ),
                                dmc.Group(
                                    [
                                        dmc.Text("Norway Fjord Adventures", w=500),
                                        dmc.Badge("On Sale", c="red", variant="light"),
                                    ],
                                    pos="apart",
                                    mt="md",
                                    mb="xs",
                                ),
                                dmc.Text(
                                    "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                    size="sm",
                                    c="dimmed",
                                ),
                                dmc.Button(
                                    "Book classic tour now",
                                    variant="light",
                                    c="blue",
                                    fullWidth=True,
                                    mt="md",
                                    radius="md",
                                ),
                            ],
                            withBorder=True,
                            shadow="sm",
                            radius="md",
                            style={"maxWidth": "20em"},
                        ),
                        dmc.Card(
                            [
                                dmc.CardSection(
                                    dmc.Image(
                                        src="https://images.unsplash.com/photo-1527004013197-933c4bb611b3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=720&q=80",
                                        h=160,
                                    )
                                ),
                                dmc.Group(
                                    [
                                        dmc.Text("Norway Fjord Adventures", w=500),
                                        dmc.Badge("On Sale", c="red", variant="light"),
                                    ],
                                    pos="apart",
                                    mt="md",
                                    mb="xs",
                                ),
                                dmc.Text(
                                    "With Fjord Tours you can explore more of the magical fjord landscapes with tours and activities on and around the fjords of Norway",
                                    size="sm",
                                    c="dimmed",
                                ),
                                dmc.Button(
                                    "Book classic tour now",
                                    variant="light",
                                    c="blue",
                                    fullWidth=True,
                                    mt="md",
                                    radius="md",
                                ),
                            ],
                            withBorder=True,
                            shadow="sm",
                            radius="md",
                            style={"maxWidth": "20em"}
                        ),
                    ]
                ),
            ], style={"maxWidth": "40em"}
        ),
    ]
)


dash.register_page("example", layout=layout, path="/", title="Example - {app_name}")
