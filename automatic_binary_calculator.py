import flet
from flet import (
    Checkbox,
    Column,
    Container,
    ElevatedButton,
    InputFilter,
    MainAxisAlignment,
    Page,
    Row,
    TextField,
    UserControl,
)


class BinaryCalculator(UserControl):
    def build(self):
        # Variable of controls
        self.txt_hexadecimal = TextField(
            label="Hexadecimal",
            width=350,
            rtl=True,
            input_filter=InputFilter(regex_string=r"[0-9/aA-fF]"),
            value="0",
            data="hexadecimal",
            disabled=True,
            on_change=self.calculateValue,
            on_submit=self.calculateValue,
        )  # noqa: F841
        self.txt_decimal = TextField(
            label="Decimal",
            width=350,
            rtl=True,
            input_filter=InputFilter(regex_string=r"[0-9]"),
            value="0",
            data="decimal",
            disabled=True,
            on_change=self.calculateValue,
            on_submit=self.calculateValue,
        )  # noqa: F841
        self.txt_octal = TextField(
            label="Octal",
            width=350,
            rtl=True,
            input_filter=InputFilter(regex_string=r"[0-7]"),
            value="0",
            data="octal",
            disabled=True,
            on_change=self.calculateValue,
            on_submit=self.calculateValue,
        )  # noqa: F841
        self.txt_binary = TextField(
            label="Binary",
            width=350,
            rtl=True,
            input_filter=InputFilter(regex_string=r"[0-1]"),
            value="0",
            data="binary",
            disabled=True,
            on_change=self.calculateValue,
            on_submit=self.calculateValue,
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
                                on_click=self.deleteOrClearAll,
                            ),
                            ElevatedButton(
                                text="F",
                                width=80,
                                data="F",
                                on_click=self.button_of_value_clicked,
                            ),
                            ElevatedButton(
                                text="E",
                                width=80,
                                data="E",
                                on_click=self.button_of_value_clicked,
                            ),
                            ElevatedButton(
                                text="<-",
                                width=80,
                                data="delete",
                                on_click=self.deleteOrClearAll,
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
                                on_click=self.button_of_value_clicked,
                            ),
                            ElevatedButton(
                                text="C",
                                width=80,
                                data="C",
                                on_click=self.button_of_value_clicked,
                            ),
                            ElevatedButton(
                                text="B",
                                width=80,
                                data="B",
                                on_click=self.button_of_value_clicked,
                            ),
                            ElevatedButton(
                                text="A",
                                width=80,
                                data="A",
                                on_click=self.button_of_value_clicked,
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
                                on_click=self.button_of_value_clicked,
                            ),
                            ElevatedButton(
                                text="8",
                                width=80,
                                data="8",
                                on_click=self.button_of_value_clicked,
                            ),
                            ElevatedButton(
                                text="7",
                                width=80,
                                data="7",
                                on_click=self.button_of_value_clicked,
                            ),
                            ElevatedButton(
                                text="6",
                                width=80,
                                data="6",
                                on_click=self.button_of_value_clicked,
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
                                on_click=self.button_of_value_clicked,
                            ),
                            ElevatedButton(
                                text="4",
                                width=80,
                                data="4",
                                on_click=self.button_of_value_clicked,
                            ),
                            ElevatedButton(
                                text="3",
                                width=80,
                                data="3",
                                on_click=self.button_of_value_clicked,
                            ),
                            ElevatedButton(
                                text="2",
                                width=80,
                                data="2",
                                on_click=self.button_of_value_clicked,
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
                                on_click=self.button_of_value_clicked,
                            ),
                            ElevatedButton(
                                text="0",
                                width=80,
                                data="0",
                                on_click=self.button_of_value_clicked,
                            ),
                            ElevatedButton(
                                text="=",
                                width=170,
                                data="equal",
                                on_click=self.calculateValue,
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ]
            )
        )

    def button_of_value_clicked(self, e):
        data = e.control.data

        if (
            self.data_of_selection_textbox == "Select_hexadecimal"
            and self.state == 1
            and data
            in (
                "F",
                "E",
                "D",
                "C",
                "B",
                "A",
                "9",
                "8",
                "7",
                "6",
                "5",
                "4",
                "3",
                "2",
                "1",
                "0",
            )
        ):
            self.txt_hexadecimal.value = self.txt_hexadecimal.value + data
        elif (
            self.data_of_selection_textbox == "Select_decimal"
            and self.state == 1
            and self.state == 1
            and data
            in (
                "9",
                "8",
                "7",
                "6",
                "5",
                "4",
                "3",
                "2",
                "1",
                "0",
            )
        ):
            self.txt_decimal.value = self.txt_decimal.value + data
        elif (
            self.data_of_selection_textbox == "Select_octal"
            and self.state == 1
            and data
            in (
                "7",
                "6",
                "5",
                "4",
                "3",
                "2",
                "1",
                "0",
            )
        ):
            self.txt_octal.value = self.txt_octal.value + data
        elif (
            self.data_of_selection_textbox == "Select_binary"
            and self.state == 1
            and data in ("1", "0")
        ):
            self.txt_binary.value = self.txt_binary.value + data

        self.update()

    def disableControlls(self, e):
        self.state = 0
        self.data_of_selection_textbox = e.control.data

        if self.data_of_selection_textbox == "Select_hexadecimal":
            if self.select_decimal.disabled is False:
                self.state = 1
                self.select_binary.disabled = True
                self.select_octal.disabled = True
                self.select_decimal.disabled = True
                self.txt_hexadecimal.disabled = False
            elif self.select_decimal.disabled is True:
                self.state = 0
                self.select_binary.disabled = False
                self.select_octal.disabled = False
                self.select_decimal.disabled = False
                self.txt_hexadecimal.disabled = True
        elif self.data_of_selection_textbox == "Select_decimal":
            if self.select_octal.disabled is False:
                self.state = 1
                self.select_binary.disabled = True
                self.select_octal.disabled = True
                self.select_hexadecimal.disabled = True
                self.txt_decimal.disabled = False
            elif self.select_octal.disabled is True:
                self.state = 0
                self.select_binary.disabled = False
                self.select_octal.disabled = False
                self.select_hexadecimal.disabled = False
                self.txt_decimal.disabled = True
        elif self.data_of_selection_textbox == "Select_octal":
            if self.select_binary.disabled is False:
                self.state = 1
                self.select_binary.disabled = True
                self.select_decimal.disabled = True
                self.select_hexadecimal.disabled = True
                self.txt_octal.disabled = False
            elif self.select_binary.disabled is True:
                self.state = 0
                self.select_binary.disabled = False
                self.select_decimal.disabled = False
                self.select_hexadecimal.disabled = False
                self.txt_octal.disabled = True
        elif self.data_of_selection_textbox == "Select_binary":
            if self.select_hexadecimal.disabled is False:
                self.state = 1
                self.select_octal.disabled = True
                self.select_decimal.disabled = True
                self.select_hexadecimal.disabled = True
                self.txt_binary.disabled = False
            elif self.select_hexadecimal.disabled is True:
                self.state = 0
                self.select_octal.disabled = False
                self.select_decimal.disabled = False
                self.select_hexadecimal.disabled = False
                self.txt_binary.disabled = True

        self.update()

    def calculateValue(self, e):
        convert_decimal = 0
        convert_hexadecimal = 0
        convert_octal = 0
        convert_binary = 0
        if self.data_of_selection_textbox == "Select_hexadecimal":
            if self.txt_hexadecimal.value == "":
                self.txt_hexadecimal.value = "0"
            value_of_text_box = self.txt_hexadecimal.value
            try:
                convert_decimal = int(value_of_text_box, 16)
                self.txt_decimal.value = str(convert_decimal)
                convert_octal = oct(convert_decimal)[2:]
                self.txt_octal.value = str(convert_octal)
                convert_binary = bin(convert_decimal)[2:]
                self.txt_binary.value = str(convert_binary)
            except ValueError:
                self.txt_binary.value = "0"
                self.txt_octal.value = "0"
                self.txt_decimal.value = "0"
                self.txt_hexadecimal.value = ""
        elif self.data_of_selection_textbox == "Select_decimal":
            if self.txt_decimal.value == "":
                self.txt_decimal.value = "0"
            value_of_text_box = int(self.txt_decimal.value)
            try:
                convert_hexadecimal = hex(value_of_text_box)[2:]
                self.txt_hexadecimal.value = str(convert_hexadecimal).upper()
                convert_octal = oct(value_of_text_box)[2:]
                self.txt_octal.value = str(convert_octal)
                convert_binary = bin(value_of_text_box)[2:]
                self.txt_binary.value = str(convert_binary)
            except ValueError:
                self.txt_binary.value = "0"
                self.txt_octal.value = "0"
                self.txt_decimal.value = ""
                self.txt_hexadecimal.value = "0"
        elif self.data_of_selection_textbox == "Select_octal":
            if self.txt_octal.value == "":
                self.txt_octal.value = "0"
            value_of_text_box = self.txt_octal.value
            try:
                convert_decimal = int(value_of_text_box, 8)
                self.txt_decimal.value = str(convert_decimal)
                convert_hexadecimal = hex(convert_decimal)[2:]
                self.txt_hexadecimal.value = str(convert_hexadecimal).upper()
                convert_binary = bin(convert_decimal)[2:]
                self.txt_binary.value = str(convert_binary)
            except ValueError:
                self.txt_binary.value = "0"
                self.txt_octal.value = ""
                self.txt_decimal.value = "0"
                self.txt_hexadecimal.value = "0"
        elif self.data_of_selection_textbox == "Select_binary":
            if self.txt_binary.value == "":
                self.txt_binary.value = "0"
            value_of_text_box = self.txt_binary.value
            try:
                convert_decimal = int(value_of_text_box, 2)
                self.txt_decimal.value = str(convert_decimal)
                convert_hexadecimal = hex(convert_decimal)[2:]
                self.txt_hexadecimal.value = str(convert_hexadecimal).upper()
                convert_octal = oct(convert_decimal)[2:]
                self.txt_octal.value = str(convert_octal)
            except ValueError:
                self.txt_binary.value = ""
                self.txt_octal.value = "0"
                self.txt_decimal.value = "0"
                self.txt_hexadecimal.value = "0"
        else:
            self.update()

        self.update()

    def deleteOrClearAll(self, e):
        data = e.control.data
        if data == "delete" and self.txt_hexadecimal.value != "0":
            self.txt_hexadecimal.value = str(self.txt_hexadecimal.value)[:-1]
        elif data == "delete" and self.txt_decimal.value != "0":
            self.txt_decimal.value = str(self.txt_decimal.value)[:-1]
        elif data == "delete" and self.txt_octal.value != "0":
            self.txt_octal.value = str(self.txt_octal.value)[:-1]
        elif data == "delete" and self.txt_binary.value != "0":
            self.txt_binary.value = str(self.txt_binary.value)[:-1]
        else:
            self.txt_binary.value = "0"
            self.txt_octal.value = "0"
            self.txt_decimal.value = "0"
            self.txt_hexadecimal.value = "0"
        self.update()


def main(page: Page):
    # Configuring the personalize of Page desktop
    page.title = "Binary Calculator"
    page.window_height = 570
    page.window_width = 460
    page.window_max_height = 620
    page.window_max_width = 500
    page.window_min_height = 560
    page.window_min_width = 440
    page.window_maximizable = False

    calc = BinaryCalculator()

    page.add(calc)


flet.app(target=main)
