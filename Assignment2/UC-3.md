## Use Case Train (UC-3)

**Related Requirements:** REQ3

**Initiating Actor:** Developer

**Actor's Goal:** To to train the generation model, adjust the parameters for generations and adjust the configurations include musical style, tonality and duration.

**Participating Actor:** Generator

**Preconditions:** None.

**Postconditions:** The configuration list is refreshed.

**Flow of Event for Main Success Scenario:**

→ 1. **Developer** puts the MIDI files that used to train into the train set folder.

→ 2. **Developer** (a) inputs the trainning setting and (b) adjusts the parameters in the configuration source code.

← 3. **Trainer** (a) prints the trainning result, (b) generate a test melody and (c) save the trained model.

→ 4. **Developer** updates the configuration lists.

**Flow of Events for Extensions (Alternate Scenarios):** 

2a. Trainer meets error during training.

← 1. **Trainer** prints the errors.

→ 2. **Developer** modifies the trainning setting.

2b. Generator cannot generate a test melody normally.

← 1. **Generator** signals that it cannot generate the melody.

→ 2. **Developer** (a) modifies the trainning setting or (b) modifies the parameters in the configuration source code.

## Responsibilities

| Responsibility Description                                   | Concept Name |
| ------------------------------------------------------------ | ------------ |
| Rs1. Receive the trainning setting and parameters.           | Receiver     |
| Rs2. Load the trainning MIDI files.                          | Loader       |
| Rs3. Process the training data and adjust the model.         | Processor    |
| Rs4. Print the logs included training and generation information. | Printer      |
| Rs5. Update the configuration lists.                         | Updater      |

## Associations

| Concept Pair       | Association description                                      | Association name         |
| ------------------ | ------------------------------------------------------------ | ------------------------ |
| Loader↔Processor   | Loader passes the loadedfiles to processor to process the training data. | provides training set    |
| Receiver↔Processor | Receiver passes the received parameters and training setting  to processor to control the training process. | provides parameters      |
| Processor↔Logger   | Processor passes the information for trianing regeneration to the logger. | provides training logs   |
| Generator↔Logger   | Generator passes the information for trianing regeneration to the logger. | provides generation logs |
| Receiver↔Updater   | Receiver passes the received configurations to updater to update the configuration lists. | provides configurations  |

## Attributes

| Concept   | Attributes     | Attribute Description                                 |
| --------- | -------------- | ----------------------------------------------------- |
| Processor | setting        | The setting for training.                             |
|           | training set   | The training set used to train the model.             |
|           | model          | The trained model used to generate melody.            |
| Reciever  | parameters     | The inputed parameters.                               |
|           | setting        | The setting for training.                             |
| Loader    | dataset        | The loaded MIDI dataset.                              |
| Printer   | logs           | Store the logs received from processor and generator. |
| Updater   | configurations | Received from Receiver                                |