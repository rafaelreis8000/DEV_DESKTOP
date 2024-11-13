import flet as ft
import requests

from ..componentes.appbar import Appbar
from ..componentes.sidebar import Sidebar

class TelaUsuarios:
    def __init__(self,page,checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def usuarios(self):
        appbar=Appbar(self.page).Componente_Appbar()
        sidebar=Sidebar(self.page).Componente_sidebar("usuarios")

        txt_tela=ft.Container(
            padding=10,
            margin=10,
            content=ft.Column(
                [
                    ft.Text("Gerenciamento de Usuários",color=ft.colors.BLACK,size=20),
                    ft.Text(
                        "Aqui você pode visualizar e criar usuários.",
                        color=ft.colors.BLACK
                    )
                ]
            )
        )

        ###############################################################################
        ###############################################################################

        tela=ft.Container(
            expand=True,
            bgcolor="#D9D9D9",
            content=ft.Row(
                [
                    sidebar,
                    ft.Column(
                        [
                            appbar,
                            txt_tela
                        ]
                    )
                ]
            )
        )

        return tela