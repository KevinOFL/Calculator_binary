import flet
from flet import (
    AppBar,
    Checkbox,
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
            value="0",
            data="hexadecimal",
            disabled=True,
        )  # noqa: F841
        self.txt_decimal = TextField(
            label="Decimal",
            width=350,
            rtl=True,
            input_filter=InputFilter(regex_string=r"[0-9]"),
            value="0",
            data="decimal",
            disabled=True,
        )  # noqa: F841
        self.txt_octal = TextField(
            label="Octal",
            width=350,
            rtl=True,
            input_filter=InputFilter(regex_string=r"[0-7]"),
            value="0",
            data="octal",
            disabled=True,
        )  # noqa: F841
        self.txt_binary = TextField(
            label="Binary",
            width=350,
            rtl=True,
            input_filter=InputFilter(regex_string=r"[0-1]"),
            value="0",
            data="binary",
            disabled=True,
        )  # noqa: F841

        self.select_hexadecimal = Checkbox(
            data="Select_hexadecimal",
            on_change=self.disableControlls,
        )
        self.select_decimal = Checkbox(
            data="Select_decimal",
            on_change=self.disableControlls,
        )
        self.select_octal = Checkbox(
            data="Select_octal",
            on_change=self.disableControlls,
        )
        self.select_binary = Checkbox(
            data="Select_binary",
            on_change=self.disableControlls,
        )

        return Container(
            content=Column(
                controls=[
                    Row(
                        controls=[self.txt_hexadecimal, self.select_hexadecimal],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[self.txt_decimal, self.select_decimal],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[self.txt_octal, self.select_octal],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[self.txt_binary, self.select_binary],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="A/C",
                                width=80,
                                data="clear",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="F",
                                width=80,
                                data="F",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="E",
                                width=80,
                                data="E",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="<-",
                                width=80,
                                data="remove",
                                on_click=self.button_clicked,
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="D",
                                width=80,
                                data="D",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="C",
                                width=80,
                                data="C",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="B",
                                width=80,
                                data="B",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="A",
                                width=80,
                                data="A",
                                on_click=self.button_clicked,
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="9",
                                width=80,
                                data="9",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="8",
                                width=80,
                                data="8",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="7",
                                width=80,
                                data="7",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="6",
                                width=80,
                                data="6",
                                on_click=self.button_clicked,
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="5",
                                width=80,
                                data="5",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="4",
                                width=80,
                                data="4",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="3",
                                width=80,
                                data="3",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="2",
                                width=80,
                                data="2",
                                on_click=self.button_clicked,
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                width=80,
                                data="1",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="0",
                                width=80,
                                data="0",
                                on_click=self.button_clicked,
                            ),
                            ElevatedButton(
                                text="=",
                                width=170,
                                data="=",
                                on_click=self.button_clicked,
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ]
            )
        )

    def button_clicked(self, e): ...

    def disableControlls(self, e):
        data = e.control.data
        print(data)

        if data == "Select_hexadecimal":
            if self.select_decimal.disabled is False:
                self.select_binary.disabled = True
                self.select_octal.disabled = True
                self.select_decimal.disabled = True
                self.txt_hexadecimal.disabled = False
            elif self.select_decimal.disabled is True:
                self.select_binary.disabled = False
                self.select_octal.disabled = False
                self.select_decimal.disabled = False
                self.txt_hexadecimal.disabled = True
        elif data == "Select_decimal":
            if self.select_octal.disabled is False:
                self.select_binary.disabled = True
                self.select_octal.disabled = True
                self.select_hexadecimal.disabled = True
                self.txt_decimal.disabled = False
            elif self.select_octal.disabled is True:
                self.select_binary.disabled = False
                self.select_octal.disabled = False
                self.select_hexadecimal.disabled = False
                self.txt_decimal.disabled = True
        elif data == "Select_octal":
            if self.select_binary.disabled is False:
                self.select_binary.disabled = True
                self.select_decimal.disabled = True
                self.select_hexadecimal.disabled = True
                self.txt_octal.disabled = False
            elif self.select_binary.disabled is True:
                self.select_binary.disabled = False
                self.select_decimal.disabled = False
                self.select_hexadecimal.disabled = False
                self.txt_octal.disabled = True
        elif data == "Select_binary":
            if self.select_hexadecimal.disabled is False:
                self.select_octal.disabled = True
                self.select_decimal.disabled = True
                self.select_hexadecimal.disabled = True
                self.txt_binary.disabled = False
            elif self.select_hexadecimal.disabled is True:
                self.select_octal.disabled = False
                self.select_decimal.disabled = False
                self.select_hexadecimal.disabled = False
                self.txt_binary.disabled = True

        self.update()


def main(page: Page):
    # Configuring the personalize of Page desktop
    page.title = "Binary Calculator"
    page.window_height = 600
    page.window_width = 600
    page.window_max_height = 700
    page.window_max_width = 700
    page.window_min_height = 575
    page.window_min_width = 450
    page.window_maximizable = False

    calc = BinaryCalculator()

    page.add(calc)


flet.app(target=main)
