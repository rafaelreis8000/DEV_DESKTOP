import flet as ft

def main(page: ft.Page):
    # Cria uma coluna para adicionar controles
    container = ft.Column()

    # Função para adicionar controles à coluna
    def add_controls(e):
        container.controls.append(ft.Text("Novo Texto"))
        page.update()

    # Função para limpar o container
    def clear_container(e):
        container.controls.clear()  # Limpa os controles do container
        page.update()

    # Botão para adicionar controles
    btn_add = ft.ElevatedButton("Adicionar Controle", on_click=add_controls)
    
    # Botão para limpar a coluna
    btn_clear = ft.ElevatedButton("Limpar Container", on_click=clear_container)

    # Adiciona os botões e o container à página
    page.add(btn_add, btn_clear, container)

ft.app(target=main)
