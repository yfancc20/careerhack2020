#!/bin/sh

# Generate lines_xxxx.json under Lines_with_label
cd src 
python3 preprocessing.py

cd ..

# Copy draw images into framework
cp -r src/Draw/ apps/public/input

# Copy the result json into framework
cp -r src/Lines/ apps/storage/json/

# Copy the testing json files into framework
cp -r Testing_data/ apps/storage/input/