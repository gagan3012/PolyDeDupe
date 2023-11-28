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

Output:

```bash
Original dataset size: 52002
Number of duplicate clusters: 40
Files in duplicate cluster: 82
Unique files in duplicate cluster: 52
Filtered dataset size: 51972
Cluster:
Base Index: 1482, Data: {'instruction': 'Find the five largest cities in France.', 'input': '', 'output': 'The five largest cities in France are Paris, Marseille, Lyon, Toulouse, and Nice.', 'text': 'Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\nFind the five largest cities in France.\n\n### Response:\nThe five largest cities in France are Paris, Marseille, Lyon, Toulouse, and Nice.'}
Base Index: 1820, Data: {'instruction': 'Name five cities in France.', 'input': '', 'output': 'The five cities in France are Paris, Marseille, Lyon, Toulouse, and Nice.', 'text': 'Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\nName five cities in France.\n\n### Response:\nThe five cities in France are Paris, Marseille, Lyon, Toulouse, and Nice.'}
```

Citation:

```
@misc{Bhatia,
    title={PolyDeDupe: Multi-Lingual Data Deduplication},
    url={https://github.com/gagan3012/PolyDeDupe},
    journal={GitHub},
    publisher={gagan3012}, 
    author={Bhatia, Gagan}
}
```
