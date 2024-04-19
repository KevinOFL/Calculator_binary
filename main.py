import flet as ft


def main(page: ft.page):
    # Configuring the personalize of page desktop
    page.title = "Binary Calculator"
    page.window_height = 600
    page.window_width = 600
    page.window_max_height = 700
    page.window_max_width = 700
    page.window_min_height = 575
    page.window_min_width = 400
    page.window_maximizable = False

    page.appbar = ft.AppBar(
        title=ft.Text("Binary Calculator"),
    )

    # Variable of controls
    txt_hexadecimal = ft.TextField(
        label="Hexadecimal",
        width=350,
        rtl=True,
        input_filter=ft.InputFilter(regex_string=r"[0-9/aA-hH]"),
    )  # noqa: F841
    txt_decimal = ft.TextField(
        label="Decimal",
        width=350,
        rtl=True,
        input_filter=ft.InputFilter(regex_string=r"[0-9]"),
    )  # noqa: F841
    txt_octal = ft.TextField(
        label="Octal",
        width=350,
        rtl=True,
        input_filter=ft.InputFilter(regex_string=r"[0-7]"),
    )  # noqa: F841
    txt_binary = ft.TextField(
        label="Binary",
        width=350,
        rtl=True,
        input_filter=ft.InputFilter(regex_string=r"[0-1]"),
    )  # noqa: F841

    page.add(
        ft.Row(
            controls=[txt_hexadecimal],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            controls=[txt_decimal],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            controls=[txt_octal],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            controls=[txt_binary],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(
                    " H ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " G ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " F ",
                    width=80,
                ),
                ft.ElevatedButton(
                    "A/C",
                    width=80,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(
                    " E ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " D ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " C ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " B ",
                    width=80,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(
                    " A ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " 9 ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " 8 ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " 7 ",
                    width=80,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(
                    " 6 ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " 5 ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " 4 ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " 3 ",
                    width=80,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(
                    " 2 ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " 1 ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " 0 ",
                    width=80,
                ),
                ft.ElevatedButton(
                    " = ",
                    width=80,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    ),

    page.update()


ft.app(main)
