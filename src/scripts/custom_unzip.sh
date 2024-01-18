#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No arguments supplied. Path to the archive needed"
    exit
fi

unzip -d data/raw/emotion_facial_images $1
base=data/raw/emotion_facial_images/train
mv $base/angry $base/anger
mv $base/happy $base/joy
mv $base/sad $base/sadness