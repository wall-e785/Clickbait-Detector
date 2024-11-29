from datasets import load_dataset

# let's load the imdb dataset from huggingface
# source: (https://huggingface.co/datasets/imdb)
raw_dataset = load_dataset('imdb')
raw_dataset
from datasets import load_dataset
ds = load_dataset("christinacdl/clickbait_detection_dataset")