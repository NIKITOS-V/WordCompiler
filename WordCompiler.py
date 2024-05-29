from readchar import readchar
import os
from itertools import permutations
import inspect
import hashlib
import pickle


class WordCompiler:
    def __init__(self):
        self.RuDict = None

        self.OpenFile()
        self.MainLoop()

    def ClearConsole(self):
        os.system('cls')

    def OpenFile(self):
        Dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

        with open(f'{Dir}\\russian.bin', 'rb') as File:
            self.RuDict = pickle.load(File)

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

                self.PrintWord(set(permutations(ListOfSymbols, NumberSymbolsInWord)))

                UserInput = self.RunContinue()

            else:
                print('\nКриво ввёл')

                UserInput = self.RunContinue()

    def PrintWord(self, List):
        print()

        for Word in List:

            try:
                print(self.RuDict[hashlib.sha256(''.join(Word).encode()).hexdigest()])

            except KeyError:
                pass

        print()


WC = WordCompiler()
