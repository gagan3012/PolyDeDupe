# Usage

```python
from PolyDeDupe import deduplicate_dataset, display_dataset_entries
from datasets import load_dataset

dataset = load_dataset("tatsu-lab/alpaca",split="train")
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

## Supported Langauges

- **Western European Languages**:
  - French, German, Spanish, Portuguese, Italian, Dutch, etc.

- **Central European and Baltic Languages**:
  - Czech, Polish, Slovak, Hungarian, Croatian, Slovenian, Latvian, Lithuanian, etc.

- **Additional European Languages**:
  - Additional European languages with special characters.

- **Vietnamese and Some African Languages**:
  - Vietnamese and various African languages using extended Latin characters.

- **Slavic Languages Using Cyrillic Script**:
  - Russian, Bulgarian, Serbian, Ukrainian, Belarusian, Macedonian, etc.

- **Greek Language**:
  - Modern Greek.

- **Arabic Language and its Variants**:
  - Standard Arabic, Persian (Farsi), Urdu, Pashto, Kurdish (Sorani), etc.

- **Languages Using the Devanagari Script**:
  - Hindi, Marathi, Sanskrit, Nepali, Konkani, Bodo, etc.

- **Ethiopic Script Languages**:
  - Amharic, Tigrinya, and other languages in Ethiopia and Eritrea.

- **Tifinagh Script for Berber Languages**:
  - Berber languages in North Africa.

- **Vai Script**:
  - Used for the Vai language in West Africa.

- **East Asian Languages**:
  - Chinese, Japanese, Korean.

- **Dravidian Languages**:
  - Tamil, Telugu, Kannada, Malayalam.

- **Indian Languages**:
  - Bengali, Punjabi, Gujarati, Oriya.

- **General Latin, Numerals, and Underscore**:
  - Basic Latin characters, numbers, and underscore used globally.

