# Project Title: Emotion Detection from Image and Text

## Overview
The main goal is to test the behaviour of a neural network in deteting the emotion of an image combined with some text.
The documentation of the project is available [here](https://emotion-detection-from-image-and-text-gabrigeno-0342883c89cf315.gitlab.io/main.pdf).

## Setup and usage
1. Clone the repository: `git clone [repository link]`
2. If you want to recreate the dataset follow the next steps
3. Download the image dataset from this [link](https://www.kaggle.com/datasets/msambare/fer2013?resource=download)
4. Use `./src/scripts/custom_unzip.sh [/path/to/archive.zip]` to unzip the images' archive correctly
5. If you want to regenerate the processed datased, use `./src/scripts/merge_dataset.py`
6. Use the notebook to run the project

## Data
The data used in this project are the following:
- **Raw Data**: location of the Ekmann dataset and Kaggle's image dataset
- **Processed Data**: location of the custom dataset created with a script

## Contact
Gabriele Genovese - gabriele.genovese2@studio.unibo.it

Erik Koci - erik.koci@studio.unibo.it
