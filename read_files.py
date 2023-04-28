import time
import re
from collections import defaultdict

from tqdm import tqdm

def read_raw_text(corpus_fn, drug_formal):
    start = time.time()
    all_text = []
    num_lines = sum(1 for line in open(corpus_fn, 'r'))
    with open(corpus_fn, 'r') as fin:
        for line in tqdm(fin, total=num_lines):
            temp = line.split()
            if any(ele in temp for ele in drug_formal) and len(line) <= 150:
                all_text.append(line.strip())
    print('[read_data.py] Finish reading data using %.2fs' % (time.time() - start))
    return all_text

def read_files(euph_answer_fn, target_fn, auto_fn):
    print('[read_data.py] Reading data with read_files...')
    euph_answer = defaultdict(list)
    with open(euph_answer_fn) as f:
        lines = f.readlines()
        pattern = '[;\\n]+'
        for l in lines:
            l = l.lower()
            val = l.split(':')[0]
            keys = l.split(':')[1]
            keys = re.split(pattern, keys)
            for k in keys:
                if len(k) == 0:
                    pass
                else:
                    euph_answer[k.strip()].append(val) # key = casual, val = formal

    # drug_euphemism = sorted(list(set([x[0] for x in euph_answer.items()])))
    drug_formal = sorted(list(set([y for x in euph_answer.items() for y in x[1]])))

    target_dict = {}
    count = 0
    with open(target_fn) as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip().split('\t')
            for i in l:
                target_dict[i.strip()] = count
            count += 1

    auto_euph = []
    with open(auto_fn) as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip().split('\t')
            for i in range(len(l)):
                if i%2 != 0:
                    auto_euph.append(l[i])
                else:
                    pass

    return euph_answer, drug_formal, target_dict, auto_euph

def read_all_data(datapath, euph_answer_fn, target_fn, auto_fn):
    print('[read_data.py] Reading data with read_all_data...')

    euph_answer, drug_formal, target_dict, auto_euph = read_files(euph_answer_fn, target_fn, auto_fn)
    all_text = read_raw_text(datapath, drug_formal)

    return all_text, euph_answer, drug_formal, target_dict, auto_euph