#Use this file to test anything
from GAModel.period import unit, period

# s = [0, 2, 4, 5, 7, 9, 11, 12]
# a = unit(s, 1)
# b = period([a])
# print(b.units[0].notes)
# s[2] = 3
# x = []
# a.notes[2] = 3
# b.append(a)
# print(b.get_notes())
# print(a[5])
# print(b[1][2])
# t = [0, 2, 8, 5, 9, 9, 11, 12]
# b.units[1] = unit(t)
# print(b)
t = unit([0, 2, 8, 5, 9, 9, 11, 12])
t.update_chord_4()
print(t.chord_score)