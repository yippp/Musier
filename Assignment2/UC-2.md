## Use Case Audiction(UC-2)

**Related Requirements:** REQ1 & REQ2 & REQ6

**Initiating Actor:** User

**Actor's Goal:** To specify the fisrt piece of music used to generate melody. 

**Participating Actor:** Visualizer

**Preconditions:** The configuration has done by user.

**Postconditions:** The program uses the melody provided by user to train and gernerate new melody.

**Flow of Event for Main Success Scenario:**

→ 1. **User** (a) clicks "Import" buttom to import the first piece of melody from MIDI file, or (b) notes the melody using numbered musical notations. 

← 2. **Visualizer** displays the user's input.



## Responsibilities

| Responsibility Description                                   | Concept Name |
| ------------------------------------------------------------ | ------------ |
| Rs1. Load the music data from MIDI file.                     | Loader       |
| Rs2. Translate the MIDI data to numbered musial notations.   | Translator   |
| Rs3. Graphical interface that allows to edit the numbered musical notations . | Editor       |

## Associations

| Concept Pair      | Association description                            | Association name           |
| ----------------- | -------------------------------------------------- | -------------------------- |
| Loader↔Translator | Loader passes the music data to Translator         | provides MIDI data         |
| Translator↔Editor | Translator passes the notations to Editor          | provides musical notations |

## Attributes

| Concept | Attributes     | Attribute Description          |
| ------- | -------------- | ------------------------------ |
| Loader  | MIDI data      | MIDI data loaded from files.   |
| Editor  | notations data | user's noted musical notations |
