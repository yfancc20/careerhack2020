import csv
import json
import numpy as np
import pandas as pd
import cv2
import difflib
import glob


INPUT_NUM = 334
KEYWORD = ':'
KEYWORD_RATIO = 0

def check_keyword(d):
    ratio = difflib.SequenceMatcher(None, KEYWORD.lower(), d['text'].lower()).ratio()
    if ratio > KEYWORD_RATIO:
        return True
    else:
        return False

def process_by_lines(results, data, input_num):
    flag = False
    for page in data['recognitionResults']:
        for line in page['lines']:
            for word in line['words']:
                if flag:
                    label = 0
                    b = word['boundingBox']
                    points = np.array([[b[0], b[1]],[b[2], b[3]],[b[4], b[5]],[b[6], b[7]]], np.int32)
                    cv2.polylines(src_img, pts=[points], isClosed=True, color=(0, 0, 255), thickness=2)

                    results.append({
                        'input': input_num,
                        'text': word['text'],
                        'boundingBox': word['boundingBox'],
                        'label': label,
                    })
                    flag = False
                    continue

                flag = False

                if check_keyword(word):
                    flag = True
                    label = 0
                    b = word['boundingBox']
                    points = np.array([[b[0], b[1]],[b[2], b[3]],[b[4], b[5]],[b[6], b[7]]], np.int32)
                    cv2.polylines(src_img, pts=[points], isClosed=True, color=(0, 0, 255), thickness=2)
                else:
                    label = 99

                results.append({
                    'input': input_num,
                    'text': word['text'],
                    'boundingBox': word['boundingBox'],
                    'label': label,
                })

    with open('Lines/lines_' + '{:04d}'.format(num) + '.json', 'w') as f:
        json.dump(results, f)
        f.close()

    return results

for num in range(INPUT_NUM + 1):
    num_str = '{:04d}'.format(num)
    image_file = '../Testing_data/labeling_' + num_str + '.jpg'
    src_img = cv2.imread(image_file)
    

    filename = '../Testing_data/labeling_' + '{:04d}'.format(num) + '.json'
    df = pd.read_json(filename)


    results = []
    results = process_by_lines(results, df, num)

    cv2.imwrite('Draw/labeling_' + num_str + '.jpg', src_img)

    


# df.to_csv('preprocessing.csv')
    

# with open('preprocessing.json', 'w') as f:
#     json.dump(results, f)



# print(results)