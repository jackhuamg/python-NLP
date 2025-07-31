# 中文文字生成模型（LSTM）

這是一個使用 PyTorch 建立的簡單中文文字生成模型，採用 LSTM 神經網路架構，透過原創故事文本進行訓練，並自動生成續寫內容。

## 📚 專案特色

- 支援兩種訓練方式：
  - ✅ **逐字（char-level）版本**：不依賴任何斷詞工具，適合入門者。
- 使用者可自訂起始文字，讓模型接續生成內容。
- 完整 Python 程式碼，適合教學、實驗與創作。

## 📁 專案結構

```
textgen-lstm/
├── char_version.py       # 逐字訓練版本（不需 jieba）
├── requirements.txt      # 所需套件
└── README.md             # 專案說明文件
```

## 🛠️ 執行方式

### 1. 安裝套件

```bash
pip install -r requirements.txt
```

### 2. 執行逐字版本（不需 jieba）

```bash
python char_version.py
```

## 🧠 範例輸出

```text
🔮 生成結果：
臺北，一如往常地下著毛毛細雨。捷運站的人潮不多也不少...
```

## 📄 授權條款

本專案以 MIT License 授權，你可自由修改、再發佈。
