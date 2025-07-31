# 中文文字生成模型（LSTM）

這是一個使用 PyTorch 建立的中文文字生成模型，分別以「字元」與「詞語」為單位訓練，輸入開頭文字或詞語後可自動產生續寫內容。

---

## 📚 專案特色

- 🧠 使用 LSTM 架構學習中文語料
- 📝 提供 **逐字版本** 及 **逐詞版本**
- 🔤 起始輸入可自訂，讓模型自由生成故事

---

## 📁 專案結構

```
textgen-lstm/
├── char_version.py       # 不使用 jieba，逐字訓練版本
├── word_version.py       # 使用 jieba 分詞的逐詞訓練版本
├── requirements.txt      # 需要安裝的 Python 套件
└── README.md             # 專案說明文件
```

---

## 🛠️ 安裝套件

```bash
pip install -r requirements.txt
```

---

## 🚀 執行方式

### 🔹 逐字版本（char-level，不需 jieba）
```bash
python char_version.py
```

### 🔹 逐詞版本（word-level，需要 jieba）
```bash
python word_version.py
```

---

## 🔮 產生結果範例

```text
🔮 生成結果：
臺北，一如往常地下著毛毛細雨。捷運站的人潮不多也不少，林昀青站在人群中...
```

---

## 🔧 可調參數

| 參數 | 說明 |
|------|------|
| `seq_length` | 輸入序列長度（字數或詞數） |
| `hidden_size` | LSTM 隱藏層維度 |
| `num_layers` | LSTM 疊加層數 |
| `start` / `start_words` | 起始輸入（文字或詞語） |

---

## 🪪 授權 License

本專案以 MIT License 授權，可自由使用與修改。

---

## ✍️ 作者

- 原始故事、程式設計：你自己 💡  
- 歡迎點星星 ⭐、Fork、留言交流！
