import flet as ft

class TelaHome:
    def home(page:ft.Page):

        #Pop-up de alerta. Ao clicar em fazer logoff, uma confirmação é chamada
        alerta_logout=ft.AlertDialog(
            modal=True,
            bgcolor="#2A383E",
            title=ft.Text("CONFIRMAR LOGOUT"),
            content=ft.Text("Você realmente deseja fazer Logoff do aplicativo?"),
            actions=[
                ft.TextButton("Sim", on_click=lambda _:page.go("/")),
                ft.TextButton("Não", on_click=lambda e:page.close(alerta_logout)),
            ]
        )

        ###############################################################################
        ###############################################################################

        logo=ft.Image("app/assets\logo3.jpg")
        icone_sair=ft.Container(
            margin=20,
            on_click=lambda e:page.open(alerta_logout),
            content=ft.Image("app/assets\Ícone Sair.svg"),
        )

        appbar=ft.Container(
            height=75,
            bgcolor="#2A383E",
            content=ft.Row(
                [
                    logo,
                    icone_sair
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )

        sidebar=ft.Container(
            width=160,
            bgcolor="#2A383E",
            content=ft.Column(
                [
                    ft.Text("Teste 1"),
                    ft.Text("Teste 2"),
                    ft.Text("Teste 3")
                ]
            )
        )

        ###############################################################################
        ###############################################################################

        tela=ft.Container(
            expand=True,
            bgcolor="#D9D9D9",
            content=ft.ResponsiveRow(
                col={"xs":12,"sm":6,"md":4},
                controls=[
                    appbar,
                    ft.Container(
                        sidebar,
                        alignment=ft.alignment.center_left #joga a sidebar para a esquerda, sem que estique pro restante da tela
                    ),
                ]
            )
        )

        return tela