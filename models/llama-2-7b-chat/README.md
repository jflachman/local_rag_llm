---
duplicated_from: localmodels/LLM
---
# Llama 2 7B Chat ggml

From: https://huggingface.co/meta-llama/Llama-2-7b-chat-hf

---

### Original llama.cpp quant methods: `q4_0, q4_1, q5_0, q5_1, q8_0`

Quantized using an older version of llama.cpp and compatible with llama.cpp from May 19, commit 2d5db48.

### k-quant methods: `q2_K, q3_K_S, q3_K_M, q3_K_L, q4_K_S, q4_K_M, q5_K_S, q6_K`

Quantization methods compatible with latest llama.cpp from June 6, commit 2d43387.

---

## Provided files
| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| llama-2-7b-chat.ggmlv3.q2_K.bin | q2_K | 2 | 2.87 GB| 5.37 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.vw and feed_forward.w2 tensors, GGML_TYPE_Q2_K for the other tensors. |
| llama-2-7b-chat.ggmlv3.q3_K_L.bin | q3_K_L | 3 | 3.60 GB| 6.10 GB | New k-quant method. Uses GGML_TYPE_Q5_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| llama-2-7b-chat.ggmlv3.q3_K_M.bin | q3_K_M | 3 | 3.28 GB| 5.78 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| llama-2-7b-chat.ggmlv3.q3_K_S.bin | q3_K_S | 3 | 2.95 GB| 5.45 GB | New k-quant method. Uses GGML_TYPE_Q3_K for all tensors |
| llama-2-7b-chat.ggmlv3.q4_0.bin | q4_0 | 4 | 3.79 GB| 6.29 GB | Original quant method, 4-bit. |
| llama-2-7b-chat.ggmlv3.q4_1.bin | q4_1 | 4 | 4.21 GB| 6.71 GB | Original quant method, 4-bit. Higher accuracy than q4_0 but not as high as q5_0. However has quicker inference than q5 models. |
| llama-2-7b-chat.ggmlv3.q4_K_M.bin | q4_K_M | 4 | 4.08 GB| 6.58 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q4_K |
| llama-2-7b-chat.ggmlv3.q4_K_S.bin | q4_K_S | 4 | 3.83 GB| 6.33 GB | New k-quant method. Uses GGML_TYPE_Q4_K for all tensors |
| llama-2-7b-chat.ggmlv3.q5_0.bin | q5_0 | 5 | 4.63 GB| 7.13 GB | Original quant method, 5-bit. Higher accuracy, higher resource usage and slower inference. |
| llama-2-7b-chat.ggmlv3.q5_1.bin | q5_1 | 5 | 5.06 GB| 7.56 GB | Original quant method, 5-bit. Even higher accuracy, resource usage and slower inference. |
| llama-2-7b-chat.ggmlv3.q5_K_M.bin | q5_K_M | 5 | 4.78 GB| 7.28 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q5_K |
| llama-2-7b-chat.ggmlv3.q5_K_S.bin | q5_K_S | 5 | 4.65 GB| 7.15 GB | New k-quant method. Uses GGML_TYPE_Q5_K for all tensors |
| llama-2-7b-chat.ggmlv3.q6_K.bin | q6_K | 6 | 5.53 GB| 8.03 GB | New k-quant method. Uses GGML_TYPE_Q8_K for all tensors - 6-bit quantization |
| llama-2-7b-chat.ggmlv3.q8_0.bin | q8_0 | 8 | 7.16 GB| 9.66 GB | Original quant method, 8-bit. Almost indistinguishable from float16. High resource use and slow. Not recommended for most users. |