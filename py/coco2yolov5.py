# -*- coding: utf-8 -*-

"""
@date: 2023/3/27 下午10:09
@file: voc2yolov5.py
@author: zj
@description:

>>>python coco2yolov5.py /home/zj/data/coco ./coco2yolov5-train --name train2017
>>>python coco2yolov5.py /home/zj/data/coco ./coco2yolov5-val --name val2017
"""
import argparse
import shutil

import cv2
import os.path

import numpy as np
from numpy import ndarray
from tqdm import tqdm

from pycocotools.coco import COCO


def parse_args():
    parser = argparse.ArgumentParser(description="COCO2YOLOv5")
    parser.add_argument('src', metavar='SRC', type=str, help='Coco Dataset Root Path.')
    parser.add_argument('dst', metavar='DST', type=str, help='Coco2yolov5 dataset Root Path.')
    parser.add_argument('--name', metavar='NAME', type=str, default='train2017', help='Coco Dataset Name.')

    args = parser.parse_args()
    print("args:", args)
    return args


def x1y1wh2xcycwh(bbox: ndarray):
    assert len(bbox.shape) == 1 and len(bbox) == 4

    x1, y1, w, h = bbox[:4]
    xc = x1 + w / 2
    yc = y1 + h / 2

    return np.array([xc, yc, w, h])


def process(coco: COCO, images_dir: str, dst_root: str):
    dst_images_dir = os.path.join(dst_root, 'images')
    if not os.path.exists(dst_images_dir):
        os.makedirs(dst_images_dir)
    dst_label_dir = os.path.join(dst_root, 'labels')
    if not os.path.exists(dst_label_dir):
        os.makedirs(dst_label_dir)

    ids = coco.getImgIds()
    class_ids = sorted(coco.getCatIds())
    for img_id in tqdm(ids):
        image_name = '{:012}'.format(img_id) + '.jpg'
        image_path = os.path.join(images_dir, image_name)
        assert os.path.isfile(image_path), image_path

        image = cv2.imread(image_path)
        img_h, img_w = image.shape[:2]

        label_list = list()

        anno_ids = coco.getAnnIds(imgIds=[int(img_id)], iscrowd=None)
        annotations = coco.loadAnns(anno_ids)
        for anno in annotations:
            bbox_x1y1 = np.array(anno['bbox'])
            bbox_xcyc = x1y1wh2xcycwh(bbox_x1y1)
            bbox_xcyc[0::2] /= img_w
            bbox_xcyc[1::2] /= img_h

            cate_id = class_ids.index(anno['category_id'])
            xc, yc, box_w, box_h = bbox_xcyc[:4]
            label_list.append([int(cate_id), xc, yc, box_w, box_h])

        # Save
        dst_img_path = os.path.join(dst_images_dir, image_name)
        assert not os.path.exists(dst_img_path), dst_img_path
        shutil.copyfile(image_path, dst_img_path)

        label_name = '{:012}'.format(img_id) + '.txt'
        label_path = os.path.join(dst_label_dir, label_name)
        assert not os.path.exists(label_path), label_path
        np.savetxt(label_path, label_list, fmt='%f', delimiter=' ')


def main(args):
    src_root = os.path.abspath(args.src)
    dst_root = os.path.abspath(args.dst)
    coco_name = args.name

    ann_file_path = os.path.join(src_root, 'annotations', f'instances_{coco_name}.json')
    assert os.path.isfile(ann_file_path), ann_file_path
    images_dir = os.path.join(src_root, 'images', coco_name)
    assert os.path.isdir(images_dir), images_dir

    print(f"Process COCO {coco_name}")
    coco = COCO(annotation_file=ann_file_path)
    process(coco, images_dir, dst_root)


if __name__ == '__main__':
    args = parse_args()
    main(args)
