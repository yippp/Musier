## Use Case - Audition (UC-3)

**Related Requirements:** REQ8 & REQ10

**Initiating Actor:** User

**Actor's Goal:** To audition the generated melody and tag the unsatisfactory part.

**Participating Actor:** Visualizer, Generator

**Preconditions:** The generator has generated a piece of melody.

**Postconditions:** The program saves the melody.

**Flow of Event for Main Success Scenario:**

→ 1. **User** clicks the button "Play/Pause".

← 2. **Visualizer** (a) plays the melody and (b) visualizes the melody in the graphic interface. 

**Flow of Events for Extensions (Alternate Scenarios):** 

2a. User finds out some unsatisfactory parts in the melody.

→ 1. **User** tags the unsatisfactory parts. 

← 2. **Visualizer** sends the tagged information to the **Generator**.

→ 3. **Generator** regenerates the melody. 

← 4. **User** (a) auditions the renegerated melody and (b) visualizes the melody.

## Responsibilities

| Responsibility Description                                   | Concept Name       |
| ------------------------------------------------------------ | ------------------ |
| Rs1. Receive the generated melody from Generator.            | Receiver           |
| Rs2. Visualize the generated melody.                         | Visualizer         |
| Rs3. Play the melody.                                        | Player             |
| Rs4. Receive the unsatisfactory tags from user.              | Tag                |
| Rs5. Request the Generator to regenerate the unsatisfactory part. | Regenerate Request |

## Associations

| Concept Pair          | Association description                                      | Association name |
| --------------------- | ------------------------------------------------------------ | ---------------- |
| Receiver↔Visualizer   | Receiver passes the received melody to Visualizer to visualize the melody. | provides melody  |
| Receiver↔Player       | Receiver passes the received melody to Player to play the melody. | provides melody  |
| Tag↔Regeneate Request | Tag passes the information for melody regeneration to Generator. | provides tagged data |

## Attributes

| Concept            | Attributes      | Attribute Description                                     |
| ------------------ | --------------- | --------------------------------------------------------- |
| Receiver           | config          | Style, tonality and duration.                             |
|                    | melody          | The generated melody.                                     |
| Visualizer         | music score     | Visualize the melody.                                     |
|                    | current moment  | Display the current position in the score during playing the music. |
| Tag                | tag information | Store the start and end position of each tagged part.     |
| Regenerate Request | tag information | Copied from tag; send the information to Generator.       |


