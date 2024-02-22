import reflex as rx


class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1
        if self.count % 2 == 0:
            raise ValueError("Even number detected!")


def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(f"Count: {State.count}"),
            rx.button(
                "Increment",
                on_click=State.increment,  # type: ignore
                size="4",
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )
def custom_exception_handler(exception):
    print(f"custom exception handler called: {exception}") 

app = rx.App(exception_handler=custom_exception_handler)

app = rx.App()
app.add_page(index)
