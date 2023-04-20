from transformers import BertJapaneseTokenizer, BertModel
import torch

class SentenceBert:
    def __init__(self, model_name_or_path, device=None):
        self.__tokenizer = BertJapaneseTokenizer.from_pretrained(model_name_or_path)
        self.__model = BertModel.from_pretrained(model_name_or_path)
        self.__model.eval()

        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        self.__device = torch.device(device)
        self.__model.to(device)

    def __mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0]
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    @torch.no_grad()
    def encode(self, sentences, batch_size=8):
        all_embeddings = []
        iterator = range(0, len(sentences), batch_size)
        for batch_idx in iterator:
            batch = sentences[batch_idx:batch_idx + batch_size]

            encoded_input = self.__tokenizer.batch_encode_plus(batch, padding="longest",truncation=True, return_tensors="pt").to(self.__device)
            model_output = self.__model(**encoded_input)
            sentence_embeddings = self.__mean_pooling(model_output, encoded_input["attention_mask"]).to('cpu')

            all_embeddings.extend(sentence_embeddings)

        # return torch.stack(all_embeddings).numpy()
        return torch.stack(all_embeddings)

if __name__ == "__main__":
    MODEL_NAME = "sonoisa/sentence-bert-base-ja-mean-tokens-v2"
    model = SentenceBert(MODEL_NAME)

    sentences = ["暴走した人工知能"]
    sentence_embeddings = model.encode(sentences, batch_size=8)

    print("Sentence embeddings:", sentence_embeddings)  #768次元
    print(len(sentence_embeddings[0]))
