class Greeting:
    def __init__(self, word):
        self.msg = word

    def helloworld(self):
        print(self.msg)

gree = Greeting("Hello World")
gree.helloworld()
