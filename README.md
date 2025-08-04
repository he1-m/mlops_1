Here’s a **beautiful, professional, and recruiter-friendly README.md** tailored to showcase your MLOps project workflow with all the tools, features, and services you’ve incorporated:

---

# 🚗 Vehicle Insurance Premium Prediction - MLOps Project

![MLOps Banner](https://img.shields.io/badge/MLOps-EndToEnd-blue)

> An end-to-end Machine Learning Operations (MLOps) pipeline to predict vehicle insurance premium costs, equipped with CI/CD, Docker, MongoDB, AWS S3 integration, and a deployed Flask Web App.

---

## 🧠 Project Highlights

✅ Modular Project Template
✅ MongoDB for scalable data storage
✅ Logging, Exception Handling, and Robust Configuration
✅ Component-based Pipeline (Ingestion → Validation → Transformation → Training → Evaluation)
✅ AWS S3 Integration for Model Versioning
✅ CI/CD Deployment using Docker + GitHub Actions + EC2 Runner
✅ FastAPI/Flask Web UI hosted on EC2

---

## 🔧 Setup Instructions

### 1️⃣ Initialize Project

```bash
python template.py
```

### 2️⃣ Set Up Local Packaging

Write `setup.py` and `pyproject.toml` to package your modules.
📘 *Learn more in* `crashcourse.txt`

### 3️⃣ Create & Activate Virtual Environment

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
pip list  # Confirm installed packages
```

---

## ☁️ MongoDB Atlas Setup

1. Create a MongoDB Atlas account & project
2. Deploy a **M0 cluster**
3. Set up DB user credentials
4. Add IP Access: `0.0.0.0/0`
5. Get Python connection string
6. Create `notebook/mongoDB_demo.ipynb` and push dataset
7. Verify upload via MongoDB Atlas → Browse Collections

---

## 📚 Logging, Exception & EDA

* ✍️ Implemented logger and exception handling (`logger.py`, `exception.py`)
* 📊 Added EDA + Feature Engineering Notebook in `/notebook`

---

## 📥 Data Ingestion Module

✔ Structured ingestion pipeline with the following:

* `constants/__init__.py`: Configuration values
* `configuration/mongo_db_connection.py`: MongoDB client logic
* `data_access/proj1_data.py`: Fetch & convert MongoDB records
* `entity/config_entity.py`: Ingestion config class
* `entity/artifact_entity.py`: Ingestion artifact class
* `components/data_ingestion.py`: Core ingestion logic
* `pipeline/training_pipeline.py`: Run ingestion
* `demo.py`: Test and run the complete flow

🌐 **Set MongoDB URI:**

```bash
# Bash
export MONGODB_URL="your-url"
# PowerShell
$env:MONGODB_URL = "your-url"
```

---

## 📏 Data Validation, Transformation & Model Trainer

* `utils/main_utils.py`: Helper logic
* `config/schema.yaml`: Dataset schema
* `components/data_validation.py`: Check nulls, schema, duplicates
* `components/data_transformation.py`: Encoding, Imputation
* `components/model_trainer.py`: Model training & hyperparameter tuning
* `entity/estimator.py`: Holds preprocessing pipeline & model

---

## ☁️ AWS Integration (S3, IAM)

1. Create IAM user & download credentials
2. Add env vars:

```bash
export AWS_ACCESS_KEY_ID="your_key"
export AWS_SECRET_ACCESS_KEY="your_secret"
```

3. Create S3 Bucket: `my-model-mlopsproj` (us-east-1)
4. Update:

   * `configuration/aws_connection.py`
   * `constants/__init__.py`
   * `aws_storage/` & `entity/s3_estimator.py` for push/pull logic

---

## 📊 Model Evaluation & Pusher

* `components/model_evaluation.py`: Checks model drift via threshold
* `components/model_pusher.py`: Pushes model to S3 bucket if improved

---

## 🌐 Web Application & Prediction Pipeline

* Built with Flask
* `/`: Form interface
* `/predict`: Returns prediction
* `/train`: Trigger model training

📁 Folder structure:

```
|-- static/
|-- templates/
|-- app.py
```

---

## 🚀 CI/CD Pipeline Setup

### 🐳 Docker + GitHub Actions + EC2

* Setup:

  * `Dockerfile`, `.dockerignore`
  * `.github/workflows/aws.yaml`

* EC2:

  * Ubuntu 24.04 (T2 Medium), open port `5080`
  * Installed Docker, connected GitHub Self-hosted runner

* GitHub Secrets:

  ```
  AWS_ACCESS_KEY_ID
  AWS_SECRET_ACCESS_KEY
  AWS_DEFAULT_REGION
  ECR_REPO
  ```

### ✅ End-to-End Automation

Trigger pipeline with every push to GitHub. EC2 runner builds image → pushes to ECR → deploys container → App auto-hosted at:

```
http://<EC2-IP>:5080
```

---

## 📦 Tech Stack

| Category             | Tools / Services                      |
| -------------------- | ------------------------------------- |
| Language             | Python 3.10                           |
| ML Libraries         | Scikit-learn, Pandas, NumPy, XGBoost  |
| Database             | MongoDB Atlas                         |
| Model Registry       | AWS S3                                |
| CI/CD & Deployment   | GitHub Actions, Docker, AWS EC2 & ECR |
| Web Framework        | Flask                                 |
| Monitoring & Logging | Custom Logger, Exception Tracker      |

---

## 📁 Folder Structure

```
vehicle-mlops/
│
├── src/
│   ├── components/
│   ├── configuration/
│   ├── data_access/
│   ├── entity/
│   ├── aws_storage/
│   ├── pipeline/
│   ├── constants/
│   └── utils/
│
├── notebook/
├── static/
├── templates/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── setup.py
├── pyproject.toml
└── .github/workflows/aws.yaml
```

---

## 👨‍💻 Author

**Hemant Joshi**
*MLOps * Python Enthusiast*
 [GitHub](https://github.com/he1-m) 

---

Let me know if you want a downloadable `.md` file or a styled PDF version as well.
