# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Specify a cache directory where the model will be saved
cache_dir = "./flan_t5_large"

# Download the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large", cache_dir=cache_dir)
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large", cache_dir=cache_dir)

print("Model and tokenizer downloaded to:", cache_dir)