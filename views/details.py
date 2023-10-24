from flet import *
from flet_route import Params, Basket

class DetailsPage:
    def __init__(self):
        super().__init__()

    def view(self, page: Page, params: Params, basket: Basket):
        body = Column()
        body.controls.append(Text("Details"))
        body.controls.append((TextButton("Go to Details", on_click=lambda _ : page.go("/"))))

        return View("/", controls=[body])
