# -*- coding: utf-8 -*-

"""
@Time    : 2023/12/30 14:29
@File    : show_image.py
@Author  : zj
@Description:
"""
import json
import os
import cv2
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Show Image")
    parser.add_argument('-i', '--image', metavar='IMAGE', type=str, default='assets/cocolike/000006.jpg',
                        help='COCOLike IMAGE path.')
    parser.add_argument('-j', '--json', metavar='JSON', type=str, default='assets/cocolike/000006.json',
                        help='COCOLike JSON path.')

    args = parser.parse_args()
    print("args:", args)
    return args


def parse_coco(json_path):
    assert os.path.isfile(json_path), json_path

    with open(json_path, 'r') as f:
        label_list = json.load(f)

    print(f"label_list: {label_list}")
    return label_list


def main(args):
    image_name = os.path.basename(args.image)
    image = cv2.imread(args.image, cv2.IMREAD_COLOR)

    label_list = parse_coco(args.json)
    for item in label_list:
        assert isinstance(item, dict), item
        assert image_name == item['image']
        for anno in item['annotations']:
            label_name = anno['label']
            x_c = anno['coordinates']['x']
            y_c = anno['coordinates']['y']
            box_w = anno['coordinates']['width']
            box_h = anno['coordinates']['height']

            x_min = int(x_c - box_w / 2)
            y_min = int(y_c - box_h / 2)
            x_max = int(x_c + box_w / 2)
            y_max = int(y_c + box_h / 2)

            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 1)

    cv2.imshow("image", image)
    cv2.waitKey(0)


if __name__ == '__main__':
    args = parse_args()
    main(args)
