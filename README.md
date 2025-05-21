# NLP-SpaCy Project

This repo is home to the code that accompanies Jidapa's *NLP-SpaCy Project* :

- **Description**:  
  Developed a FastAPI-based NLP microservice for multiple text analysis modes (e.g., sentiment analysis, NER, POS tagging) using `spaCy` and `TextBlob`. The API accepts JSON text input and returns structured NLP analysis results. Integrated CI/CD using GitHub Actions and containerized the service with Docker for scalable deployment.

- **Modes Supported**:
  - `SENTIMENT`: Sentiment polarity & subjectivity (via `spacytextblob`)
  - `NER`: Named Entity Recognition  
  - `POS`: Part-of-speech tagging  
  - `DEP`: Dependency parsing  
  - `LEMMA`: Lemmatization  
  - `TOKEN`: Tokenization  
  - `SENT`: Sentence segmentation  
  - `SIM`: Text similarity  

- **Libraries Used**:
  - **NLP**: `spaCy`, `TextBlob`, `spacytextblob`
  - **API Framework**: `FastAPI`, `pydantic`
  - **DevOps**: `Docker`, `GitHub Actions`, `pytest`


- **Features**:
  - `GET /`: Root endpoint that returns a welcome message
  - `POST /process`: Accepts `text1`, `text2`, and `mode` in JSON format to perform selected NLP task with dynamic mode selection for analysis type
  - `POST /modes`: Returns the list of supported NLP modes
  - `POST /pipelines`: Returns the current pipeline components in the loaded spaCy model
  - Supports both individual and comparative text analysis
  - Clean modular project structure (routers, utils, models)
  - JSON responses with extracted NLP insights


- **CI/CD Integration**:
  - Automated testing pipeline using `pytest`
  - GitHub Actions workflow for testing and Docker image build
  - Dockerized app with `Dockerfile` and `docker-compose.yml` for reproducible deployment

- **Example demo**:  
  [demo](https://github.com/JPP-J/nlp1-spacy/blob/448ef6ccb229174748875beeef2191be77417dff/example_demo.ipynb)
