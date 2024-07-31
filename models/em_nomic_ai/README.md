---
base_model: nomic-ai/nomic-embed-text-v1.5
inference: false
language:
  - en
license: apache-2.0
model_creator: Nomic
model_name: nomic-embed-text-v1.5
model_type: bert
pipeline_tag: sentence-similarity
quantized_by: Nomic
tags:
  - feature-extraction
  - sentence-similarity
---

***
**Note**: For compatiblity with current llama.cpp, please download the files published on 2/15/2024. The files originally published here will fail to load.
***

<br/>

# nomic-embed-text-v1.5 - GGUF

Original model: [nomic-embed-text-v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5)


## Description

This repo contains llama.cpp-compatible files for [nomic-embed-text-v1.5](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5) in GGUF format.

llama.cpp will default to 2048 tokens of context with these files. To use the full 8192 tokens that Nomic Embed is benchmarked on, you will have to choose a context extension method. The original model uses Dynamic NTK-Aware RoPE scaling, but that is not currently available in llama.cpp. A combination of YaRN and linear scaling is an acceptable substitute.

These files were converted and quantized with llama.cpp [PR 5500](https://github.com/ggerganov/llama.cpp/pull/5500), commit [34aa045de](https://github.com/ggerganov/llama.cpp/pull/5500/commits/34aa045de44271ff7ad42858c75739303b8dc6eb).

## Example `llama.cpp` Command

Compute a single embedding:
```shell
./embedding -ngl 99 -m nomic-embed-text-v1.5.f16.gguf -c 8192 -b 8192 --rope-scaling yarn --rope-freq-scale .75 -p 'search_query: What is TSNE?'
```

You can also submit a batch of texts to embed, as long as the total number of tokens does not exceed the context length. Only the first three embeddings are shown by the `embedding` example.

texts.txt:
```
search_query: What is TSNE?
search_query: Who is Laurens Van der Maaten?
```

Compute multiple embeddings:
```shell
./embedding -ngl 99 -m nomic-embed-text-v1.5.f16.gguf -c 8192 -b 8192 --rope-scaling yarn --rope-freq-scale .75 -f texts.txt
```


## Compatibility

These files are compatible with llama.cpp as of commit [4524290e8](https://github.com/ggerganov/llama.cpp/commit/4524290e87b8e107cc2b56e1251751546f4b9051) from 2/15/2024.


## Provided Files

The below table shows the mean squared error of the embeddings produced by these quantizations of Nomic Embed relative to the Sentence Transformers implementation.

Name | Quant | Size | MSE 
-----|-------|------|-----
[nomic-embed-text-v1.5.Q2\_K.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.Q2_K.gguf) | Q2\_K | 48 MiB | 2.33e-03
[nomic-embed-text-v1.5.Q3\_K\_S.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.Q3_K_S.gguf) | Q3\_K\_S | 57 MiB | 1.19e-03
[nomic-embed-text-v1.5.Q3\_K\_M.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.Q3_K_M.gguf) | Q3\_K\_M | 65 MiB | 8.26e-04
[nomic-embed-text-v1.5.Q3\_K\_L.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.Q3_K_L.gguf) | Q3\_K\_L | 69 MiB | 7.93e-04
[nomic-embed-text-v1.5.Q4\_0.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.Q4_0.gguf) | Q4\_0 | 75 MiB | 6.32e-04
[nomic-embed-text-v1.5.Q4\_K\_S.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.Q4_K_S.gguf) | Q4\_K\_S | 75 MiB | 6.71e-04
[nomic-embed-text-v1.5.Q4\_K\_M.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.Q4_K_M.gguf) | Q4\_K\_M | 81 MiB | 2.42e-04
[nomic-embed-text-v1.5.Q5\_0.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.Q5_0.gguf) | Q5\_0 | 91 MiB | 2.35e-04
[nomic-embed-text-v1.5.Q5\_K\_S.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.Q5_K_S.gguf) | Q5\_K\_S | 91 MiB | 2.00e-04
[nomic-embed-text-v1.5.Q5\_K\_M.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.Q5_K_M.gguf) | Q5\_K\_M | 95 MiB | 6.55e-05
[nomic-embed-text-v1.5.Q6\_K.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.Q6_K.gguf) | Q6\_K | 108 MiB | 5.58e-05
[nomic-embed-text-v1.5.Q8\_0.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.Q8_0.gguf) | Q8\_0 | 140 MiB | 5.79e-06
[nomic-embed-text-v1.5.f16.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.f16.gguf) | F16 | 262 MiB | 4.21e-10
[nomic-embed-text-v1.5.f32.gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-GGUF/blob/main/nomic-embed-text-v1.5.f32.gguf) | F32 | 262 MiB | 6.08e-11
