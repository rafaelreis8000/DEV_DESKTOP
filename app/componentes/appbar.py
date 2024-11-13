import flet as ft

class Appbar:
    def __init__(self,page):
        self.page=page
    
    def Componente_Appbar(self):

        #pop-up que aparece se o usuário clica no botão de sair do sistema
        alerta_logout=ft.AlertDialog(
            modal=True,
            bgcolor="#2A383E",
            title=ft.Text("CONFIRMAR LOGOUT"),
            content=ft.Text("Você realmente deseja fazer logout do aplicativo?"),
            actions=[
                ft.TextButton("Sim",on_click=lambda _:self.page.go("/")), #se sim, ele volta pra tela inicial de login
                ft.TextButton("Não",on_click=lambda _:self.page.close(alerta_logout)) #senão, fecha o pop-up
            ]
        )

        icone_sair=ft.Container(
            padding=20,
            on_click=lambda e:self.page.open(alerta_logout),
            content=ft.Image("app/assets\icone_sair.svg"),
        )

        appbar=ft.Container(
            height=75,
            width=self.page.width * 1,
            bgcolor="#1D3331",
            content=ft.Row(
                [
                    ft.Container(), #container vazio, usado para espaçar o ícone sair pro canto direito da tela
                    icone_sair
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=0
        )

        return appbar