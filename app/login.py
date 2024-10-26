import flet as ft

def login(page:ft.Page):

    tela=ft.Container(
        expand=True,
        bgcolor="#1D3331",
        content=ft.ResponsiveRow(
            col={"xs":12,"sm":6,"md":4},
            controls=[ft.Text("LOGIN")]
        )
    )

    return tela