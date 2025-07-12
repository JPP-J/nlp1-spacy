# NLP-SpaCy Project
![Last Commit](https://img.shields.io/github/last-commit/JPP-J/nlp1-spacy?style=flat-square)
![Languages](https://img.shields.io/github/languages/count/JPP-J/nlp1-spacy?style=flat-square)

This repo is home to the code that accompanies Jidapa's *NLP-SpaCy Project*:

## 📌 Overview

This project develops a **FastAPI-based NLP microservice** that supports a wide range of language processing tasks — including sentiment analysis, NER, part-of-speech tagging, dependency parsing, lemmatization, tokenization, and more. The service is built for flexibility, scalability, and production readiness, integrating DevOps tools for seamless deployment.


### 🧩 Problem Statement

Social media platforms generate massive amounts of real-time, informal, and noisy text. For businesses, researchers, and public sector agencies, analyzing this data to uncover **trends**, **public opinion**, and **emerging events** is both critical and challenging.

Key problems include:

- 🔄 **Unstructured Input**: Social posts often contain misspellings, slang, emojis, and abbreviations  
- 🧠 **Multiple NLP Needs**: From detecting **sentiment**, identifying **named entities**, tagging **parts of speech**, to extracting **grammatical structures** — there’s a need for a **unified service**  
- 🧪 **Scalability**: Traditional tools are hard to scale for real-time or batch processing of thousands of posts  
- ⚙️ **Integration Challenge**: Organizations need a deployable, modular API that plugs easily into analytics pipelines or UIs  
- 🚀 **Deployment Overhead**: Maintaining and deploying NLP tools with different dependencies can be complex without containerization

This project addresses these challenges by offering a cloud-deployable, containerized NLP microservice that wraps multiple NLP tasks into a single, fast API.



### 🔍 Approach

- Built with **FastAPI** for efficient REST API performance  
- Powered by **spaCy**, **TextBlob**, and **spacytextblob** for robust NLP capabilities  
- Uses **Docker** for portability and **GitHub Actions** for CI/CD automation  
- Deployed using **AWS ECS + Fargate**, allowing scalable, production-grade serving  
- Supports multi-task NLP (`SENTIMENT`, `NER`, `POS`, `DEP`, `LEMMA`, etc.) with clean endpoint structure



### 🎢 Processes

1. **Text Analysis Modes** – Supports 8+ NLP modes, triggered via `POST /process`  
2. **Smart Input Handling** – Supports comparative input for sentiment/similarity scoring  
3. **Clean JSON Outputs** – Easy-to-consume format for integration in pipelines or dashboards  
4. **CI/CD Automation** – Validated, containerized, and auto-deployed on push to main branch  
5. **Cloud-Native Setup** – Docker → ECR → ECS + Load Balancer with GitHub Actions



### 🎯 Results & Impact

- ✅ **Sentiment Analysis** on posts from Twitter, Facebook, Threads helps brands gauge public mood in real-time  
- ✅ **NER (Named Entity Recognition)** identifies trending topics, mentions of people, companies, places — useful for monitoring PR or crisis  
- ✅ **POS (Part-of-Speech Tagging)** helps uncover writing patterns, intent (e.g., questions, actions, commands), or build chatbots tuned to common phrasing  
- ✅ **Dependency Parsing & Lemmatization** supports deeper semantic analysis, such as subject-object relationships or intent classification  
- ✅ Enables **automated and consistent analysis** of thousands of social media posts, reducing human labor and boosting turnaround  
- ✅ Easy to integrate into news, marketing, or customer insight pipelines — making it valuable for **trend detection**, **customer service automation**, and **brand monitoring**


### 🔧 Example Use Cases

- **Marketing**: Analyze tweet sentiment + NER to track campaign mentions and spot brand advocates or critics  
- **Media**: Segment live-streamed comment feeds into topic categories via POS/NER  
- **Customer Support**: Use dependency parsing to flag complaint language or requests in inbound social messages  
- **News Monitoring**: Detect breaking events and involved entities early through clustered NER hits



### ⚙️ Key Challenges

- **Text Noise**: Handling non-standard spelling, emoji, hashtags, and code-switching in social media  
- **Combining Tasks**: Efficiently serving different NLP modes under one interface  
- **Scalability & Speed**: Serving thousands of requests in near real-time  
- **Deployment Reliability**: Ensuring updates don’t break critical tasks using automated CI/CD  
- **Extensibility**: Designing the system to allow future NLP task integrations (e.g., topic modeling, toxicity detection)




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

> **Example demo**:  [demo](example_demo.ipynb)
---
