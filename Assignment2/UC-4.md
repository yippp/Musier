## User Case Audiction(UC-4)

**Related Requirements:** REQ8 & REQ9

**Initiating Actor:** User

**Actor's Goal:** To audition the genrated melody and tag the unsatisfactory part.

**Participating Actor:** Visualizer

**Preconditions:** The generator has generated a melody.

**Postconditions:** The program save the melody.

**Flow of Event for Main Success Scenario:**

→ 1. **User** click the button "Play"

← 2. **Visulizer** (a) play the melody and (b) visulize the melody in the graphic interface 

**Flow of Events for Extensions (Alternate Scenarios):** 

2a. User find out some unsatisfactory part in the melody.

→ 1. **User** tags the unsatisfactory part 

← 2. **Visulizer** send the tag information to the **genetaor**

→ 3. **Generator** regenerate the melody 

← 4. **User** (a) audiction the renegerated melody and (b) visualize the melody

## Responsibilities

| Responsibility Description                                   | Concept Name       |
| ------------------------------------------------------------ | ------------------ |
| Rs1. Recive the generated melody from generator.             | Reciver            |
| Rs2. Visulize the generated melody.                          | Visulizer          |
| Rs3. Play the melody.                                        | Player             |
| Rs4. Recive the unsatisfactory tags from user.               | Tag                |
| Rs5. Request the generator to regenerate the unsatisfactory part. | Regenerate Request |

## Associations

| Concept Pair          | Association description                                      | Association name |
| --------------------- | ------------------------------------------------------------ | ---------------- |
| Reciver↔Visulizer     | Reciver passes the recived melody to visulizer to visulize the melody. | provides melody  |
| Reciver↔Player        | Reciver passes the recived melody to plaer to play the melody. | provides melody  |
| Tag↔Regeneate Request | Tag passes the informations that which parts are needed to regenerate to to the generator. | provide tag data |

## Attributes

| Concept            | Attributes      | Attribute Description                                    |
| ------------------ | --------------- | -------------------------------------------------------- |
| Reciver            | config          | Style, tonality and duration.                            |
| Visualizer         | music score     | Visulize the melody.                                     |
|                    | current moment  | Visulize the current moment in the score during playing. |
| Tag                | tag information | Store the start and end position of each tagged part.    |
| Regenerate Request | tag information | Copied from tag; send the information to generator.      |

