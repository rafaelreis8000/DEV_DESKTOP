import flet as ft

def login(page:ft.Page):

    logo=ft.Container(
        content=ft.Image("app/assets\logo.png")
    )

    input_usuario=ft.Container(
        content=ft.Column(
            controls=[
                ft.TextField(label="Insira se E-mail: "),
                ft.TextField(label="Insira sua senha: ",password=True),
            ],
            alignment=ft.alignment.center
        )
    )

#####################################################################################
#####################################################################################

    tela=ft.Container(
        expand=True,
        bgcolor="#1D3331",
        content=ft.ResponsiveRow(
            col={"xs":12,"sm":6,"md":4},
            controls=[
                #logo,
                input_usuario
            ]
        )
    )

    return tela