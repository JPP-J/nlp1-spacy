# NLP-SpaCy Project

This repo is home to the code that accompanies Jidapa's *NLP-SpaCy Project*:


## Description
Developed a FastAPI-based NLP microservice for multiple text analysis modes (e.g., sentiment analysis, NER, POS tagging) using `spaCy` and `TextBlob`. The API accepts JSON text input and returns structured NLP analysis results. Integrated CI/CD using GitHub Actions and containerized the service with Docker for scalable deployment.


## Modes Supported
- `SENTIMENT`: Sentiment polarity & subjectivity (via `spacytextblob`)  
- `NER`: Named Entity Recognition  
- `POS`: Part-of-speech tagging  
- `DEP`: Dependency parsing  
- `LEMMA`: Lemmatization  
- `TOKEN`: Tokenization  
- `SENT`: Sentence segmentation  
- `SIM`: Text similarity  


## Libraries Used
- **NLP**: `spaCy`, `TextBlob`, `spacytextblob`  
- **API Framework**: `FastAPI`, `pydantic`  
- **DevOps**: `Docker`, `GitHub Actions`, `pytest`  


## Features
- `GET /`: Root endpoint returning a welcome message  
- `POST /process`: Accepts `text1`, `text2`, and `mode` JSON payload to perform selected NLP task  
- `POST /modes`: Returns the list of supported NLP modes  
- `POST /pipelines`: Returns current spaCy pipeline components  
- Supports both individual and comparative text analysis  
- Modular project structure (routers, utils, models)  
- JSON responses with extracted NLP insights  


## Deployment on AWS ECS + Fargate with GitHub Actions CI/CD

This project supports containerized deployment using AWS ECS Fargate with an Application Load Balancer for scalable and reliable serving.

### How to deploy:

1. **Dockerize** the FastAPI app (Dockerfile included)  
2. **Push Docker image** to AWS Elastic Container Registry (ECR)  
3. **Deploy** the image on ECS Fargate service behind an ALB  
4. **Automate** deployment via GitHub Actions

**Example demo**:  [demo](https://github.com/JPP-J/nlp1-spacy/blob/448ef6ccb229174748875beeef2191be77417dff/example_demo.ipynb)