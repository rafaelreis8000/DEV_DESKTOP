import flet as ft

from app.login import login
from app.home import TelaHome #chama a classe tela home

obj_home=TelaHome()#instancia a tela home como um objeto

def registro_rotas(page:ft.Page):
    def mudar_rotas(route):

        page.views.clear()

        if page.route=="/":
            page.views.append(ft.View(route="/",controls=[login(page)]))

        elif page.route=="/home":
            page.views.append(ft.View(route="/home",controls=[obj_home.home()]))

        page.update()

    page.on_route_change=mudar_rotas