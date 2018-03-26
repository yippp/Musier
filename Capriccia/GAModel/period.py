from settings import *
from copy import deepcopy

class unit:
    def __init__(self, notes = None, chordID = 0):
        self.notes = deepcopy(notes)
        self.length = len(notes)
        self.chordID = chordID

    def __getitem__(self, i):
        return self.notes[i]

    def __str__(self):
        return "%s chordID: %d" % (self.notes, self.chordID)

class period:
    def __init__(self, units = None):
        self.units = deepcopy(units)
        self.length = len(units)

    def __getitem__(self, i):
        return self.units[i]

    def __str__(self):
        s = ''
        for u in self.units:
            s = s + str(u) + '\n'
        return s[:-1]

    def append(self, u):
        self.units.append(u)

    def extend(self, p):
        self.units.extend(p)

    def notes(self):
        notes = []
        for u in self.units:
            notes.extend(u.notes)
        return notes