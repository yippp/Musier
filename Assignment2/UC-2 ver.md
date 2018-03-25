## Use Case - Train (UC-2)

**Related Requirements:** REQ3

**Initiating Actor:** Developer

**Actor's Goal:** To train the generation model, adjust the parameters for generation and adjust the configurations including musical style, tonality and duration.

**Participating Actor:** Generator, Trainer

**Preconditions:** None.

**Postconditions:** The configuration list is updated.

**Flow of Event for Main Success Scenario:**

→ 1. **Developer** puts the MIDI files, which are used to train model, into the train set folder.

→ 2. **Developer** (a) inputs the training settings and (b) adjusts the parameters in the configuration source code.

← 3. **Trainer** (a) prints the training result, (b) generates a piece of melody for testing and (c) saves the trained model.

→ 4. **Developer** updates the configuration lists.

**Flow of Events for Extensions (Alternate Scenarios):** 

2a. Trainer meets error during training.

← 1. **Trainer** prints the errors.

→ 2. **Developer** modifies the training settings.

2b. Generator cannot generate a test case normally.

← 1. **Generator** signals that it cannot generate the melody.

→ 2. **Developer** (a) modifies the training settings or (b) modifies the parameters in the configuration source code.

## Responsibilities

| Responsibility Description                                   | Concept Name |
| ------------------------------------------------------------ | ------------ |
| Rs1. Receive the training settings and parameters.           | Receiver     |
| Rs2. Load the training MIDI files.                           | Loader       |
| Rs3. Process the training data and adjust the model.         | Processor    |
| Rs4. Print the logs including training and generation information. | Printer      |
| Rs5. Update the configuration lists.                         | Updater      |

## Associations

| Concept Pair       | Association description                                      | Association name         |
| ------------------ | ------------------------------------------------------------ | ------------------------ |
| Loader↔Processor   | Loader passes the loaded files to Processor to process the training data. | provides training set    |
| Receiver↔Processor | Receiver passes the received parameters and training settings to Processor to control the training process. | provides parameters      |
| Processor↔Printer   | Processor passes the information for training regeneration to the Printer. | provides training logs   |
| Generator↔Printer   | Generator passes the information for training regeneration to the Printer. | provides generation logs |
| Receiver↔Updater   | Receiver passes the received configurations to Updater to update the configuration lists. | provides configurations  |

## Attributes

| Concept   | Attributes     | Attribute Description                                 |
| --------- | -------------- | ----------------------------------------------------- |
| Processor | settings       | The settings for training.                            |
|           | training set   | The training set used to train the model.             |
|           | model          | The trained model used to generate melody.            |
| Receiver  | parameters     | The inputted parameters.                              |
|           | settings       | The settings for training.                            |
| Loader    | dataset        | The loaded MIDI dataset.                              |
| Printer   | logs           | Store the logs received from Processor and Generator. |
| Updater   | configurations | Configurations received from Receiver                 |
