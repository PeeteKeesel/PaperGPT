

I followed this guide from HuggingFace: https://huggingface.co/docs/transformers/main/model_doc/llama#llama.
- First, I requested and downloaded LLaMa's weights into `PaperGPT/data/llama/weights/raw/`
- Then I ran the following to convert and save the converted weights in Hugging Face Transformers format

```bash
python src/transformers/models/llama/convert_llama_weights_to_hf.py \
    --input_dir /path/to/downloaded/llama/weights \
    --model_size 7B \
    --output_dir /data/llama/weights/huggingface
````
