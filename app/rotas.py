import flet as ft

from app.login import login

def registro_rotas(page:ft.Page):
    def mudar_rotas(route):

        page.views.clear()

        if page.route=="/":
            page.views.append(ft.View(route="/",controls=[login(page)]))

        page.update()

    page.on_route_change=mudar_rotas