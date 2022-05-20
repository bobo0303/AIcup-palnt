# AICUP-plant (TEAM_240)
組員: louis52099, julian135707, wiwi61666166  
Only for AI CUP group and private notes

---
## 農地作物現況調查影像辨識競賽 - 春季賽：AI作物影像判釋
![image](https://i.imgur.com/TXrb6aw.jpeg)
---

## 文件結構說明

- `applications`: 包括`test.py, train.py, convert.py`等應用，提供給`main.py`調用；
- `checkpoints`: 訓練好的模型文件保存目錄；
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

## 預訓練與模型載點

- `checkpoints` & `pretrained`: 目錄內 `Readme.md` 附有載點雲端；

---

## 使用說明

### 數據準備

在文件夾`data`下放數據，分成三個文件夾: `train/test/val`，對應 訓練/測試/驗證 數據文件夾；
每個子文件夾下，依據分類類別每個類別建立一個對應的文件夾，放置該類別的圖片。

數據準備完畢後，使用`utils/check_images.py`腳本，檢查圖像數據的有效性，防止在訓練過程中遇到無效圖片中止訓練。

最終大概結構為：
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

### 部分重要配置參數說明

針對`config.py`裡的部分重要參數說明如下：

- `--data`: 數據集根目錄，下麵包含`train`, `test`, `val`三個目錄的數據集，默認當前文件夾下`data/`目錄；
- `--image_size`: 輸入應該為兩個整數值，預訓練模型的輸入時正方形的，也就是[224, 224]之類的；
實際可以根據自己需要更改，數據預處理時，會將圖像 等比例resize然後再padding（默認用0 padding）到 指定的輸入尺寸。
- `--num_classes`: 分類模型的預測類別數；
- `-b`: 設置batch size大小，默認為256，可根據GPU顯存設置；
- `-j`: 設置數據加載的進程數，默認為8，可根據CPU使用量設置；
- `--criterion`: 損失函數，一種使用PyTorch自帶的softmax損失函數，一種使用我自定義的sigmoid損失函數；
sigmoid損失函數則是將多分類問題轉化為多標籤二分類問題，同時我增加了幾個如GHM自定義的sigmoid損失函數，
可通過`--weighted_loss --ghm_loss --threshold_loss --ohm_loss`指定是否啟動；
- `--lr`: 初始學習率，`main.py`裡我默認使用Adam優化器；目前學習率的scheduler我使用的是`LambdaLR`接口，自定義函數規則如下，
詳細可參考`main.py`的`adjust_learning_rate(epoch, args)`函數：
```
~ warmup: 0.1
~ warmup + int([1.5 * (epochs - warmup)]/4.0): 1, 
~ warmup + int([2.5 * (epochs - warmup)]/4.0): 0.1
~ warmup + int([3.5 * (epochs - warmup)]/4.0) 0.01
~ epochs: 0.001
```
- `--warmup`: warmup的迭代次數，訓練前warmup個epoch會將 初始學習率*0.1 作為warmup期間的學習率；
- `--epochs`: 訓練的總迭代次數；
- `--aug`: 是否使用數據增強，目前默認使用的是自定義的數據增強方式：`dataloader/my_augment.py`；
- `--mixup`: 數據增強mixup，默認 False；
- `--multi_scale`: 多尺度訓練，默認 False；
- `--resume`: 權重文件路徑，模型文件將被加載以進行模型初始化，`--jit`和`--evaluation`時需要指定；
- `--jit`: 將模型轉為JIT格式，利於部署；
- `--evaluation`: 在測試集上進行模型評估；
- `--knowledge`: 指定數據集，使用教師模型（配合resume選型指定）對該數據集進行預測，獲取概率文件（知識)，
生成的概率文件路徑為`data/distill.txt`，同時生成原始概率`data/label.txt`;
- `--distill`: 模型蒸餾（需要教師模型輸出的概率文件)，默認 False，
使用該模式訓練前，需要先啟用`--knowledge train --resume teacher.pth`對訓練集進行測試，生成概率文件作為教師模型的概率；
概率文件形式為`data`路徑下`distill*.txt`模式的文件，有多個文件會都使用，取均值作為教師模型的概率輸出指導接下來訓練的學生模型；
- `--visual_data`: 對指定數據集運行測試，並進行可視化；
- `--visual_method`: 可視化方法，包含`cam`, `grad-cam`, `grad-camm++`三種；
- `--make_curriculum`: 製作課程學習的課程文件；
- `--curriculum_thresholds`: 不同課程中樣本的閾值；
- `--curriculum_weights`: 不同課程中樣本的損失函數權重；
- `--curriculum_learning`: 進行課程學習，從`data/curriculum.txt`中讀取樣本權重數據，訓練時給對應樣本的損失函數加權；

參數的詳細說明可查看`config.py`文件。

---
## Train
1. 資料夾 `data` 由上述引導放置資料
2. `config.py` 由上述引導設定 (重點data、arch、num_classes、train、epochs、warmup、evaluate、resume、)
3. 運行`main.py` 開始訓練

## Test  
Method1:
1. 若 `config.py --evaluate` 設定為 `True` 則會在訓練完畢後自動檢測 Test 資料夾內圖片
2. 生成log檔也可重複觀看結果資料以及準確度
3. 生成之 `ConfusionMatrix.png` 也可以確認測試資料之準確度  

Method2:  
可以使用 `demos` 目錄下的 `main.py` 測試圖片 (未測試)

## Ensanble 
1. 將三者模型測試出的結果 `.log` 檔運行 `write_csv.py` 將log檔轉換成讀取用的csv  
    - 將各模型分兩類，圖片分類檔 & 純置信度檔 (共六個csv)
2. 運行 `read_csv.py` 讀取csv檔生成最後結果

---
## Result (ConfusionMatrix)  
- Model1 (efficientnet_b4_10) 資料為訓練資料分割5%
![image](https://i.imgur.com/V2gEWRK.png)

- Model2 (efficientnet_b4_10+10) 資料為訓練資料分割5%
![image](https://i.imgur.com/JYN1VSq.png)

- Model3 (efficientnet_b5_20) 資料為訓練資料分割5%
![image](https://i.imgur.com/mJy7MKb.png)

- #失敗例子# (efficiennet_b6_10) 資料為訓練資料分割5%
  - 未做資料增強 & 模型太大 Overfitting (少數類別準確率極低)
![image](https://i.imgur.com/2Dtfd0O.png)



---

## Reference

[ilaydaDuratnir/python_image_enhancement](https://github.com/ilaydaDuratnir/python_image_enhancement)

[zheng-yuwei/PyTorch-Image-Classification](https://github.com/zheng-yuwei/PyTorch-Image-Classification)

[d-li14/mobilenetv3.pytorch](https://github.com/d-li14/mobilenetv3.pytorch)

[lukemelas/EfficientNet-PyTorch](https://github.com/lukemelas/EfficientNet-PyTorch)

[zhanghang1989/ResNeSt](https://github.com/zhanghang1989/ResNeSt)

[yizt/Grad-CAM.pytorch](https://github.com/yizt/Grad-CAM.pytorch)

---
## Contact
If you have any question, feel free to contact wiwi61666166@gmail.com


