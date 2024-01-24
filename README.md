# Unveiling Global Narratives: A Multilingual Twitter Dataset of News Media on the Russo-Ukrainian Conflict

This is the official Git repository page for the dataset paper:
> Hakimov, S., and Cheema, G.S., (2023).  Unveiling Global Narratives: A Multilingual Twitter Dataset of News Media on the Russo-Ukrainian Conflict. [Arxiv](https://arxiv.org/pdf/2306.12886.pdf)


## Dataset

The dataset can be downloaded from [Zenodo](https://zenodo.org/records/10563101).

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

If you need access to the full text of the dataset, please contact us via an email: [sherzodhakimov (at sign) gmail.com](mailto:sherzodhakimov@gmail.com)


## Setup & Installation

```
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Code

Each component is implement separately under ``src`` folder.


## Citation
If you find the resources useful, please cite us:
```
@misc{hakimov2023unveiling,
      title={Unveiling Global Narratives: A Multilingual Twitter Dataset of News Media on the Russo-Ukrainian Conflict}, 
      author={Sherzod Hakimov and Gullal S. Cheema},
      year={2023},
      eprint={2306.12886},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```