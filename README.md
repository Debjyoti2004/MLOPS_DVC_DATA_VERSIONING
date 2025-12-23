# MLOPS_DVC_DATA_VERSIONING

This project demonstrates **data versioning using DVC (Data Version Control)** with a clean and production-style **Git + DVC workflow**.  
It shows how large datasets are versioned separately from source code and stored in a remote backend (Amazon S3).

---

## 🚀 Project Overview

- **Git** is used to version source code and DVC metadata  
- **DVC** is used to version datasets  
- **Amazon S3** acts as the remote storage for data  
- **Python virtual environment** ensures isolated and reproducible setup  

The repository intentionally does **not** store large datasets or virtual environments.  
All data is restored locally using `dvc pull`.

---

> ❌ `data/` and `venv/` are intentionally NOT pushed to GitHub  
> ✅ They are recreated locally when required
---
## 🧰 Prerequisites

- Python 3.9+
- Git
- AWS account (for S3 remote storage)
- AWS CLI configured (`aws configure`)

---

## ⚙️ Setup Instructions (Fresh Clone)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Debjyoti2004/MLOPS_DVC_DATA_VERSIONING.git
cd MLOPS_DVC_DATA_VERSIONING
```
### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
### 3️⃣ Install project dependencies
```bash
pip install -r requirements.txt
```

`requirements.txt` includes:
```txt
pandas
dvc[s3]

```
### 4️⃣ Configure AWS credentials
```
aws configure
```
This step is required for DVC to access the S3 remote.

### 5️⃣ Pull the dataset using DVC
```
dvc pull
```
### 6️⃣ Run the project

```
python main.py

```

### 🔄 Data Versioning Workflow
Track new or updated data
```
dvc add data/
git add data.dvc .gitignore
git commit -m "Update dataset version"

```

### Push data to the remote storage
Each Git commit is linked to a specific data version.
```
git checkout <commit-hash>
dvc pull --force

```
