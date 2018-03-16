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

