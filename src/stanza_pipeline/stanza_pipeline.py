import stanza

class StanzaPipeline:
    def __init__(self):
        self.nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,ner')

    def process(self, input_text):
        doc = self.nlp(input_text)
        return doc
