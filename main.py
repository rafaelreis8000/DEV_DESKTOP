import flet as ft

from app.rotas import registro_rotas

def main(page:ft.Page):

    registro_rotas(page)
    page.title="Fazenda Horticultura"

    page.go("/")
    page.update

ft.app(target=main)