import random
import string


class Alphabets:
    alpha_lower = list(string.ascii_lowercase)
    alpha_upper = list(string.ascii_uppercase)
    upper_lower_alphabets = alpha_lower + alpha_upper
    alpha_list = []

    def __init__(self, num_of_alpha):
        self.num_of_alpha = num_of_alpha

    def num_of_input_alphabets(self):
        for a in range(self.num_of_alpha):
            self.alpha_list.append(random.choice(self.upper_lower_alphabets))
        return self.alpha_list

    def __repr__(self):
        return '%r' % self.num_of_input_alphabets()
