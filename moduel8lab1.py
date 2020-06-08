"""
CTEC 121
eddy
moduel8 lab 1
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""




from graphics import *
from dog import Dog
from msdie import MSDie
import docTest
def main():
    # dictionarys
    '''
    mydict = {}
    # key - value
    # create element
    mydict["key"] = "value"
    mydict["key"] = "new value"
    print(mydict.keys())
    print(mydict.values())
    print(mydict.items())
    '''
    # files
    '''
    filenames = open("somestufft.txt", "r")
    print()
    readreturn = filenames.read()
    print(type(readreturn))
    print()
    print("sec line", filenames.read())
    filenames.close()
    '''
    # mod 7 assignment review
    # section 1
    '''
    win = GraphWin("demo", 1000, 1000)
    myCircel = Circle(Point(500, 500), 200)
    myCircel.setFill("green")
    myCircel.draw(win)
    win.getMouse()
    '''
    # section 2
    '''
    d = Dog("Dog")
    print(d)
    print(d.getName())
    d.setName("jevus")
    print(d.getName())

    d.bark()
    '''

    # section 3
    '''
    die = MSDie(6)
    print("number of sides", die.getSides())
    print("value: ", die.getValue())
    die.setValue(5)
    print("value: ", die.getValue())
    die.setValue(12)
    print("value: ", die.getValue())
    die.roll()
    print("value: ", die.getValue())
    die.roll()
    print("value: ", die.getValue())
    '''
    print()
    # print moduel/files header documentation

    print(docTest.__doc__)
    # print class docs
    print()
    print(docTest.DocTest.__doc__)
    # print method docs
    print()
    print(docTest.DocTest.method.__doc__)


main()
