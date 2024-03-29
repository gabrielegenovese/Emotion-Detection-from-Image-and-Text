# Emotion Detection from Image and Text

## Overview

The main goal is to test the behaviour of a neural network in deteting the emotion of an image combined with some text.

## Setup and usage

1. Clone the repository: `git clone [repository link]`
2. If you want to recreate the dataset follow the next steps
3. Download the image dataset from this [link](https://www.kaggle.com/datasets/msambare/fer2013?resource=download)
4. Use `./src/scripts/custom_unzip.sh [/path/to/archive.zip]` to unzip the images' archive correctly
5. If you want to regenerate the processed dataset, use `./src/scripts/merge_dataset.py`
6. zip all the data with `zip -r data.zip data` and upload the archive on Google Drive
7. Use the notebook on Google Colab to run the project

## Dataset

The data used in this project are the following:

- **Raw Data**: location of the _Ekmann text dataset_ and _Kaggle's image dataset_
- **Processed Data**: location of the custom dataset created with a script

## Documentation

The documentation of the project is available [here](https://gabrielegenovese.github.io/Emotion-Detection-from-Image-and-Text/main.pdf) or you can generete it with:

```bash
cd docs
pdflatex main.tex
pdflatex main.tex
```

## Future works

- Use a confusion matrix to really understand precision and recall metrics
- Create a custom layer to set a weight to the text and image input for each emotion (i.e. text should be more weightened than image for surprise)
- Explore ramdoness for image data and for emotion (see `random-emotion` branch)

## Contact

Gabriele Genovese - gabriele.genovese2@studio.unibo.it

Erik Koci - erik.koci@studio.unibo.it
