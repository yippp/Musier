from settings import *
from copy import deepcopy

class unit:
    def __init__(self, notes = None, chordID = 0):
        if notes == None:
            self.notes = []
        else:
            self.notes = deepcopy(notes)
        self.length = len(self.notes)
        self.chordID = chordID
        self.score = NULL_SCORE

    def __getitem__(self, i):
        return self.notes[i]

    def __str__(self):
        return "%s chordID: %d" % (self.notes, self.chordID)

class period:
    def __init__(self, units = None):
        if units == None:
            self.units = []
        else:
            self.units = deepcopy(units)
        self.length = len(self.units)
        self.score = NULL_SCORE

    def __getitem__(self, i):
        return self.units[i]

    def __str__(self):
        s = ''
        for u in self.units:
            s = s + str(u) + '\n'
        return s[:-1]

    def append(self, u):
        self.units.append(u)
        self.length += 1

    def extend(self, p):
        self.units.extend(p)
        self.length += p.length

    def get_notes(self):
        '''
        :return: A list containing all the notes of the melody.
        '''
        notes = []
        for u in self.units:
            notes.extend(u.notes)
        return notes