# AIcup-palnt
Only for AI CUP group and private notes

---

## 文件結構說明

- `applications`: 包括`test.py, train.py, convert.py`等應用，提供給`main.py`調用；
- `checkpoints`: 訓練好的模型文件保存目錄（當前可能不存在）；
- `criterions`: 自定義損失函數；
- `data`: 訓練/測試/驗證/預測等數據集存放的路徑；
- `dataloader`: 數據加載、數據增強、數據預處理（默認採用ImageNet方式）；
- `demos`: 模型使用的demo，目前`classifier.py`顯示如何調用`jit`格式模型進行預測；
- `logs`: 訓練過程中TensorBoard日誌存放的文件（當前可能不存在）；
- `models`: 自定義的模型結構；
- `optim`: 一些前沿的優化器，PyTorch官方還未實現；
- `pretrained`: 預訓練模型文件；
- `utils`: 工具腳本：混淆矩陣、圖片數據校驗、模型結構打印、日誌等；
- `config.py`: 配置文件；
- `main.py`: 總入口；
- `requirements.txt`: 工程依賴包列表；


---

## 使用说明

### 数据准备

在文件夹`data`下放数据，分成三个文件夹: `train/test/val`，对应 训练/测试/验证 数据文件夹；
每个子文件夹下，依据分类类别每个类别建立一个对应的文件夹，放置该类别的图片。

数据准备完毕后，使用`utils/check_images.py`脚本，检查图像数据的有效性，防止在训练过程中遇到无效图片中止训练。

最终大概结构为：
```
- data
  - train
    - class_0
      - 0.jpg
      - 1.jpg
      - ...
    - class_1
      - ...
    - ..
  - test
    - ...
  - val
    - ...
- dataloader
- ...
```

### 部分重要配置参数说明

针对`config.py`里的部分重要参数说明如下：

- `--data`: 数据集根目录，下面包含`train`, `test`, `val`三个目录的数据集，默认当前文件夹下`data/`目录；
- `--image_size`: 输入应该为两个整数值，预训练模型的输入时正方形的，也就是[224, 224]之类的；
实际可以根据自己需要更改，数据预处理时，会将图像 等比例resize然后再padding（默认用0 padding）到 指定的输入尺寸。
- `--num_classes`: 分类模型的预测类别数；
- `-b`: 设置batch size大小，默认为256，可根据GPU显存设置；
- `-j`: 设置数据加载的进程数，默认为8，可根据CPU使用量设置；
- `--criterion`: 损失函数，一种使用PyTorch自带的softmax损失函数，一种使用我自定义的sigmoid损失函数；
sigmoid损失函数则是将多分类问题转化为多标签二分类问题，同时我增加了几个如GHM自定义的sigmoid损失函数，
可通过`--weighted_loss --ghm_loss --threshold_loss --ohm_loss`指定是否启动；
- `--lr`: 初始学习率，`main.py`里我默认使用Adam优化器；目前学习率的scheduler我使用的是`LambdaLR`接口，自定义函数规则如下，
详细可参考`main.py`的`adjust_learning_rate(epoch, args)`函数：
```
~ warmup: 0.1
~ warmup + int([1.5 * (epochs - warmup)]/4.0): 1, 
~ warmup + int([2.5 * (epochs - warmup)]/4.0): 0.1
~ warmup + int([3.5 * (epochs - warmup)]/4.0) 0.01
~ epochs: 0.001
```
- `--warmup`: warmup的迭代次数，训练前warmup个epoch会将 初始学习率*0.1 作为warmup期间的学习率；
- `--epochs`: 训练的总迭代次数；
- `--aug`: 是否使用数据增强，目前默认使用的是我自定义的数据增强方式：`dataloader/my_augment.py`；
- `--mixup`: 数据增强mixup，默认 False；
- `--multi_scale`: 多尺度训练，默认 False；
- `--resume`: 权重文件路径，模型文件将被加载以进行模型初始化，`--jit`和`--evaluation`时需要指定；
- `--jit`: 将模型转为JIT格式，利于部署；
- `--evaluation`: 在测试集上进行模型评估；
- `--knowledge`: 指定数据集，使用教师模型（配合resume选型指定）对该数据集进行预测，获取概率文件（知识)，
生成的概率文件路径为`data/distill.txt`，同时生成原始概率`data/label.txt`;
- `--distill`: 模型蒸馏（需要教师模型输出的概率文件)，默认 False，
使用该模式训练前，需要先启用`--knowledge train --resume teacher.pth`对训练集进行测试，生成概率文件作为教师模型的概率；
概率文件形式为`data`路径下`distill*.txt`模式的文件，有多个文件会都使用，取均值作为教师模型的概率输出指导接下来训练的学生模型；
- `--visual_data`: 对指定数据集运行测试，并进行可视化；
- `--visual_method`: 可视化方法，包含`cam`, `grad-cam`, `grad-camm++`三种；
- `--make_curriculum`: 制作课程学习的课程文件；
- `--curriculum_thresholds`: 不同课程中样本的阈值；
- `--curriculum_weights`: 不同课程中样本的损失函数权重；
- `--curriculum_learning`: 进行课程学习，从`data/curriculum.txt`中读取样本权重数据，训练时给对应样本的损失函数加权；

BTW，在`models/efficientnet/model.py`中增加了`sample-free`的思想，目前代码注释掉了，若需要可以借鉴使用。
`sample-free`主要是我使用bce进行多标签二分类时，我希望任务偏好某些类别，所以在初始某些类别的bias上设置一个较大的数，提高初始概率。
（具体计算公式可参考原论文 Is Sampling Heuristics Necessary in Training Deep Object Detectors）

参数的详细说明可查看`config.py`文件。

---
