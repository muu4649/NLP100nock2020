from transformers import BertJapaneseTokenizer
tokenizer = BertJapaneseTokenizer.from_pretrained('bert-base-japanese-whole-word-masking')
tokenizer.tokenize('お腹が痛いので遅れます。')
# ['お', '##腹', 'が', '痛', '##い', 'ので', '遅れ', 'ます', '。']
