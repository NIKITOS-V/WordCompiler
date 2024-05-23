from spellchecker import SpellChecker
from readchar import readchar
from os import system


class WordCompiler:
    def __init__(self):
        self.SpellChecker = SpellChecker(language='ru')

        self.MainLoop()

    def ClearConsole(self):
        system('cls')

    def MainLoop(self):
        UserInput = ''

        while UserInput != ' ':
            Symbols = input("Введите буквы через пробел")
            NumberSymbolsInWord = int(input("Введите кол-во букв в слове"))

            if Symbols.isalpha():
                LenSymbols = len(Symbols)
                Symbols = Symbols.split()

                String = ''

                for index, symbol1 in enumerate(Symbols):
                    String += symbol1

                    for number in range(NumberSymbolsInWord):
                        for symbol2 in Symbols[index+1: -1-number]:
                            String += symbol2

                print(String)

            else:
                print('\n\tКриво ввёл')
                UserInput = readchar()


if __name__ == "__name__":
    WC = WordCompiler()
