import flet as ft

from app.login import login
from app.home import home

def registro_rotas(page:ft.Page):
    def mudar_rotas(route):

        page.views.clear()

        if page.route=="/":
            page.views.append(ft.View(route="/",controls=[login(page)]))

        elif page.route=="/home":
            page.views.append(ft.View(route="/home",controls=[home(page)]))

        page.update()

    page.on_route_change=mudar_rotas