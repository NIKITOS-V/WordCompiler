from readchar import readchar
import os
from itertools import permutations
import inspect
import ctypes


class WordCompiler:
    def __init__(self):
        self.RuDict = None
        self.WordSearchEngine = None
        self.LenRuDict = None
        self.Dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

        self.LibraryPreparation()
        self.OpenFile()
        self.MainLoop()

    def LibraryPreparation(self):
        self.WordSearchEngine = ctypes.WinDLL(f"{self.Dir}\\WordSearchEngine.dll").For
        self.WordSearchEngine.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_size_t]
        self.WordSearchEngine.restypes = ctypes.c_int

    def ClearConsole(self):
        os.system('cls')

    def OpenFile(self):
        with open(f'{self.Dir}\\russian.txt', 'r', encoding='windows-1251', ) as File:
            RuDict = list(map(lambda word: hash(word), File.read().split('\n')[0:-1]))

        self.RuDict = (ctypes.c_int * len(RuDict))()

        for Index, Hash in enumerate(RuDict):
            self.RuDict[Index] = Hash

        self.LenRuDict = len(self.RuDict)

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

            if self.WordSearchEngine(hash(Word), self.RuDict, self.LenRuDict):
                print(Word)

        print()


WC = WordCompiler()
