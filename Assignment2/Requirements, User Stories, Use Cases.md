# Assignment 2
## Requirements

| Identifier | Priority | Requirement                                                  |
| ---------- | -------- | ------------------------------------------------------------ |
| REQ1       | 5        | The generator could generate music automatically.            |
| REQ2       | 5        | The user can specify the musical style, tonality and duration. |
| REQ3       | 1        | The program allows trainer to train the generation model, adjust the parameters for generations and adjust the configurations include musical style, tonality and duration. |
| REQ4       | 5        | The program could export the generated music in the MIDI format. |
| REQ5       | 4        | The program could export the generated music as audio file.  |
| REQ6       | 2        | The program allows user to create music by using numbered musical notation to generate the melody. |
| REQ7       | 3        | The generator could generate music according to a piece of music. |
| REQ8       | 1        | The generator could visualize the generated music.           |
| REQ9       | 3        | The program allows user import MIDI file.                    |
| REQ10      | 2        | The program allows user to tag the unsatisfactory part in the generated music and regenerate. |

## User Stories

| Identifier | User Story                                                   | Size      |
| ---------- | ------------------------------------------------------------ | --------- |
| ST-1       | As a user with no music knowledge, I can generate my music in one-click operation. | 4 points  |
| ST-2       | As a user with no music knowledge, I can generate music in my favorite style. | 6 points  |
| ST-3       | As a user with basic music knowledge,I can generate music in my specified tornality. | 7 points  |
| ST-4       | As a user with rich music knowledge, I can specify the first piece of music, and generate the whole melody with the help of the generator. | 9 points  |
| ST-5       | As a user with rich music knowledge, I can audition the generated melody, mark the unsatisfactory part and let the program regenerate. | 10 points |
| ST-6       | As a trainer, I can train models, adjust the parameters and modify the configuration list. | 5 points  |

## Use Cases

| Actor      | Actor's Goal                                                 | Use Case Name   |
| ---------- | ------------------------------------------------------------ | --------------- |
| User       | To configure the tonality and the style so as to get the generated melody. Or to specify the first piece of music to generate melody. | Config (UC-1)  |
| Trainer    | To train the model based on collected MIDI files, and adjust the parameters which are used to generate the melody and be added into configuration list. | Train (UC-3)    |
| Generator  | To generate the melody based on the configurations.          | UC-1            |
| User       | To audition the generated melody and tag the unsatisfactory parts which need to be regenerated. | Audition (UC-4) |
| Visualizer | To visualize the generated melody, the current playing position and the tagged parts. | UC-4            |
| User       | To save the generated melogy as MIDI or audio files.         | Save (UC-5)     |

​                                                                             
