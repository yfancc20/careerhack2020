import numpy as np
import pandas as pd
import json
import random
import cv2
import difflib

COLORS = [(147, 20, 255), (0, 165, 255), (0, 255, 255),
          (50, 205, 154), (255, 191, 0),
          (50, 205, 154), (255, 191, 0),
          (50, 205, 154), (255, 191, 0), 
          (50, 205, 154), (255, 191, 0),
          (205, 38, 10), (255, 0, 255), (153, 50, 204), (139, 137, 137),
          (156, 156, 156), (178, 223, 223), (139, 0, 0), (0, 139, 139), (255, 187, 255)]

def get_coordinates(label, boxes):
    for b in boxes:
        points = np.array([[b[0], b[1]],[b[2], b[3]],[b[4], b[5]],[b[6], b[7]]], np.int32)
        cv2.polylines(src_img, pts=[points], isClosed=True, color=COLORS[label], thickness=2)
        # if label == 5 or label == 7 or label == 9:
        #     if b[6]-b[4] != 0:
        #         a = int((b[7]-b[5])/(b[6]-b[4])*(1000-b[4]))+b[5]
        #     elif b[6]== b[4]:
        #         a = b[5]
        #     cv2.line(src_img,(b[6],b[7]),(1000,a),COLORS[label],1)

        # pairs = []
        # pairs.append({'x': b[0], 'y': b[1]})
        # pairs.append({'x': b[2], 'y': b[3]})
        # pairs.append({'x': b[4], 'y': b[5]})
        # pairs.append({'x': b[6], 'y': b[7]})
    
        # max_x_pair = max(pairs, key=lambda a:a['x'])
        # pairs.remove(max_x_pair)
        # max_y_pair = max(pairs, key=lambda a:a['y'])
        # pairs.remove(max_y_pair)
        # min_x_pair = min(pairs, key=lambda a:a['x'])
        # pairs.remove(min_x_pair)
        # min_y_pair = min(pairs, key=lambda a:a['y'])
        # pairs.remove(min_y_pair)

        # xy = (
        #     max_x_pair['x'], max_x_pair['y'],
        #     max_y_pair['x'], max_y_pair['y'],
        #     min_x_pair['x'], min_x_pair['y'],
        #     min_y_pair['x'], min_y_pair['y'],
        # )

        # draw.polygon(xy, fill=COLORS[label])
        # draw_new.polygon(xy, fill=COLORS[label])

        # xy = (b[6], b[7], b[4], b[5])
        # draw.line(xy, fill=COLORS[label])
        # draw_new.line(xy, fill=COLORS[label])
        # xy = (b[6], b[7], b[0], b[1])
        # draw.line(xy, fill=COLORS[label])
        # draw_new.line(xy, fill=COLORS[label])
        # xy = (b[2], b[3], b[4], b[5])
        # draw.line(xy, fill=COLORS[label])
        # draw_new.line(xy, fill=COLORS[label])



def check_keyword(keyword, d):
    ratio = difflib.SequenceMatcher(None, keyword, d['text']).ratio()
    if ratio > 0.5:
        return True
    else:
        return False


def processing(data):
    # Get the max label
    labels = []
    for d in data:
        if 'label' not in d:
            continue
        labels.append(d['label'])

    if len(labels):
        max_label = max(labels)
    else:
        max_label = 0

    # Process the data with the same label
    coordinates = []
    i = 0
    while i <= max_label:
        # if i == 0: 
        #     i += 1 
        #     continue
        # if i == 2: break
        bounding_boxes = []
        for d in data:
            if check_keyword(keyword, d):
                d['label'] = 0
                print(d['text'])
            if 'label' not in d:
                continue
            if d['label'] == i:
                bounding_boxes.append(d['boundingBox'])
        
        coordinates = get_coordinates(i, bounding_boxes)
        i += 1
    

start = 0
end = 0
keyword = 'Tax'
for idx in range(start, end + 1):
    num_str = '{:04d}'.format(idx)
    image_file = 'Input/labeling_' + num_str + '.jpg'
    # src_img = Image.open('Input/labeling_' + num_str + '.jpg').convert('RGB')
    # new_img = Image.new('RGB', src_img.size, color = 'white')
    # draw = ImageDraw.Draw(src_img)
    # draw_new = ImageDraw.Draw(new_img)

    src_img = cv2.imread(image_file)

    input_file = 'Lines/lines_' + num_str + '.json'
    with open(input_file) as json_file:
        data = json.load(json_file)
        processing(data)

    cv2.imwrite('Draw/labeling_' + num_str + '.jpg', src_img)
    
    # cv2.imshow('image', src_img)
    # cv2.waitKey(0)
    # src_img.save('Draw/labeling_origin_' + num_str + '.jpg', quality=100)
    # new_img.save('Draw/labeling_' + num_str + '.jpg', quality=100)
