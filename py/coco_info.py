# -*- coding: utf-8 -*-

"""
@date: 2023/4/8 下午3:36
@file: coco_info.py
@author: zj
@description: 判断coco数据集中annotations列表中的id/image_id/category_id的取值范围

category_id：从1开始取值
image_id：等同于images列表中的id。另外，从计算结果可知，并不是所有图像均有bbox标注
id: 每个bbox一个独立id
"""

import json
from tqdm import tqdm

# with open("/data/sdd/coco/coco/annotations/instances_val2017.json", 'rb') as f:
with open("/data/sdd/coco/coco/annotations/instances_train2017.json", 'rb') as f:
    data = json.load(f)

anno_id_list = list()
anno_image_id_list = list()
anno_cls_id_list = list()

for item in tqdm(data['annotations']):
    if item['id'] not in anno_id_list:
        anno_id_list.append(item['id'])
    if item['image_id'] not in anno_image_id_list:
        anno_image_id_list.append(item['image_id'])
    if item['category_id'] not in anno_cls_id_list:
        anno_cls_id_list.append(item['category_id'])

print(len(data['images']))
print(len(data['annotations']))

# print(sorted(anno_id_list))
print(len(anno_id_list))

# print(sorted(image_id_list))
print(len(anno_image_id_list))

# print(sorted(cls_id_list))
print(len(anno_cls_id_list))

image_id_list = list()
for item in tqdm(data['images']):
    if item['id'] not in image_id_list:
        image_id_list.append(item['id'])

for id in anno_image_id_list:
    if not id in image_id_list:
        print(id)
