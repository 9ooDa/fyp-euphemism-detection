> Python version: 3.7 \
This README was last modified on __April 28th, 2023__
# Euphemistic Word Detection
Original Repo: https://github.com/WanzhengZhu/Euphemism

## Overview

Detect Euphemistic words used in Dark Net Market, where people buy, sell and review drugs. There are three main steps to this project, which are Quality Mining, Euphemistic Word Candidate Selection and Euphemistic Word Ranking. The main language model used is pre-trained BERT MLM. This project is based on the paper [Euphemistic Phrase Detection by Masked Language Model](https://aclanthology.org/2021.findings-emnlp.16.pdf) and [Euphemism Word Detection with Masked Language Model](https://arxiv.org/pdf/2103.16808.pdf).


## Table of Contents

1. [Libraries Needed](#libraries-needed)
2. [Architecture Design](#architecture-design)
3. [Step By Step Guide](#step-by-step-guide)


## Libraries Needed

- Python
- Regex
- gensim
- nltk
- pytorch_pretrained_bert


## Architecture Design

- Visual Studio Code



## Step By Step Guide

### 1. Process the raw text data
Process the raw text data with the file `data_preprocessing.ipynb`. The output file will be used as the input for the next step.

Input files:
- Raw drug data file

### 2. Run AutoPhrase to get the ranked list
Run AutoPhrase to obtain the ranked list of words. Refer to the [AutoPhrase repo](https://github.com/shangjingbo1226/AutoPhrase) for the use of AutoPhrase.
If the above AutoPhrase does not work, please refer to this [simplified repo](https://github.com/Youplala/AutoPhrase).

Input files:
- Processed drug data file

### 3. Wikipedia Processing
Process the Wikipedia Dump files with `wiki_and_w2v_viz.ipynb` so that it can be used as the embedding training file. There are multiple paths and files inside the original dump file, and so this stage helps to combine the corpus into one file.

Input files:
- Any version of [Wikipedia dump](https://dumps.wikimedia.org/enwiki/)

### 4. Word2Vec process for candidate list
Run the cells provided in `word2vec.ipynb` file and obtain the candidate list, which will be used in the BERT MLM stage.

_The last section in `word2vec.ipynb` provides the resulting file for Word2Vec as the baseline method, and the result visualization can be seen in the last section in `wiki_and_w2v_viz.ipynb`._

Input files:
- Euphemism answer file
- Target keyword file
- Wiki embedding file
- Processed drug data file

### 5. Euphemistic word detection with BERT MLM
In this stage, you will be able to detect the euphemistic words with the pre-trained BERT model. 
The output will look like the picture below, and the bolded words are true positives.

![Output](https://github.com/9ooDa/fyp-euphemism-detection/blob/main/mlm_output.png)

Input files:
- vocab.txt
- BERT model config files (you can obtain this from the original repository)
- Processed drug data file
