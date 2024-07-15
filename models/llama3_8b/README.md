---
language:
- en
pipeline_tag: text-generation
tags:
- facebook
- meta
- pytorch
- llama
- llama-3
license: other
license_name: llama3
license_link: LICENSE
base_model: meta-llama/Meta-Llama-3-8B-Instruct
---

# Meta-Llama-3-8B-Instruct-GGUF

- This is GGUF quantized version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) created using llama.cpp
- **Re-uploaded with new end token**

## Model Details

Meta developed and released the Meta Llama 3 family of large language models (LLMs), a collection of pretrained and instruction tuned generative text models in 8 and 70B sizes. The Llama 3 instruction tuned models are optimized for dialogue use cases and outperform many of the available open source chat models on common industry benchmarks. Further, in developing these models, we took great care to optimize helpfulness and safety. 

**Model developers** Meta

**Variations** Llama 3 comes in two sizes — 8B and 70B parameters — in pre-trained and instruction tuned variants.

**Input** Models input text only.

**Output** Models generate text and code only.

**Model Architecture** Llama 3 is an auto-regressive language model that uses an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align with human preferences for helpfulness and safety.


<table>
  <tr>
   <td>
   </td>
   <td><strong>Training Data</strong>
   </td>
   <td><strong>Params</strong>
   </td>
   <td><strong>Context length</strong>
   </td>
   <td><strong>GQA</strong>
   </td>
   <td><strong>Token count</strong>
   </td>
   <td><strong>Knowledge cutoff</strong>
   </td>
  </tr>
  <tr>
   <td rowspan="2" >Llama 3
   </td>
   <td rowspan="2" >A new mix of publicly available online data.
   </td>
   <td>8B
   </td>
   <td>8k
   </td>
   <td>Yes
   </td>
   <td rowspan="2" >15T+
   </td>
   <td>March, 2023
   </td>
  </tr>
  <tr>
   <td>70B
   </td>
   <td>8k
   </td>
   <td>Yes
   </td>
   <td>December, 2023
   </td>
  </tr>
</table>


**Llama 3 family of models**. Token counts refer to pretraining data only. Both the 8 and 70B versions use Grouped-Query Attention (GQA) for improved inference scalability.

**Model Release Date** April 18, 2024.

**Status** This is a static model trained on an offline dataset. Future versions of the tuned models will be released as we improve model safety with community feedback.

**License** A custom commercial license is available at: [https://llama.meta.com/llama3/license](https://llama.meta.com/llama3/license)

Where to send questions or comments about the model Instructions on how to provide feedback or comments on the model can be found in the model [README](https://github.com/meta-llama/llama3). For more technical information about generation parameters and recipes for how to use Llama 3 in applications, please go [here](https://github.com/meta-llama/llama-recipes). 

