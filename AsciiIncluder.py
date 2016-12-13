import os

# This class makes it easy to include ascii art images from a given directory into your programs.

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