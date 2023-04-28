from collections import Counter
from tqdm import tqdm


def read_vocab_from_corpus(fn, fout):
    print("[create_vocab_from_corpus.py] Creating vocab...")

    cnt = Counter()
    with open(fn, "r") as fin:
        for line in fin:
            if line.strip() == "":
                continue
            seq = line.lower().split()
            for word in seq:
                cnt[word] += 1           

    with open(fout, "w") as fout:
        special_tokens = ['[PAD]', '[MASK]', '[CLS]', '[SEP]']

        for token in special_tokens:
            line = f'{token}\n'
            fout.write(line)

        for key in tqdm(cnt.keys()):
            line = f'{key}\n'
            fout.write(line)
    return cnt

read_vocab_from_corpus('data/output/processed_corpus.txt', 'data/output/vocab_from_corpus.txt')