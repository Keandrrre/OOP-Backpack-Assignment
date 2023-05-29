# Task 1
class backpack_class:
    # Define constructor method
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False

    # Methods
    def openBag(self):
        self.open = True
        print("Backpack open")

    def closeBag(self):
        self.open = False
        print("Backpack closed")

    def putin(self, item):
        if self.open == True:
            self.items.append(item)
            print('"' + str(item) + '" was added to the backpack.')

    def takeout(self, item):
        if self.open == True:
            for i in range(len(self.items)):
                if self.items[i] == item:
                    self.items.pop(i)
                    print('"' + str(item) + '" was removed from backpack')


# Task 2
backpack1 = backpack_class('blue', 'small')
backpack2 = backpack_class('red', 'medium')
backpack3 = backpack_class('green', 'large')

# Task 3
backpack3.openBag()
backpack3.putin('lunch')
backpack3.putin('jacket')
backpack3.closeBag()
backpack3.openBag()
backpack3.takeout('jacket')
backpack3.closeBag()
