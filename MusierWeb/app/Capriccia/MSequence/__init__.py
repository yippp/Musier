"""
MSequence is the encapsulation for melody sequence.
This package contains less information than MIDI file and focuses on composing only.
Definition and interfaces such like I/O included in this module.

Reference only, all numerical pitch notation following this dictionary in this module
pitch_dictionary = {-1:'mute',
                    0: 'last',
                    1: 'A0', 2: 'A#0', 3: 'B0', ...,
                    40: 'C4', 41: 'C#4', 42: 'D4', 43: 'D#4', 44: 'E4', 45: 'F4',
                    46: 'F#4', 47: 'G4', 48: 'G#4', 49: 'A5', 50: 'A#5', 51: 'B5', 52: 'C5', ...,
                    88: 'C8'}

"""
