import torch
import torch.nn as nn
from Net import Net
from BvhLoader import BvhLoader
from Vocabulary import Vocabulary
import matplotlib.pyplot as plt

def main():
    input_size = 66 + 66 + 768  #len(rotation) + len(position)
    output_size = 66 + 66
    hidden_dim = 256
    num_layers = 1

    net = Net(input_size=input_size, output_size=output_size, hidden_dim=hidden_dim, batch_first=True)
    print(net)
    criterion = nn.CrossEntropyLoss(ignore_index=0)
    optimizer = torch.optim.Adam(net.parameters(), lr=0.03)
    epochs = 200

    bvh = BvhLoader()
    bvh.load("C:/Users/apple/PycharmProjects/MotionGen/MotionData/data/dataset-1_bow_active_001.bvh")


    return

def train(model, dataloader, criterion, optimizer, epochs, vocab_size):
    pass



if __name__ == '__main__':
    main()