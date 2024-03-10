#!/bin/python

import os
import csv
import random

reponame = "emotion-detection-from-image-and-text"
basepath = os.path.join(os.getcwd().split(reponame)[0], reponame)
trainpath = os.path.join(basepath, "data/raw/train_ekmann.csv")
testpath = os.path.join(basepath, "data/raw/test_ekmann.csv")
imagepath = os.path.join(
    basepath,
    "data/raw/emotion_facial_images/train",
)
imagetestpath = os.path.join(
    basepath,
    "data/raw/emotion_facial_images/test",
)
newfilepath = os.path.join(
    basepath,
    "data/processed/text_image_emotion_random.csv",
)

emotions_list = ["anger", "disgust", "fear", "neutral", "sadness", "surprise", "joy"]


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


def create_dataset_from_emotion(basepath, csvfile, emotion):
    emotiondirpath = os.path.join(basepath, emotion)
    filenames = get_images_name(emotiondirpath)
    random.shuffle(filenames)
    res = []
    counter = 0
    for s in csvfile:
        if s[1] == emotion:
            res.append([s[0], filenames[counter], random.choice(emotions_list)])
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
    # final_list = [["text","image","emotion"]]
    dir_list = os.listdir(imagepath)
    for emotion_dir in dir_list:
        final_list += create_dataset_from_emotion(imagepath, csvfile, emotion_dir)
    
    with open(testpath, newline="") as test_ekmann_f:
        test_ekmann_csv = csv.reader(test_ekmann_f, delimiter=",", quotechar='"')
        csvfile = []
        for s in test_ekmann_csv:
            csvfile.append(s)
            
        dir_list = os.listdir(imagetestpath)
        for emotion_dir in dir_list:
            final_list += create_dataset_from_emotion(imagetestpath, csvfile, emotion_dir)

        with open(newfilepath, "w", encoding="UTF8") as newfile_csv:
            spamwriter = csv.writer(newfile_csv, delimiter=",")
            for line in final_list:
                spamwriter.writerow(line)
