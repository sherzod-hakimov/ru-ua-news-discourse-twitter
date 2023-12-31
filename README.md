# Unveiling Global Narratives: A Multilingual Twitter Dataset of News Media on the Russo-Ukrainian Conflict

This is the official Git repository page for the dataset paper:
> Hakimov, S., and Cheema, G.S., (2023).  Unveiling Global Narratives: A Multilingual Twitter Dataset of News Media on the Russo-Ukrainian Conflict. [Arxiv](https://arxiv.org/pdf/2306.12886.pdf)


## Dataset

The dataset can be downloaded from [Zenodo](https://doi.org/10.5281/zenodo.8043459).

The dataset includes 1,524,832 tweets for 60 languages. Each entry in the dataset is a single JSON line and has the following entries:

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
If you find the resources, please cite us:
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