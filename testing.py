class myClass():
    def __init__(self, name, age, username):
        self.name = name
        self.username = username
        self.age = age

    def post(self, message):
        print(message.format(**self.__dict__))

instance = myClass("Robstersgaming", "50", "Rob")
instance.post("Hello {name} nice name!!! {age}, {username}")
