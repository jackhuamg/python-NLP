import torch
import torch.nn as nn
import torch.optim as optim
import jieba

# ========== 中文訓練語料 ==========
text = """
臺北，一如往常地下著毛毛細雨。捷運站的人潮不多也不少，林昀青站在人群中，手握著一杯快涼掉的咖啡，眼神飄忽。她正要趕往一家她不是特別喜歡的公司，做著一份她不討厭但也說不上熱愛的工作。

就在列車抵達的時候，一個穿著黃色雨衣的小男孩突然跌倒在月台邊緣。昀青毫不猶豫衝上前，一把將他拉了回來，列車擦身而過，風掀起她的髮絲。

「你沒事吧？」她喘著氣問。

小男孩點點頭，看著她說：「妳是不是本來要搭這班車？」

「是啊，但沒關係，還有下一班。」

小男孩笑了，眼睛亮晶晶的：「妳救了我，妳會有好運的！」

昀青一愣，想笑，卻在下一秒發現那個小男孩不見了。她四處張望，人群來來去去，彷彿什麼都沒發生。

那天，她遲到了半小時。主管臉色不好看，會議也早已結束。但奇妙的是，她竟然沒有被責罵，反而被另一個部門的經理注意到，邀請她參與一個新的專案。專案的內容讓她心動，久違地感受到工作真正的意義。

幾天後，她走在回家的路上，又見到那個黃色雨衣的男孩，在一間書店前靜靜站著。這次他轉身朝她笑了笑，然後指向書店裡的一本書：《人生的三條路》。

她走進去，買下那本書。書的開頭寫著：「有些選擇，看似微小，卻決定了我們的一生。」

接下來的日子裡，昀青開始留意那些「看似微小」的選擇。她開始說出自己的意見、不再勉強自己加班、不再和那個讓她總是感覺疲憊的前男友糾纏。每一個選擇，都像是在調整命運的方向。

三個月後，那個專案成功了，她也被升職。她第一次感覺自己在走一條真正屬於自己的路。某天夜晚，在回家的捷運上，她又見到了那個男孩。

「謝謝妳那天救了我。」他輕聲說。

「你…到底是誰？」她小聲問。

男孩眨眨眼，說：「我是妳命運裡的一個選擇。那天如果妳沒有停下來，妳會搭上那班車，人生會往另一條路走。現在的妳，比那時候更靠近妳真正想成為的人。」

列車抵達終點時，男孩不見了。只留下一張便利貼貼在車窗上：「繼續選擇妳相信的方向，就會走到真正的自己。」

昀青微笑，把便利貼收進錢包。從此，她不再隨波逐流，也不再恐懼改變。因為她知道——

每一次停下來的勇氣，都可能讓人生改寫。
"""  # 重複資料擴增語料

# ========== 使用 jieba 分詞 ==========
words = list(jieba.cut(text))  # 使用詞語而非字
word_set = list(set(words))    # 唯一詞表
word2idx = {w: i for i, w in enumerate(word_set)}
idx2word = {i: w for w, i in word2idx.items()}

# ========== 超參數 ==========
input_size = len(word_set)
hidden_size = 128
num_layers = 1
seq_length = 5
learning_rate = 0.005

# ========== 建立資料集 ==========
def make_dataset(words, seq_length):
    x_data, y_data = [], []
    for i in range(len(words) - seq_length):
        x_seq = words[i:i+seq_length]
        y_seq = words[i+1:i+seq_length+1]
        x_data.append([word2idx[w] for w in x_seq])
        y_data.append([word2idx[w] for w in y_seq])
    return x_data, y_data

x_data, y_data = make_dataset(words, seq_length)
x = torch.LongTensor(x_data)
y = torch.LongTensor(y_data)

# ========== 定義模型 ==========
class WordLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(WordLSTM, self).__init__()
        self.embed = nn.Embedding(input_size, hidden_size)
        self.lstm = nn.LSTM(hidden_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, input_size)

    def forward(self, x):
        x = self.embed(x)
        out, _ = self.lstm(x)
        out = self.fc(out)
        return out

# ========== 模型訓練 ==========
model = WordLSTM(input_size, hidden_size, num_layers)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

print("開始訓練...")
for epoch in range(100):
    output = model(x)
    loss = criterion(output.view(-1, input_size), y.view(-1))

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/100], Loss: {loss.item():.4f}")

# ========== 測試產生詞語 ==========
start_words = words[:seq_length]
input_test = torch.LongTensor([[word2idx[w] for w in start_words]])
result = start_words.copy()

model.eval()
with torch.no_grad():
    for _ in range(30):  # 生成 30 個詞
        output = model(input_test)
        pred = output[:, -1, :].argmax(dim=1).item()
        next_word = idx2word[pred]
        result.append(next_word)
        input_test = torch.LongTensor([[*input_test[0][1:], pred]])

print("\n🔮 生成詞語結果：")
print(''.join(result))
