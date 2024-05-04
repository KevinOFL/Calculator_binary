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
        
        try:
            if self.data_of_selection_textbox == "Select_hexadecimal" and self.state == 1 and data in (
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
            ):
                self.txt_hexadecimal.value = self.txt_hexadecimal.value + data
            elif self.data_of_selection_textbox == "Select_decimal" and self.state == 1 and data in (
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
            ):
                self.txt_decimal.value = self.txt_decimal.value + data
            elif self.data_of_selection_textbox == "Select_octal" and self.state == 1 and data in (
                "7",
                "6",
                "5",
                "4",
                "3",
                "2",
                "1",
                "0",
            ):
                self.txt_octal.value = self.txt_octal.value + data
            elif self.data_of_selection_textbox == "Select_binary" and self.state == 1 and data in ("1", "0"):
                self.txt_binary.value = self.txt_binary.value + data
        except AttributeError:
            self.txt_binary.value = "0"
            self.txt_octal.value = "0"
            self.txt_decimal.value = "0"
            self.txt_hexadecimal.value = "0"
            
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
        if self.data_of_selection_textbox == "Select_hexadecimal":
            if self.txt_hexadecimal.value == "":
                self.txt_hexadecimal.value = "0"
            value_of_text_box = self.txt_hexadecimal.value
            try:
                self.txt_decimal.value = self.calculateValuesForTheRespectivePower(
                    value_of_text_box
                )
                self.txt_octal.value = self.calculateOctalValue(self.txt_decimal.value)
                self.txt_binary.value = self.calculateBinaryValue(
                    self.txt_decimal.value
                )
            except ValueError:
                self.txt_binary.value = "0"
                self.txt_octal.value = "0"
                self.txt_decimal.value = "0"
                self.txt_hexadecimal.value = ""
        elif self.data_of_selection_textbox == "Select_decimal":
            if self.txt_decimal.value == "":
                self.txt_decimal.value = "0"
            value_of_text_box = self.txt_decimal.value
            try:
                self.txt_hexadecimal.value = self.calculateHexadecimalValue(
                    value_of_text_box
                )
                self.txt_octal.value = self.calculateOctalValue(value_of_text_box)
                self.txt_binary.value = self.calculateBinaryValue(value_of_text_box)
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
                self.txt_decimal.value = self.calculateValuesForTheRespectivePower(
                    value_of_text_box
                )
                self.txt_hexadecimal.value = self.calculateHexadecimalValue(
                    self.txt_decimal.value
                )
                self.txt_binary.value = self.calculateBinaryValue(
                    self.txt_decimal.value
                )
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
                self.txt_decimal.value = self.calculateValuesForTheRespectivePower(
                    value_of_text_box
                )
                self.txt_hexadecimal.value = self.calculateHexadecimalValue(
                    self.txt_decimal.value
                )
                self.txt_octal.value = self.calculateOctalValue(self.txt_decimal.value)
            except ValueError:
                self.txt_binary.value = ""
                self.txt_octal.value = "0"
                self.txt_decimal.value = "0"
                self.txt_hexadecimal.value = "0"
        else:
            self.update()
        self.update()

    def calculateValuesForTheRespectivePower(self, value):
        aux = str(value)
        power = 0
        aux_list = []
        result = 0
        sum = 0
        if self.data_of_selection_textbox == "Select_binary":
            for i in range(len(aux) - 1, -1, -1):

                if aux[i] == "0":
                    aux_list.append(int(aux[i]))
                else:
                    result = int(aux[i]) * (2**power)
                    aux_list.append(result)
                power += 1

            for i in aux_list:
                sum += i

            return str(sum)
        elif self.data_of_selection_textbox == "Select_octal":
            for i in range(len(aux) - 1, -1, -1):

                if aux[i] == "0":
                    aux_list.append(int(aux[i]))
                else:
                    result = int(aux[i]) * (8**power)
                    aux_list.append(result)
                power += 1

            for i in aux_list:
                sum += i

            return str(sum)

        elif self.data_of_selection_textbox == "Select_hexadecimal":
            for i in range(len(aux) - 1, -1, -1):
                aux[i].upper
                if aux[i] == "A" or aux[i] == "a":
                    result = 10 * (16**power)
                    aux_list.append(int(result))
                elif aux[i] == "B" or aux[i] == "b":
                    result = 11 * (16**power)
                    aux_list.append(int(result))
                elif aux[i] == "C" or aux[i] == "c":
                    result = 12 * (16**power)
                    aux_list.append(int(result))
                elif aux[i] == "D" or aux[i] == "d":
                    result = 13 * (16**power)
                    aux_list.append(int(result))
                elif aux[i] == "E" or aux[i] == "e":
                    result = 14 * (16**power)
                    aux_list.append(int(result))
                elif aux[i] == "F" or aux[i] == "f":
                    result = 15 * (16**power)
                    aux_list.append(int(result))
                else:
                    result = int(aux[i]) * (16**power)
                    aux_list.append(result)
                power += 1

            for i in aux_list:
                sum += i

            return str(sum)

    def calculateBinaryValue(self, value):
        aux = int(value)
        aux_list = []
        while True:
            result = aux // 2
            calc = (aux // 2) * 2
            resto = aux - calc
            aux_list.append(str(resto))
            aux = result

            if aux == 0 or aux == 1:
                aux_list.append(str(aux))
                break

        aux_list.reverse()
        aux_list = "".join(aux_list)
        return str(aux_list)

    def calculateOctalValue(self, value):
        aux = int(value)
        aux_list = []
        while True:
            result = aux // 8
            calc = (aux // 8) * 8
            resto = aux - calc
            aux_list.append(str(resto))
            aux = result

            if aux <= 8:
                aux_list.append(str(aux))
                break

        aux_list.reverse()
        aux_list = "".join(aux_list)
        return str(aux_list)

    def calculateHexadecimalValue(self, value):
        aux = int(value)
        aux_list = []

        while True:
            result = aux // 16
            calc = (aux // 16) * 16
            resto = aux - calc

            if resto == 10:
                aux_list.append("A")
            elif resto == 11:
                aux_list.append("B")
            elif resto == 12:
                aux_list.append("C")
            elif resto == 13:
                aux_list.append("D")
            elif resto == 14:
                aux_list.append("E")
            elif resto == 15:
                aux_list.append("F")
            else:
                aux_list.append(str(resto))

            aux = result

            if aux <= 16:
                aux_list.append(str(aux))
                break
        aux_list.reverse()
        aux_list = "".join(aux_list)
        return str(aux_list)

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
