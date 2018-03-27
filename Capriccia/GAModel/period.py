from settings import *
from copy import deepcopy

class unit:
    def __init__(self, notes=None, chordID=0):
        if notes is None:
            self.notes = []
        else:
            self.notes = deepcopy(notes)
        self.length = len(self.notes)
        self.chordID = chordID
        self.chord_score = NULL_SCORE
        self.score = NULL_SCORE

    def __getitem__(self, i):
        return self.notes[i]

    def __str__(self):
        return "%s chordID: %d" % (self.notes, self.chordID)

    def update_chord_4(self):
        """
        Find a reasonable chord for a 4*k-length unit 'u', and update u.chord
        """
        if (self.length == 0) or (self.length % 4 != 0):
            raise Exception('Error: Invalid unit length.')
        n = (self[0] % 12, self[self.length // 2] % 12, self[self.length // 4] % 12, self[self.length * 3 // 4] % 12)
        s = (12, 8, 2, 2)
        s_n = (4, 5, 1, 1)
        best = -1
        best_id = 0
        for i in range(1, len(CHORD)):
            score = 0
            for j in range(4):
                if n[j] is None:
                    score += s_n[j]
                if n[j] in CHORD[i]:
                    score += s[j]
            if score > best:
                best = score
                best_id = i
        self.chordID = best_id
        self.chord_score = best

class period:
    def __init__(self, units=None):
        if units is None:
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