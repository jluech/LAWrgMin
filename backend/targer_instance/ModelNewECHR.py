import sys
sys.path.insert(0, "./lstm")

import nltk
from lstm.src.factories.factory_tagger import TaggerFactory


path = "./models/ECHR_model_100epoch_pe.hdf5"


class ModelNewECHR:

    tagger = TaggerFactory.load(path, -1)

    def __init__(self):
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')

    def label(self, input_text):
        sentences = [nltk.word_tokenize(input_text)]

        output = self.tagger.predict_tags_from_words(sentences, batch_size=200)

        result = []
        for sentenceIdx in range(len(sentences)):
            tokens = sentences[sentenceIdx]
            sentence = []
            for tokenIdx in range(len(tokens)):
                current_word = {
                    'token': tokens[tokenIdx],
                    'label': output[sentenceIdx][tokenIdx]
                }
                sentence.append(current_word)
            result.append(sentence)

        return result
