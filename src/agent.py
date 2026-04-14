class Agent:
    def __init__(self, start):
        self.position = start
        self.path = []

    def set_path(self, path):
        self.path = path

    def move(self):
        if self.path:
            self.position = self.path.pop(0)