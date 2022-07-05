from project_beginner.password_generator import alphabets, numbers, symbols


class Main():
    pass_gen = []
    user_a = alphabets.Alphabets(int(input("Enter number of alphabet you want in your password: ")))
    user_b = numbers.Numbers(int(input("Enter number of alphabet you want in your password: ")))
    user_s = symbols.Symbols(int(input("Enter number of alphabet you want in your password: ")))

    pg = user_a.num_of_input_alphabets() + user_b.user_input_num_of_numbers() + user_s.user_input_num_of_symbols()
    print(''.join(map(str, pg)))
