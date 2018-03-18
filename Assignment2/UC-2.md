## User Case Audiction(UC-2)

**Related Requirements:** REQ1 & REQ2 & REQ6

**Initiating Actor:** User

**Actor's Goal:** To specify the fisrt piece of music used to generate melody. 

**Participating Actor:** Visualizer

**Preconditions:** The configuration has done by user.

**Postconditions:** The program use the melody provide by user to train and gernerate new melody.

**Flow of Event for Main Success Scenario:**

→ 1. **User** (a) clicks "Import" buttom to import the first piece melody from MIDI file, or (b) note the melody using numbered musical notations. 

← 2. **Visulizer** Display user's input.



## Responsibilities

| Responsibility Description                                   | Concept Name |
| ------------------------------------------------------------ | ------------ |
| Rs1. Read the music data from MIDI file.                     | Reader       |
| Rs2. Translate the MIDI data to numbered musial notations.   | Translator   |
| Rs3. Graphical interface that allows to edit the numbered musical notations . | Editor       |

## Associations

| Concept Pair      | Association description                            | Association name           |
| ----------------- | -------------------------------------------------- | -------------------------- |
| Reader↔Translator | Recorder pass the music data to translator         | provides MIDI data         |
| Translator↔Editor | Translator pass the notations to Translator-Editor | provides misical notations |

## Attributes

| Concept | Attributes     | Attribute Description          |
| ------- | -------------- | ------------------------------ |
| Reader  | MIDI data      | MIDI data read from files      |
| Editor  | notations data | user's noted musical notations |
