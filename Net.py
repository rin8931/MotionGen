import torch
import torch.nn as nn
import torch.nn.init as init
import torch.optim as optim
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self, input_size, output_size, hidden_dim, batch_first):
        """
        モデルの定義
        :param input_size: 入力データの次元
        :param output_size: 出力データの次元
        :param hidden_dim: 隠れ層の次元
        :param batch_first: batch_sizeの順番
        """
        super(Net, self).__init__()
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_dim, batch_first=batch_first)
        self.fc1 = nn.Linear(in_features=hidden_dim, out_features=output_size)


if __name__ == "__main__":
    input_size = 66 + 66  # len(rotation) + len(position)
    output_size = 66 + 66
    hidden_dim = 256

    net = Net(input_size=input_size, output_size=output_size, hidden_dim=hidden_dim, batch_first=True)
    print(net)

