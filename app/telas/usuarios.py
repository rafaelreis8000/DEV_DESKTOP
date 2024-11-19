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

    # define o que a lista realmente vai fazer
    def lista_usuarios(self):
        print(self.checar_estado.token)
        parametros={"Authorization":f"Bearer {self.checar_estado.token}"}

        resultado=requests.get(f"{API_URL}/users",headers=parametros)

        usuarios=resultado.json()

        for user in usuarios:
            container_elemento_lista=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Image("app/assets\icone_perfil.svg",width=50,height=50),
                        ft.Text(f"Nome: {user["nome"]}",size=15),
                        ft.Text(f"E-mail: {user["email"]}",size=15),
                        ft.Text(f"Cargo: {user["tipo_usuario"]}",size=15)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                width=700,
                padding=20,
                bgcolor="#2A383E",
                border=ft.border.all(6,ft.colors.BLUE_GREY),
                border_radius=ft.border_radius.all(10),
            )

            self.componente_lista.controls.append(container_elemento_lista)

        ###############################################################################
        ###############################################################################

class TelaUsuarios:

    def __init__(self,page,checar_estado):
        self.page=page
        self.checar_estado=checar_estado

    def usuarios(self):
        appbar=Appbar(self.page).appBar()
        sidebar=Sidebar(self.page).sideBar("usuarios")
        users=UsuariosAPI(self.checar_estado)

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
                            txt_tela,
                            ft.Column(
                                [
                                    ft.Container(users,alignment=ft.alignment.center)
                                ],
                                expand=True,
                                scroll="auto" # habilita o scroll somente para a lista
                            ),
                           # ft.Container(users,alignment=ft.alignment.center) # lista de usuários alinhada no centro da tela
                        ],
                        expand=True,

                    )
                ],
                spacing=0,
            )
        )

        return tela