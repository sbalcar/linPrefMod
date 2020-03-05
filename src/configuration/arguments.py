#!/usr/bin/python3

from configuration.argument import Argument

class Arguments:
    # arguments:list<Argument>
    def __init__(self, arguments):
        if type(arguments) is not list:
            raise ValueError("Argument arguments isn't type list.")
        for argumentI in arguments:
            if type(argumentI) is not Argument:
                raise ValueError("Argument arguments don't contain Argument.")
        self.arguments = arguments

    # string:str
    def importAsString(string):
        if string.strip() == '':
            return Arguments([])

        argumentsList= []
        strings = string.split(",")

        for stringI in strings:
          argumentsList.append(Argument.importAsString(stringI.strip()))

        return Arguments(argumentsList)

    def exportAsString(self):
        string = ""
        for argumentI in self.arguments:
            string = string + argumentI.exportAsString() + ", "
        return string[:-2]

    # name:str
    def exportArgument(self, name):
        argumentSelected = [argumentI for argumentI in self.arguments if argumentI.name == name]
        if len(argumentSelected) == 0:
            return None
        return argumentSelected[0]