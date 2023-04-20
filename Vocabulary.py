import pickle
import MeCab
import os
import re

import neologdn


class Vocabulary:
    def __init__(self):
        self.__tagger = MeCab.Tagger("-Owakati")
        self.vocab = {}

        if os.path.isfile("vocab.pkl"):
            with open("vocab.pkl", "rb") as f:
                pickle.load(self.vocab, f)
        else:
            self.vocab = {" ": 0}

        with open("StopWord.txt", "r", encoding="utf-8") as f:
            self.__stop_word = f.readlines()
        for i in range(len(self.__stop_word)):
            self.__stop_word[i] = self.__stop_word[i].replace("\n", "")
        print(self.__stop_word)



    def sentence_wakati(self, sentence):
        text = re.sub("[\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF65\u3000-\u303F]", " ", sentence) #全角文字の置換
        text = neologdn.normalize(text) #正規化
        text = text.lower() #小文字
        tokens = self.__tagger.parse(text).strip().split(" ")   #分かち書き
        tokens = [i for i in tokens if not (i in self.__stop_word)] #ストップワードの除去
        for token in tokens:
            if not (token in self.vocab):
                self.vocab[token] = len(self.vocab)
        print(self.vocab)

    def save_vocabulary(self):
        with open("vocab", "wb") as f:
            pickle.dump(self.vocab, f)
