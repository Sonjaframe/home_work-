class Button:
    def __init__(self, a: str):
        self.a = a
    def Text_Button(self) -> None:
        if self.a == "Text Box":
            return print(f"Клик по кнопке {self.a}")
        elif self.a == "Check Box":
            return print(f"Клик по кнопке {self.a}")
        elif self.a == "Radio Button":
            return print(f"Клик по кнопке {self.a}")
        elif self.a == "Web Tables":
            return print(f"Клик по кнопке {self.a}")
        elif self.a == "Links":
            return print(f"Клик по кнопке {self.a}")
        elif self.a == "Broken Links Images":
            return print(f"Клик по кнопке {self.a}")
        elif self.a == "Upload and Dowload":
            return print(f"Клик по кнопке {self.a}")
        elif self.a == "Dynamic Properties":
            return print(f"Клик по кнопке {self.a}")
        else:
            return print("Неизвестное имя кнопки")
button1 = Button("Text Box")
button2 = Button("Check Box")
button3 = Button("Radio Button")
button4 = Button("Web Tables")
button5 = Button("Links")
button6 = Button("Broken Links Images")
button7 = Button("Upload and Dowload")
button8 = Button("Dynamic Properties")
button9 = Button("Dynamic Properties23")

button1.Text_Button()
button2.Text_Button()
button3.Text_Button()
button4.Text_Button()
button5.Text_Button()
button6.Text_Button()
button7.Text_Button()
button8.Text_Button()
button9.Text_Button()



