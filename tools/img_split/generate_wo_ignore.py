""" Please enrue this script is in the rawData directory """

import os.path as osp
import json
import copy

modes = ['train', 'val', 'test']
for mode in modes:
    jsonPth = osp.join("Annotations", f'{mode}.json')
    jsonFile = json.load(open(jsonPth))
    jsonRes = copy.deepcopy(jsonFile)
    anns = jsonFile['annotations']
    annotations = list()
    for ann in anns:
        if ann['category_id'] == 10:
            continue
        annotations.append(ann)
    jsonRes['annotations'] = annotations
    json.dump(jsonRes, open(osp.join("Annotations", f'{mode}_wo_ignore.json'), "w"), indent=4)
