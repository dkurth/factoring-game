import os
import colorama
import random

# This class makes it easy to include ascii art images from a given directory into your programs.
#
# If you put your ASCII art files in a directory called "art".
# ai = AsciiIncluder('art')

class AsciiIncluder:

    def __init__(self, artPath, extensions = (".txt")):
        artPath = os.path.abspath(artPath)
        if os.path.isdir(artPath):
            self.artPath = artPath
        else:
            raise Exception("This path does not exist: {0}.  Currently here: {1}".format(artPath, os.path.dirname(os.path.realpath(__file__))))

        self.load(extensions)

    def load(self, extensions):
        self.artFiles = [f for f in os.listdir(self.artPath) if os.path.isfile(os.path.join(self.artPath, f)) and f.lower().endswith(extensions)]
        self.art = {}
        for f in self.artFiles:
            path = os.path.join(self.artPath, f)
            name = os.path.basename(os.path.splitext(path)[0])
            with open(path) as fh:
                self.art[name] = fh.read()

    def show(self, artName, fgColor = '', bgColor = ''):
        # Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
        # Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
        # Style: DIM, NORMAL, BRIGHT, RESET_ALL
        # print(colorama.Fore.GREEN + ai.art["trogdor"])

        if artName not in self.art:
            return

        fgColorMap = {
            'black': colorama.Fore.BLACK,
            'red': colorama.Fore.RED,
            'green': colorama.Fore.GREEN,
            'yellow': colorama.Fore.YELLOW,
            'blue': colorama.Fore.BLUE,
            'magenta': colorama.Fore.MAGENTA,
            'cyan': colorama.Fore.CYAN,
            'white': colorama.Fore.WHITE,
        }

        bgColorMap = {
            'black': colorama.Back.BLACK,
            'red': colorama.Back.RED,
            'green': colorama.Back.GREEN,
            'yellow': colorama.Back.YELLOW,
            'blue': colorama.Back.BLUE,
            'magenta': colorama.Back.MAGENTA,
            'cyan': colorama.Back.CYAN,
            'white': colorama.Back.WHITE,
        }

        if fgColor in fgColorMap:
            fgColor = fgColorMap[fgColor]

        if bgColor in bgColorMap:
            bgColor = bgColorMap[bgColor]

        print(fgColor + bgColor + self.art[artName])
        print(colorama.Fore.RESET + colorama.Back.RESET)

    def showAwesome(self, name):
        colorSchemes = [
            ('green', 'black'),
            ('yellow', 'black'),
            ('white', 'blue'),
            ('black', 'cyan')
        ]

        fgColor, bgColor = random.choice(colorSchemes)
        self.show(name, fgColor, bgColor)

    # Other feature ideas:
    #
    # - trim whitespice around an images
    # - pad to a certain size
    # - flip
    # - some way to truncate instead of wrapping long lines