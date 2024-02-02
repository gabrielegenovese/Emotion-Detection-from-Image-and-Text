#!/bin/python

import os
import csv
import random

reponame = "emotion-detection-from-image-and-text"
basepath = os.path.join(os.getcwd().split(reponame)[0], reponame)
trainpath = os.path.join(basepath, "data/raw/train_ekmann.csv")
imagepath = os.path.join(
    basepath,
    "data/raw/emotion_facial_images/train",
)
newfilepath = os.path.join(
    basepath,
    "data/processed/text_image_emotion.csv",
)


def get_images_name(folder):
    try:
        if not os.path.exists(folder):
            raise FileNotFoundError(f"Folder '{folder}' does not exist.")

        file_names = [
            f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))
        ]
        file_names = list(
            map(lambda x: os.path.join(folder, x).split(reponame)[1][1:], file_names)
        )

        return file_names
    except Exception as e:
        return f"Error: {str(e)}"


def create_dataset_from_emotion(csvfile, emotion):
    emotiondirpath = os.path.join(imagepath, emotion)
    filenames = get_images_name(emotiondirpath)
    random.shuffle(filenames)
    res = []
    counter = 0
    for s in csvfile:
        if s[1] == emotion:
            res.append([s[0], filenames[counter], emotion])
            counter += 1
        if counter >= len(filenames):
            break
    return res


with open(trainpath, newline="") as train_ekmann_f:
    train_ekmann_csv = csv.reader(train_ekmann_f, delimiter=",", quotechar='"')
    csvfile = []
    for s in train_ekmann_csv:
        csvfile.append(s)

    final_list = []
    dir_list = os.listdir(imagepath)
    for emotion_dir in dir_list:
        final_list += create_dataset_from_emotion(csvfile, emotion_dir)

    with open(newfilepath, "w", encoding="UTF8") as newfile_csv:
        spamwriter = csv.writer(newfile_csv, delimiter=",")
        for line in final_list:
            spamwriter.writerow(line)
