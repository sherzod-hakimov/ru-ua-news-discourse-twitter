# Unveiling Global Narratives: A Multilingual Twitter Dataset of News Media on the Russo-Ukrainian Conflict


## Wikidata Query to Extract News/Media Company Details

The query to extract news/media companies' Twitter handles and respective countries from Wikidata is accessible here: [https://t.ly/XEp6](https://t.ly/XEp6).

## Keywords

Keywords for all languages can be found under `resources/language_resources.jsonl`


## Twitter Handles of News/Media Companies

The full list can be found under `resources/newsmap_metadata.json`



## Dataset

The dataset can be downloaded from ANONYMIZED_LINK.

### Dataset details
The dataset includes 1,524,826 tweets for 60 languages. 306,295 tweets include images and thus the `image_tags` is be populated with the classified concepts based on [Recognize Anything Plus Model (RAM++)](https://github.com/xinyu1205/recognize-anything/), and it is an empty list in case the tweet does not include an image.

Each entry in the dataset is a single JSON line and has the following entries:

```
{
'tweet_id': 
'lang':
'stanza_output':
'stanza_named_entities':
'sentiment':
'stance':
'channel':
'country': 
'verified':
'image_tags':
}
```

If you need access to the full text of the dataset, please contact us via an email: [anonymized email](mailto:anonymized_email@email.com)


## Setup & Installation

```
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Code

Each component is implemented separately under ``src`` folder.


