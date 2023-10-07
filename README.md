

<div align="center">

#  Paper Explainer


<a>
    <img alt="Python" src="https://img.shields.io/badge/python-3.11.4-green">
</a>
<a>
    <img alt="numpy" src="https://img.shields.io/badge/numpy-1.26.0-blue">
</a>
<a>
    <img alt="huggingface_hub" src="https://img.shields.io/badge/huggingface_hub-0.15.1-blue">
</a>
<a>
    <img alt="openai" src="https://img.shields.io/badge/openai-0.28.1-blue">
</a>

</div>


> Simply specify of the paper your want to understand and obtain a short summary (TL;DR) of it in seconds. 

## Installation

```bash
# -----------------------------------------------------------------------------
# Setting up the environment

# Create the PaperGPT environment
conda env create -f environment.yml

# (Optiona) Run the following to check if PaperGPT got successfully created
conda env list

# Activate the environment
conda activate PaperGPT


# -----------------------------------------------------------------------------
conda install -c huggingface transformers

pip install PyPDF2
conda install -c conda-forge pypdf2

pip install openai
conda install -c conda-forge openai -y


```


## Action Points

- [ ] Ease of use: ensure that library is easy to install. Clear documentation and examples.
- [ ] Automatic processing: automatically extract text and relevant content from papers, eliminate need for users to manually input or format the content
- [ ] Compatibility: should be able to handle various document formats (`PDF`, `PNG`, `JPG`), and possibly even accept URLs to academic papers hosted online
- [ ] Multi-language support 
- [ ] Use cases: Provide real-world use cases and scenarios where the library can be valuable, such as research paper review, studying, or staying updated on the latest research.
- [ ] Model Options: Provide option for the user to decide between different LLM models such as `LLaMa`, `GPT`, `Bert`
  - `BART` (Facebook AI) -- 
  - `BERT` (Google AI) -- `bert-base-uncased`
  - `GPT-2` (OpenAI)
