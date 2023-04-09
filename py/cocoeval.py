# -*- coding: utf-8 -*-

"""
@date: 2023/3/27 下午10:11
@file: eval.py
@author: zj
@description: 
"""

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

annType = 'bbox'
prefix = 'instances'
print('Running demo for *%s* results.' % (annType))

# initialize COCO ground truth api
image_set = 'val'
year = '2012'
annFile = f'/home/zj/data/voc/voc2coco/annotations/{prefix}_{image_set}{year}.json'
cocoGt = COCO(annFile)

# initialize COCO detections api
import json

resFile = f'/home/zj/data/voc/voc2coco/annotations/{prefix}_{image_set}{year}.json'
with open(resFile, 'r') as f:
    resData = json.load(f)

res_list = list()
for item in resData['annotations']:
    res_list.append({
        'image_id': item['image_id'],
        'category_id': item['category_id'],
        'bbox': item['bbox'],
        'score': 0.9
    })

cocoDt = cocoGt.loadRes(res_list)
annsImgIds = [ann['id'] for ann in resData['annotations']]
# print(annsImgIds)
# print(cocoGt.getImgIds())
# print(set(annsImgIds) == set(cocoGt.getImgIds()))

imgIds = sorted(cocoGt.getImgIds())

# running evaluation
cocoEval = COCOeval(cocoGt, cocoDt, annType)
cocoEval.params.imgIds = imgIds
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()
