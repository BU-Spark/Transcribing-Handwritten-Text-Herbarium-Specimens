# IAM Dataset Handwritten Text Recognition 

![](https://img.shields.io/badge/python-3.6.5-green.svg?style=flat)  ![](https://img.shields.io/badge/tensorflow-1.12-orange.svg?style=flat)

## Table of Contents

- [Objective](#objective)
- [Installation](#installation)
- [Dataset](#dataset)
- [Information about model](#information-about-model)
- [References](#references)

## Objective

The objective of this project is to transcribe the handwritten text on images containing herbarium specimens. Herbarium specimens are the dried plants. These plants are stored in paper. Now this paper other than plants also contains different text information. As part of this project I was focused on particular information we called as a label on the image. This label contains the name of the curator, institution to which it belongs, species/category plant belongs and it’s collection date. A handful of these images have labels which are handwritten and date back to the early 20th century. The main reasons why this transcription is important:
* The text on the images containing the label is not in very readable format. So to make this information more readable such that it can reach a wider population even if it is in the researcher community, transcription is important.

* There is some text which has faded away. Now these labels contain information which is useful to researchers in their further work. By transcribing these information we want to preserve the information we currently have from these labels before most of it is lost. Currently transcription is being done manually which requires a lot of manual effort time as well as financial investment. 

We want to make this process automated which requires the least manual intervention.

## Installation

1. Clone this repository
2. Install the required packages mentioned in requirement.txt
3. Download the data as mentioned in [Dataset](#dataset) section (This is only required if training or validating model, not for testing)
4. Go to the model/ directory and unzip the file model.zip (pre-trained on the IAM dataset). Take care that the unzipped files are placed directly into the model/ directory and not some subdirectory created by the unzip-program.
5. To train/validate/test follow the instructions mentioned [Information about model](#information-about-model) section

## Dataset

Given the complexity of the Herbarium Dataset, I started work on an IAM dataset which contains images having only handwritten text. 

Downloaded dataset is also present in the below path. Copy all the files under the data folder of the cloned repository.

```console
/restricted/projectnb/cs501t2/Shubhangi/Herbarium_Project/Dataset/IAM/data
```

Alternatively, data can be downloaded from the host website. Follow these instructions to get the dataset:

1. Register for free at this [website](http://www.fki.inf.unibe.ch/databases/iam-handwriting-database).
2. Download `words/words.tgz`.
3. Download `ascii/words.txt`.
4. Put `words.txt` into the `data/` directory.
5. Create the directory `data/words/`.
6. Put the content (directories `a01`, `a02`, ...) of `words.tgz` into `data/words/`.
7. Go to `data/` and run `python checkDirs.py` for a rough check if everything is ok.


## Information about model

### Overview

The final model consists of 5 CNN layers, 2 RNN (LSTM) layers and the CTC loss and decoding layer. The illustration below gives an overview of the NN (green: operations, pink: data flowing through NN) and here follows a short description:

* The input image is a gray-value image and has a size of 128x32
* 5 CNN layers map the input image to a feature sequence of size 32x256
* 2 LSTM layers with 256 units propagate information through the sequence and map the sequence to a matrix of size 32x80. Each matrix-element represents a score for one of the 80 characters at one of the 32 time-steps
* The CTC layer either calculates the loss value given the matrix and the ground-truth text (when training), or it decodes the matrix to the final text with best path decoding or beam search decoding (when inferring)
* Batch size is set to 512


![nn_overview](./doc/nn_overview.png)

### Training

If you want to train the model from scratch, delete the files contained in the `model/` directory. Otherwise, the parameters are loaded from the last model-snapshot before training begins. Then, go to the `src/` directory and execute 
```console
python main.py --train
```

Below is the training loss obtained:

<img src="./doc/training_loss.jpg" width="550" height="400">

### Validation

After each epoch of training, validation is done on a validation set (the dataset is split into 80% of the samples used for training and 20% for validation as defined in the class `DataLoader`). If you only want to do validation given a trained NN, go to the `src/` directory and execute 
```console
python main.py --validate
```

Below is the validation accuracy plot:

<img src="./doc/validation_accuracy.jpg" width="500" height="400">

### Testing

To test the model an image is required in either png or jpeg format as input. If no image is provided, by default model will return the recognized text with probability on the image present in `src/` directory (test.png). To test the model go to the `src/` directory and execute 

```console
python main.py --test_folder="<path to test image>"
```
Sample for test_folder parameter:

`"restricted/projectnb/cs501t2/Shubhangi/Herbarium_Project/Dataset/IAM/src/test.png"`

To test the model on default image i.e test.png present in `src` directory , go to the `src/` directory and execute 
```console
python main.py 
```
## References

Code has been extended from the below repo:

[IAM Dataset](https://github.com/githubharald/SimpleHTR)


