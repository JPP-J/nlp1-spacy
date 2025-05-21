import spacy
from spacy.tokens import Doc
from textblob import TextBlob
from spacytextblob.spacytextblob import SpacyTextBlob  

class CustomSpacy():
    def __init__(self,text1, text2:str=None, mode:str = None, model="en_core_web_sm"):
        self.model = model
        self.nlp = spacy.load(self.model)
        self.text1 = text1
        self.text2 = text2
        self.mode = mode
        self.doc = None
        self.result = None

        # For sentiment analysis
        self.sentiment = None
        self.subject = None

        self.list_modes = ['NER', 'token', 'POS', 'DEP', 'LEMMA', 'MORPH', 'SENT', 'SIM', 'SENTIMENT']

        if "spacytextblob" not in self.nlp.pipe_names:
            self.nlp.add_pipe("spacytextblob")

        # # Example of adding other pipes
        # nlp.add_pipe("ner")          # Named Entity Recognition
        # nlp.add_pipe("tagger")       # Part-of-speech tagging
        # nlp.add_pipe("parser")       # Dependency parsing
        # nlp.add_pipe("lemmatizer")   # Lemmatization
        # nlp.add_pipe("sentencizer")         # Rule-based sentence segmentation (fast, punctuation-based)
        # nlp.add_pipe("merge_entities")      # Merge multi-token named entities into single tokens
        # nlp.add_pipe("merge_noun_chunks")   # Merge noun phrases (like "the quick fox") into single tokens
        # nlp.add_pipe("merge_subtokens")     # Merge subword tokens (used with transformers) into full words



    def check_pipline(self):
        return self.nlp.pipe_names
    
    def check_mode(self):
        if self.mode not in self.list_modes:
            raise ValueError(f"Invalid mode. Choose from {self.list_modes}")
        else:
            return self.list_modes
    
    @staticmethod
    def get_polarity(doc):
        return TextBlob(doc.text).sentiment.polarity

    @staticmethod
    def get_subjectivity(doc):
        return TextBlob(doc.text).sentiment.subjectivity
    
    def set_pol_sub(self):
        Doc.set_extension("polarity", getter=self.get_polarity, force=True)
        Doc.set_extension("subjectivity", getter=self.get_subjectivity, force=True)

    def nlp_task(self):
        # Check if text1 and text2 are provided
        if self.text2 == None:
            doc1 = self.nlp(self.text1)
        else:
            doc1 = self.nlp(self.text1)
            doc2 = self.nlp(self.text2)


        if self.mode == 'NER':
            self.result = [(ent.text, ent.label_) for ent in doc1.ents]
        elif self.mode == 'token':
            self.result = [token.text for token in doc1]
        elif self.mode == 'POS':
            self.result = [(token.text, token.pos_) for token in doc1] # fucntion of word ; looking, VERB
        elif self.mode == 'DEP':
            self.result = [(token.text, token.dep_, token.head.text) for token in doc1]
        elif self.mode == 'LEMMA':
            self.result = [(token.text, token.lemma_) for token in doc1] # original vocab ; gone, go
        elif self.mode == 'MORPH':
            self.result = [(token.text, token.morph) for token in doc1]
        elif self.mode == 'SENT':
            self.result = [sent for sent in doc1.is_sentenced]
        elif self.mode == 'SIM':
            similarity = doc1.similarity(doc2)
            self.esult = similarity
        elif self.mode == 'SENTIMENT':
            self.set_pol_sub()
            self.result = {
                "polarity": doc1._.polarity,
                "subjectivity": doc1._.subjectivity
            }
        else:
            raise ValueError(f"Invalid mode. Choose from {self.list_modes}")

        return self.result

    def classify_sentiment(self):
        if self.mode != 'SENTIMENT':
            raise ValueError("Sentiment classification is only available in SENTIMENT mode.")
        else:
            # Polarity classification
            # -1.0 (most negative) ➜ 0.0 (neutral) ➜ +1.0 (most positive)
            if self.result['polarity'] > 0:
                self.sentiment = "positive"
            elif self.result['polarity'] < 0:
                self.sentiment = "negative"
            else:
                self.sentiment = "neutral"

            # Subjectivity classification
            if self.result['subjectivity'] > 0.5:
                self.subject = "subjective"
            else:
                self.subject = "objective"
        
        classification = {
            "sentiment": self.sentiment,
            "subjectivity": self.subject
        }

        return classification

    
