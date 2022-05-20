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
