import random


class Symbols:
    symbol_list = []

    def __init__(self, num_of_symbols):
        self.num_of_symbols = num_of_symbols
        self.all_symbols = ['!', '@', '#', '$', '^', '&', '*', '/', '?', '{', '}', '[', ']', '|']

    def user_input_num_of_symbols(self):
        for i in range(self.num_of_symbols):
            self.symbol_list.append(random.choice(self.all_symbols))
        return self.symbol_list

    def __repr__(self):
        return '%r' % self.user_input_num_of_symbols()
