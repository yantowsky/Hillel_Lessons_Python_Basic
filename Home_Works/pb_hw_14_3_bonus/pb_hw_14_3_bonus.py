class Print:
    def print_text(self, text):
        pass


class PrintToScreen(Print):
    def print_text(self, text):
        print(text)


class PrintToFile(Print):
    def __init__(self, filename):
        self.filename = filename

    def print_text(self, text):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(text)


# Основний код
print_screen = PrintToScreen()
print_file = PrintToFile("output.txt")

print_screen.print_text("Hello, world!")
print_file.print_text("This text goes to a file.")
