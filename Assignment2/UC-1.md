## Use Case - Config (UC-1)

**Related Requirements:** REQ1, RE2, REQ6, REQ7 & REQ9

**Initiating Actor:** User

**Actor's Goal:** To configure the tonality and the style so as to get the generated melody. Or to specify the first piece of music to generate melody.

**Participating Actor:** Visualizer, Generator

**Preconditions:** None.

**Postconditions:** The melody is generated according to decision the user made.

**Flow of Event for Main Success Scenario:**

→ 1. **User** selects the options from the tonality, duration and style lists.

→ 2. **System** (a) saves the choices made by the **User **and (b) sends the data to the **Generator** to generate music. 

**Flow of Events for Extensions (Alternate Scenarios):** 

← 1. **User** (a) clicks “Import” button to import the first piece of melody from MIDI file, or (b) notes the melody using numbered musical notations.

← 2. **Visualizer** displays the user’s input. 

→ 3. **System** (a) saves the file made by the **User **and (b) sends the data to the **Generator** to generate music. 

## Responsibilities

| Responsibility Description               | Concept Name |
| ---------------------------------------- | ------------ |
| Rs1. Accept choices that what the tonality, duration and the style to be. | Recorder     |
| Rs2.  Send the choice to Generator.      | Sender       |
| Rs3.  Load the music data from MIDI file. | Loader       |
| Rs4. Translate the MIDI data to become the numbered musical notations. | Translator   |
| Rs5.  Graphical interface allowing the user to edit the numbered musical notations. | Editor       |

## Associations

| Concept Pair      | Association description                  | Association name           |
| ----------------- | ---------------------------------------- | -------------------------- |
| Recorder↔Sender   | Recorder passes the user’s choice to Sender to store the data. | provides data              |
| Loader↔Translator | Loader passes the MIDI data to Translator. | provides MIDI data         |
| Translator↔Editor | Translator passes the musical notations to Editor. | provides musical notations |
| Editor↔Sender     | Editor passes the final edition MIDI data to Sender. | provides data              |

## Attributes

| Concept  | Attributes                 | Attribute Description                    |
| -------- | -------------------------- | ---------------------------------------- |
| Recorder | default configuration      | The possible tonality, duration and the musical style settings are defaulted. |
|          | archiver                   | User's choices are archived.             |
| Sender   | pass data                  | The configuration is passed from Recorder to Generator. |
| Loader   | MIDI data                  | MIDI data which is loaded from files.    |
| Editor   | numbered musical notations | User's noted numbered musical notations. |

