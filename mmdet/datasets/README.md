# The Evaluation about SODA-D Dataset

With regard to the evaluation, we'd like to bring two important points to your attention:
 - The evaluation is performed on the original images (**NOT ON** the splitted images).
 - The `ignore` regions will not be used in the evaluation phase.

Hence you need to filter `ignore` annotations in the `val.json` and `test.json` in the rawData directory to get `val_wo_ignore.json` and `test_wo_ignore.json` for final performance evaluation. Finally, you may have the following folder sturcture:

```none
SODA-D
├── rawData
│   ├── Images
│   ├── Annotations
│   │   ├── train.json
│   │   ├── train_wo_ignore.json
│   │   ├── val.json
│   │   ├── val_wo_ignore.json
│   │   ├── test.json
│   │   ├── test_wo_ignore.json
├── divData
│   ├── Images
│   │   ├── train
│   │   ├── val
│   │   ├── test
│   ├── Annotations
│   │   ├── train.json
│   │   ├── val.json
│   │   ├── test.json
```
