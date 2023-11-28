# PolyDeDupe: Multi-Lingual Data Deduplication

PolyDeDupe is a Python package designed for efficient and effective data deduplication across multiple languages. With support for over 100 languages, this tool stands out in its ability to perform both syntactic and semantic deduplication, ensuring high-quality data preprocessing for various NLP tasks.

## Installation

PolyDeDupe can be installed using pip:

```bash
pip install polydedupe
```

## Usage

```python
from PolyDeDupe import deduplicate_dataset, display_dataset_entries
from datasets import load_dataset

dataset = load_dataset("tatsu-lab/alpaca",split="train")
newdataset = dataset.map(build_dataset, num_proc=16, remove_columns=dataset.column_names)
ds_dedup, duplicate_clusters = deduplicate_dataset(newdataset, jaccard_threshold=0.90)
display_dataset_entries(newdataset, duplicate_clusters)
```
