class Washer:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def print_info(self):
        print(f'height = {self.height}')
        print(f'width = {self.width}')


haiEr = Washer(100, 50)
haiEr.print_info()
