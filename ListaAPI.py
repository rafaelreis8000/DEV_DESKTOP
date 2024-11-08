import flet as ft
import requests

def main(page: ft.Page):

    API="https://api-pim.onrender.com"
    
    popup_usuario=ft.AlertDialog()

    def atualizar_lista():
        page.controls.clear()  # Limpa a lista

        try:
            response=requests.get(f"{API}/users")
            response_data=response.json()

            print(response_data) #imprime no terminal os dados coletados da lista de usuários da API
        
        except requests.exceptions.RequestException as e:
            print("erro")
        
        for i in response_data:
            itens_lista=ft.Container(
                content=ft.Text(f"Usuário {i["nome"]}", size=18, color=ft.colors.BLACK),
                width=200,
                height=50,
                bgcolor="#2E2E2E",
                border_radius=5,
                padding=10,
                alignment=ft.alignment.center,
                on_click=lambda e,index=i:exibir_popup(index)
            )
            page.controls.append(itens_lista)
            page.update()

    # Função para exibir o pop-up com as informações do item clicado
    def exibir_popup(index):
        popup_usuario.content=ft.Text(
            f"ID: {index["usuario_id"]}\nNome: {index["nome"]}\nE-mail: {index["email"]}\nNível: {index["tipo_usuario"]}"
        )
        page.dialog=popup_usuario
        popup_usuario.open=True
        page.update()

    page.add(
        ft.Column(scroll="auto"),  # Permite a rolagem na lista
    )

    atualizar_lista()

# Executa o app
ft.app(target=main)

