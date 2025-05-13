# Overview

## This project implements a simplified version of GPT-4 tokenization using the following components:

- Unicode-aware regex splitting

- UTF-8 byte encoding

- Byte Pair Encoding (BPE) merge algorithm

- Token ID generation and flattening

It simulates how a real GPT tokenizer works during the vocabulary-building phase (not inference).


```txt
+------------------+
|   Input Sentence |
+------------------+
         |
         v
+----------------------+
| Unicode Regex Split  |
+----------------------+
         |
         v
+--------------------+
| UTF-8 Byte Encoding|
+--------------------+
         |
         v
+------------------+
| BPE Merge Loop   |
| - Frequency Count|
| - Pair Merging   |
+------------------+
         |
         v
+--------------------------+
| Final Token ID Sequence |
+--------------------------+
```

## 1. GPT4_SPLIT_PATTERN
A regex-based splitting pattern used by OpenAI to tokenize text using Unicode rules:
```py
GPT4_SPLIT_PATTERN = r"""'(?i:[sdmt]|ll|ve|re)|[^\r\n\p{L}\p{N}]?+\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]++[\r\n]*|\s*[\r\n]|\s+(?!\S)|\s+"""
```

## 2. get_stats(ids: List[List[int]]) -> Dict[Tuple[int, int], int]
Calculates frequency of adjacent byte pairs in the list of token byte IDs.

## 3. merge_ids(ids, pair, new_id)
Merges a specific byte-pair across all tokens and replaces them with a unique new ID starting from 256.

## 4. gpt4_style_tokenizer(sentence, num_merges=1000)
Performs the full GPT-like tokenization pipeline:

- Regex split

- UTF-8 byte encoding

- BPE merging

- Output final token IDs and merge rules

## Output
- token_ids: Final flattened list of token byte IDs (int values, some >=256 if merged)

- merge_rules: Dictionary of merged byte-pairs → new token ID

# Requirements
```
regex
collection
torch
-e .
```
# Run

```sh
    python main.py
```

## Advanced Notes
- This tokenizer is non-reversible unless you store the mapping.

- Actual GPT tokenizers (like in tiktoken) use precompiled merge tables and optimized radix trie encoding.

- UTF-8 encoding ensures multilingual compatibility (Arabic, Tamil, Chinese, etc.).

## License
MIT License — Free for use and modification.

