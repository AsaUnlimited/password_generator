import random


class Numbers:
    num_password = []

    def __init__(self, num_of_numbers):
        self.num_of_numbers = num_of_numbers

    def user_input_num_of_numbers(self):
        for num in range(self.num_of_numbers):
            self.num_password.append(random.randint(0, 9))
        return self.num_password

    def __repr__(self):
        return '%r' % self.user_input_num_of_numbers()