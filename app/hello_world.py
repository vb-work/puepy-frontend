from puepy import Application, Page, t

app = Application()


@app.page()
class HelloWorldPage(Page):
    def populate(self):
        pass
        #t.h1("")


app.mount("#app")
