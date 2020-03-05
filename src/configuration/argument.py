#!/usr/bin/python3

import sys

#from methods.operators.evaluation.fitnessRMSE import fitnessRMSE #function
#from methods.operators.operator import operatorGenerate #function

class Argument:
    def __init__(self, name, value):
        if type(name) is not str:
            raise ValueError("Argument argument isn't type str.")
        self.name = name
        self.value = value

    def importAsString(string):
        stringList = string.split("=")
        return Argument(stringList[0], stringList[1])

    def exportAsString(self):
        return str(self.name) + "=" + str(self.value)

    def exportValueAsInt(self):
        return int(self.value)

    def exportValueAsFnc(self):
        return str_to_Fnc(self.value)

    def exportValueAsClass(self):
        return str_to_class(self.value)


def str_to_Fnc(str):
    try:
       return getattr(sys.modules["methods.operators.evaluation." + str], str)
    except:
      d = 1
    try:
       return getattr(sys.modules["methods.operators." + str], str)
    except:
      d = 1
      return None


def str_to_class(classname):
    fileName = classname[0].lower() + classname[1:]
    return getattr(sys.modules["methods.operators.aggregation." + fileName], classname)