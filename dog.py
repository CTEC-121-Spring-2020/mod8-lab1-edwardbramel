# dog


class Dog:
    # define contructor
    def __init__(self, name):
        self._name = name

    # encapsulation of instance variables
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    # add some behabior
    def bark(self):
        print("bark, barak, bark")
