from fastapi import APIRouter, Query
from app.models import TextInput
from utils.nlp_utils import CustomSpacy

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the NLP API!"}

@router.post("/modes")
async def get_modes():
    spacy_model = CustomSpacy(text1=None,  mode="NER", model="en_core_web_sm")
    modes = spacy_model.check_mode()
    return {"available_modes": modes}

@router.post("/pipelines")
async def get_pipelines():
    spacy_model = CustomSpacy(text1=None,  mode="NER", model="en_core_web_sm")
    pipelines = spacy_model.check_pipline()
    return {"available_pipelines": pipelines}

@router.post("/process")
async def analyze(data: TextInput):
    spacy_model = CustomSpacy(text1=data.text1, text2=data.text2, mode=data.mode, model="en_core_web_sm")
    result = spacy_model.nlp_task()

    if data.mode.upper() == "SENTIMENT":
        classification = spacy_model.classify_sentiment()
        return {"mode": data.mode, "result": classification}

    return {"mode": data.mode, "result": result}



# @router.post("/analyze")
# async def analyze(data: TextInput):
#     spacy_model = CustomSpacy(text1=data.text,  mode='SENTIMENT', model="en_core_web_sm")
#     result = spacy_model.nlp_task()
  
#     classification = spacy_model.classify_sentiment()
 
#     return {"result": classification}


# @router.get("/analyze")
# async def analyze(text: str = Query(..., min_length=1)):
#     spacy_model = CustomSpacy(text1=text,  mode='SENTIMENT', model="en_core_web_sm")

#     result = spacy_model.nlp_task()
#     classification = spacy_model.classify_sentiment()
 
#     return {"raw_text":text, "result": classification}
