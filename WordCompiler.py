from readchar import readchar
import os
from itertools import permutations
import inspect
import hashlib
import pickle


class WordCompiler:
    def __init__(self):
        self.Russian_dictionary = None

        self.OpenFile()
        self.mainloop()

    def clear_console(self):
        os.system('cls')

    def OpenFile(self):
        dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

        with open(f'{dir}\\russian.bin', 'rb') as file:
            self.Russian_dictionary = pickle.load(file)

    def continue_working(self):
        print('\nВведите любую букву для продолжения или пробел для завершения: ', end='')
        return readchar()

    def mainloop(self):
        user_input = ''

        while user_input != ' ':
            self.clear_console()

            list_of_characters = input("\nВведите буквы: ")
            number_characters_in_word = input("\nВведите кол-во букв в слове: ")

            try:
                number_characters_in_word = int(number_characters_in_word)

                if number_characters_in_word > len(list_of_characters):
                    print(f"\n{number_characters_in_word} > кол-ва букв")

                    user_input = self.continue_working()

                    continue

            except ValueError:
                print(f"\n{number_characters_in_word} - не число")
                continue

            if list_of_characters.isalpha():

                self.print_word(set(permutations(list_of_characters, number_characters_in_word)))

                user_input = self.continue_working()

            else:
                print('\nКриво ввёл')

                user_input = self.continue_working()

    def print_word(self, List):
        print()

        for word in List:

            try:
                print(self.Russian_dictionary[hashlib.sha256(''.join(word).encode()).hexdigest()])

            except KeyError:
                pass

        print()


WordCompiler()
