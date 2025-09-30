# CNN Classifier - End-to-End Industrial Project

## 📌 Overview
This project is an **end-to-end Convolutional Neural Network (CNN) classifier** built for industrial-level deployment.  
It includes:
- Data collection & preprocessing
- Model training, evaluation, and optimization
- Deployment via **FastAPI** in a **Docker container**
- CI/CD pipeline on **AWS** for automated updates
- Monitoring & logging for production

You can adapt this template to any classification task such as:
- **Image classification** (e.g., defect detection, product categorization)
- **Medical imaging** (e.g., X-ray anomaly detection)
- **Surveillance** (e.g., emergency vehicle detection)

---
## WOrkflow
- Update config.yaml
- Update secrets.yaml [Optional]
- Update params.yaml
- Update the entity
- Update the configuration manager in src config.
- Update the components
- Update the pipeline
- Test run pipeline stage
- run tox for testing your package
- Update the dvc.yaml
- run "dvc repro" for running all the stages in pipeline

![Data Ingestion](https://github.com/Mahadevkharmate/CNN_Classifier_Template/blob/73454cff70938969a4b6a1b90de7e6c0797e7bf3/flowcharts/Data%20Ingestion.png)

### Dataset URL:
[Click here to download data](https://github.com/entbappy/Branching-tutorial/raw/master/cat-dog-data.zip)

```
## 📂 Project Structure
cnn_classifier/
│
├── data/ # Raw & processed datasets
│ ├── raw/ # Unprocessed dataset
│ ├── processed/ # Preprocessed dataset
|
├── research/ # for experiments
│ ├── trials.ipynb 
|
├── notebooks/ # Jupyter notebooks for experimentation
│ ├── 01_data_analysis.ipynb
│ ├── 02_model_training.ipynb
│ ├── 03_model_evaluation.ipynb
│
├── src/ # Source code
| ├──components
|       ├──data_ingestion.py
|       ├──base_model.py  # CNN architecture
|       ├──train.py  # Model training
|       ├──evaluation.py # Evaluation scripts
|       ├──predict.py # Prediction script
| ├──pipeline
|       ├── data_pipeline.py # Data preprocessing & augmentation
|       ├──training_pipeline.py
|       ├──prediction_pipeline.py
|
├── deployment/
│ ├── app.py # FastAPI app for inference
│ ├── Dockerfile # Docker configuration
│ ├── requirements.txt # Python dependencies
│ ├── config.py # Configurations
│
├── tests/ # Unit & integration tests
│
├── .github/workflows/ # GitHub Actions CI/CD workflows
│
├── README.md # Project documentation
├── LICENSE # License file
├── requirements.txt # Project dependencies
└── setup.py # Package setup (optional)
```

---

## 🚀 Features
- **Custom CNN architecture** with transfer learning options
- **Data augmentation** to prevent overfitting
- **Automated training pipeline**
- **Model evaluation metrics**: Accuracy, Precision, Recall, F1-score, Confusion Matrix
- **Dockerized FastAPI deployment**
- **CI/CD pipeline** with GitHub Actions → AWS EC2/ECR
- **Monitoring** using AWS CloudWatch / Prometheus + Grafana
- **Logging** of predictions to database

---

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Deep Learning:** TensorFlow / Keras or PyTorch
- **Data Processing:** NumPy, Pandas, OpenCV
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** FastAPI, Docker, AWS EC2, AWS ECR
- **CI/CD:** GitHub Actions
- **Monitoring:** AWS CloudWatch / Prometheus + Grafana

---

## 📊 Model Pipeline
1. **Data Collection**
   - Gather dataset from local or cloud sources
   - Store in `data/raw/`

2. **Data Preprocessing & Augmentation**
   - Resize, normalize, augment
   - Save to `data/processed/`

3. **Model Design**
   - Build a CNN from scratch or use transfer learning
   - Save architecture in `src/model.py`

4. **Training**
   - Train model on GPU
   - Save best model in `/models`

5. **Evaluation**
   - Test model on unseen data
   - Generate classification report

6. **Deployment**
   - Wrap model in FastAPI
   - Containerize with Docker
   - Deploy to AWS EC2 via CI/CD

7. **Monitoring**
   - Track API performance and prediction stats
   - Alert on anomalies

---

## 📦 Installation
```bash
# Clone the repository
git clone https://github.com/your-username/cnn-classifier.git
cd cnn-classifier
```
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```
```bash
# Install dependencies
pip install -r requirements.txt
```
```bash
#🏃‍♂️ Usage
1️⃣ Train Model
python src/train.py --config config.yaml
```
```bash
2️⃣ Evaluate Model
python src/evaluate.py --model models/best_model.h5
```
```bash
3️⃣ Run API Locally
uvicorn deployment.app:app --reload
```
```bash
API available at: http://127.0.0.1:8000/docs
```
``bash
4️⃣ Docker Build & Run
docker build -t cnn-classifier .
docker run -p 8000:8000 cnn-classifier
```

# 📈 Results
Metric	    Value(change as per results)
Accuracy	   98.5%
Precision	98.2%
Recall	   97.8%
F1 Score	   98.0%


 ☁️ Deployment (AWS Example)

- Push Docker image to AWS ECR

- Pull and run container on AWS EC2

- Expose API via Nginx / Load Balancer

- Monitor using AWS CloudWatch

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/catdog

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app