import csv
import json
import numpy as np
import pandas as pd


INPUT_NUM = 127

def process_data(data):
    result = []
    for page in data['recognitionResults']:
        for line in page['lines']:
            for word in line['words']:
                result.append({
                    'text': word['text'],
                    'boundingBox': word['boundingBox']
                })
    return result

def process_data_to_csv(results, data, input_num):
    for page in data['recognitionResults']:
        for line in page['lines']:
            for word in line['words']:
                results.append({
                    'input': input_num,
                    'text': word['text'],
                    'boundingBox': word['boundingBox']
                })

    with open('Words/words_' + '{:04d}'.format(num) + '.json', 'w') as f:
        json.dump(results, f)
        f.close()
    results.append({'input': filename, 'words': words})
    f.close()

    return results

def process_by_lines(results, data, input_num):
    for page in data['recognitionResults']:
        for line in page['lines']:
            results.append({
                'input': input_num,
                'text': line['text'],
                'boundingBox': line['boundingBox']
            })

    with open('Lines/lines_' + '{:04d}'.format(num) + '.json', 'w') as f:
        json.dump(results, f)
        f.close()

    return results

for num in range(INPUT_NUM + 1):
    results = []
    filename = 'Input/labeling_' + '{:04d}'.format(num) + '.json'
    df = pd.read_json(filename)

    results = process_by_lines(results, df, num)

    


# df.to_csv('preprocessing.csv')
    

# with open('preprocessing.json', 'w') as f:
#     json.dump(results, f)



# print(results)