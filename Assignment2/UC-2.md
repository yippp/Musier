## User Case Audiction(UC-2)

**Related Requirements:** REQ1 & REQ2 & REQ6

**Initiating Actor:** User

**Actor's Goal:** To specify the fisrt piece of music used to generate melody. 

**Participating Actor:** Visualizer

**Preconditions:** The configuration has done by user.

**Postconditions:** The program use the melody provide by user to train and gernerate new melody.

**Flow of Event for Main Success Scenario:**

→ 1. **User** Either click "record" buttum to start record the melody, or note the melody using numbered musical notations. 

← 2. **Visulizer** Display the user input



## Responsibilities

| Responsibility Description                                     | Concept Name       |
| -------------------------------------------------------------- | ------------------ |
| Rs1. Record the generated melody from record device.           | Recorder           |
| Rs2. Translate the recorded melody to numbered musial notations| Translator         |
| Rs3. numbered musical notations edit inteface                  | Editor             |

## Associations

| Concept Pair          | Association description                                      | Association name |
| --------------------- | ------------------------------------------------------------ | ---------------- |
| Recorder-Translator   | Recorder pass the melody to translator 					   | provides melody  |
| Translator-Editor     | Translator pass the notations to Translator-Editor		   | provides melody  |

## Attributes

| Concept            | Attributes      | Attribute Description                                    |
| ------------------ | --------------- | -------------------------------------------------------- |
| Recorder           | sound data      | sound data of the melody	                              |
