import flet as ft
import requests

from ..componentes.appbar import Appbar
from ..componentes.sidebar import Sidebar

API_URL="https://api-pim.onrender.com"
SECRET_KEY="0d8689404a2c83325a0353496caafcdfa01abd76f4511037bad2a66ed3dd6050"

class UsuariosAPI(ft.Column):
    def __init__(self, checar_estado):
        self.checar_estado=checar_estado
        super().__init__()


        # aqui uma coluna é criada
        self.componente_lista=ft.Column(
            expand=True,
        )

        self.controls = [
            self.componente_lista
        ]

        self.lista_usuarios()
        self.criar_usuario()

    # define o que a lista realmente vai fazer
    def lista_usuarios(self):
        print(self.checar_estado.token)
        parametros={"Authorization":f"Bearer{self.checar_estado.token}"}

        resultado=requests.get(f"{API_URL}/users",headers=parametros)

        usuarios=resultado.json()

        for user in usuarios:
            container_elemento_lista=ft.Container(
                ft.Text(
                    user,
                    color="#000000"
                    ),
                    padding=50,
                    border=ft.border.all(2),
                )

            self.componente_lista.controls.append(container_elemento_lista)

    def criar_usuario(self):
        btn_create=ft.ElevatedButton("Criar",style=ft.ButtonStyle(bgcolor="#1C1C1C"))

        self.componente_lista.controls.append(btn_create)

        ###############################################################################
        ###############################################################################

class TelaUsuarios:

    def __init__(self,page, app_state):
        self.page=page
        self.app_state=app_state

    def usuarios(self):
        appbar = Appbar(self.page).appBar()
        sidebar = Sidebar(self.page).sideBar("usuarios")
        users = UsuariosAPI(self.app_state)

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

        tela = ft.Container(
            expand=True,
            bgcolor="#D9D9D9",
            content=ft.Row(
                [
                    sidebar,
                    ft.Column(
                        [
                            appbar,
                            txt_tela,
                            users
                        ],
                        expand=True
                    )
                ],
                spacing=0
            )
        )

        return tela