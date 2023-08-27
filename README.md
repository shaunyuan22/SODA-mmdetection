## Introduction

This project is based on the open source object detection toolbox [MMDetection](https://github.com/open-mmlab/mmdetection), please refer to [Installation](docs/en/get_started.md/#Installation) for installation instructions first.

The benchmark experiments work with **Python 3.8**, **PyTorch 1.10** and **mmdet 2.23.0**, and corresponding configs can be found at `sodad-benchmarks`.

## Data preparation
The data preparation of SODA-D is a little different from common detection datasets (e.g., COCO, VOC), where a image split processes is necessary before training, and more details please refer to `tools/img_split`.

## Citation

If you use our benchmark in your research, please cite this project.


```bibtex
@article{SODA,
  title={Towards large-scale small object detection: Survey and benchmarks},
  author={Cheng, Gong and Yuan, Xiang and Yao, Xiwen and Yan, Kebing and Zeng, Qinghua and Han, Junwei},
  journal={TPAMI},
  year={2023}
}
```

```bibtex
@article{mmdetection,
  title   = {{MMDetection}: Open MMLab Detection Toolbox and Benchmark},
  author  = {Chen, Kai and Wang, Jiaqi and Pang, Jiangmiao and Cao, Yuhang and
             Xiong, Yu and Li, Xiaoxiao and Sun, Shuyang and Feng, Wansen and
             Liu, Ziwei and Xu, Jiarui and Zhang, Zheng and Cheng, Dazhi and
             Zhu, Chenchen and Cheng, Tianheng and Zhao, Qijie and Li, Buyu and
             Lu, Xin and Zhu, Rui and Wu, Yue and Dai, Jifeng and Wang, Jingdong
             and Shi, Jianping and Ouyang, Wanli and Loy, Chen Change and Lin, Dahua},
  journal= {arXiv preprint arXiv:1906.07155},
  year={2019}
}
```
