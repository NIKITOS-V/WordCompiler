from spellchecker import SpellChecker
from readchar import readchar
from os import system
from itertools import permutations


class WordCompiler:
    def __init__(self):
        self.SpellChecker = SpellChecker(language='ru')

        self.MainLoop()

    def ClearConsole(self):
        system('cls')

    def RunContinue(self):
        print('\nВведите любую букву для продолжения или пробел для завершения: ', end='')
        return readchar()

    def MainLoop(self):
        UserInput = ''

        while UserInput != ' ':
            self.ClearConsole()

            ListOfSymbols = input("\nВведите буквы: ")
            NumberSymbolsInWord = input("\nВведите кол-во букв в слове: ")

            try:
                NumberSymbolsInWord = int(NumberSymbolsInWord)

                if NumberSymbolsInWord > len(ListOfSymbols):
                    print(f"\n{NumberSymbolsInWord} > кол-ва букв")

                    UserInput = self.RunContinue()

                    continue

            except ValueError:
                print(f"\n{NumberSymbolsInWord} - не число")
                continue

            if ListOfSymbols.isalpha():

                self.PrintWord(permutations(ListOfSymbols, NumberSymbolsInWord))

                UserInput = self.RunContinue()

            else:
                print('\nКриво ввёл')

                UserInput = self.RunContinue()

    def PrintWord(self, List):
        print()
        for Word in List:
            Word = ''.join(Word)

            if Word == self.SpellChecker.correction(Word):
                print(Word)
        print()


WC = WordCompiler()
