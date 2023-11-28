# **PolyDeDupe**

```{toctree}
:maxdepth: 2
:hidden:
:caption: Getting started

installation
overview
```

```{toctree}
:hidden:
:caption: Development

CHANGELOG
CONTRIBUTING
License <https://raw.githubusercontent.com/allenai/PolyDeDupe/main/LICENSE>
GitHub Repository <https://github.com/gagan3012/PolyDeDupe>
```

# PolyDeDupe: Multi-Lingual Data Deduplication

PolyDeDupe is a Python package designed for efficient and effective data deduplication across multiple languages. With support for over 100 languages, this tool stands out in its ability to perform both syntactic and semantic deduplication, ensuring high-quality data preprocessing for various NLP tasks.

## Features

- **Multi-Lingual Support**: PolyDeDupe supports over 100 languages, including English, French, German, Spanish, Portuguese, Italian, Dutch, Czech, Polish, Slovak, Hungarian, Croatian, Slovenian, Latvian, Lithuanian, Russian, Bulgarian, Serbian, Ukrainian, Belarusian, Macedonian, Greek, Arabic, Persian (Farsi), Urdu, Pashto, Kurdish (Sorani), Hindi, Marathi, Sanskrit, Nepali, Konkani, Bodo, Amharic, Tigrinya, and many more.

- **Syntactic and Semantic Deduplication**: PolyDeDupe performs both syntactic and semantic deduplication, ensuring high-quality data preprocessing for various NLP tasks.

- **Customizable Jaccard Threshold**: PolyDeDupe allows users to customize the Jaccard similarity threshold for deduplication.

- **2x faster than other tools**: PolyDeDupe is 2x faster than other tools, such as [SlimPajama](https://github.com/Cerebras/modelzoo/tree/main/modelzoo/transformers/data_processing/slimpajama)

- **Support for Instruction tuning data**: PolyDeDupe supports deduplication of instruction tuning data, which is a common use case in NLP.

## Citation

```
@software{Gagan_PolyDeDupe_2023,
    author = {Gagan, Bhatia},
    doi = {10.5281/zenodo.1234},
    month = nov,
    title = {{PolyDeDupe}},
    url = {https://github.com/gagan3012/PolyDeDupe},
    version = {1.0.0},
    year = {2023}
}
```
