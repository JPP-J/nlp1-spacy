from pydantic import BaseModel
from enum import Enum

class ModeEnum(str, Enum):
    sentiment = "SENTIMENT"
    ner = "NER"
    token = "token"
    pos = "POS"
    dep = "DEP"
    lemma = "LEMMA"
    morph = "MORPH"
    sent = "SENT"
    sim = "SIM"


class TextInput(BaseModel):
    text1: str
    text2: str
    mode: ModeEnum   # e.g. 'SENTIMENT', 'NER', etc.
