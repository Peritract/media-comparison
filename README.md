## Installation

1. `pip install -r requirements.txt`
2. `python setup_nltk.py`

## Environment

Add a `.env` file with the following variables:

```
FEED_URL_A=XXXXX
FEED_URL_B=XXXXX
```

Each value should be a valid RSS URL.

## Development

- Run `python extract.py` to store the initial data
- Run the `text_processing.ipynb` notebook to process the dataset

## Possible tasks

- Look at word frequency
- Look at sentiment (most positive/most negative)
- Use the headlines as input to an ML model
- Topics/areas of concern