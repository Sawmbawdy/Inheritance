class Bird:
    def __init__(self):
        print("Bird is ready")
    def WhoIsThis(self):
        print("Bird")
    def run(self):
        print("Run Faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin Is Ready")
    def WhoIsThis(self):
        print("Penguin")
    def fly(self):
        print("Fly Faster")
Linux = Penguin()
Linux.WhoIsThis()
Linux.fly()
Linux.run()