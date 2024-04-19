import flet
from flet import (
    AppBar,
    Column,
    Container,
    ElevatedButton,
    InputFilter,
    MainAxisAlignment,
    Page,
    Row,
    Text,
    TextField,
    UserControl,
)


class BinaryCalculator(UserControl):
    def build(self):

        Page.appbar = AppBar(
            title=Text("Binary Calculator"),
        )

        # Variable of controls
        self.txt_hexadecimal = TextField(
            label="Hexadecimal",
            width=350,
            rtl=True,
            input_filter=InputFilter(regex_string=r"[0-9/aA-hH]"),
        )  # noqa: F841
        self.txt_decimal = TextField(
            label="Decimal",
            width=350,
            rtl=True,
            input_filter=InputFilter(regex_string=r"[0-9]"),
        )  # noqa: F841
        self.txt_octal = TextField(
            label="Octal",
            width=350,
            rtl=True,
            input_filter=InputFilter(regex_string=r"[0-7]"),
        )  # noqa: F841
        self.txt_binary = TextField(
            label="Binary",
            width=350,
            rtl=True,
            input_filter=InputFilter(regex_string=r"[0-1]"),
        )  # noqa: F841

        return Container(
            content=Column(
                controls=[
                    Row(
                        controls=[self.txt_hexadecimal],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[self.txt_decimal],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(controls=[self.txt_octal], alignment=MainAxisAlignment.CENTER),
                    Row(
                        controls=[self.txt_binary],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                " H ",
                                width=80,
                            ),
                            ElevatedButton(
                                " G ",
                                width=80,
                            ),
                            ElevatedButton(
                                " F ",
                                width=80,
                            ),
                            ElevatedButton(
                                "A/C",
                                width=80,
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                " E ",
                                width=80,
                            ),
                            ElevatedButton(
                                " D ",
                                width=80,
                            ),
                            ElevatedButton(
                                " C ",
                                width=80,
                            ),
                            ElevatedButton(
                                " B ",
                                width=80,
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                " A ",
                                width=80,
                            ),
                            ElevatedButton(
                                " 9 ",
                                width=80,
                            ),
                            ElevatedButton(
                                " 8 ",
                                width=80,
                            ),
                            ElevatedButton(
                                " 7 ",
                                width=80,
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                " 6 ",
                                width=80,
                            ),
                            ElevatedButton(
                                " 5 ",
                                width=80,
                            ),
                            ElevatedButton(
                                " 4 ",
                                width=80,
                            ),
                            ElevatedButton(
                                " 3 ",
                                width=80,
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                " 2 ",
                                width=80,
                            ),
                            ElevatedButton(
                                " 1 ",
                                width=80,
                            ),
                            ElevatedButton(
                                " 0 ",
                                width=80,
                            ),
                            ElevatedButton(
                                " = ",
                                width=80,
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ]
            )
        )


def main(page: Page):
    # Configuring the personalize of Page desktop
    page.title = "Binary Calculator"
    page.window_height = 600
    page.window_width = 600
    page.window_max_height = 700
    page.window_max_width = 700
    page.window_min_height = 575
    page.window_min_width = 400
    page.window_maximizable = False

    calc = BinaryCalculator()

    page.add(calc)


flet.app(target=main)
