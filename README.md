### Instalação e Configuração

#### 1. Clone o repositório:

```bash
git clone https://github.com/lorenzouriel/excel-validation-wk-00.git
cd excel-validation-wk-00
```

#### 2. Configure a versão correta do Python com `pyenv`:

```
bash
pyenv install 3.11.5
pyenv local 3.11.5
```

#### 3. Instale as dependências do projeto:

```bash
python -m venv .venv
# O padrao é utilizar .venv
source .venv/bin/activate
# Usuários Linux e mac
.venv\Scripts\Activate
# Usuários Windows
pip install -r requirements.txt  
```

#### 4. Atualize as suas keys na API do X (Twitter):
```
access_key = ["YOUR ACCESS TOKEN"]
access_secret = ["YOUR ACCESS SECRET"]
consumer_key = ["YOUR API KEY"]
consumer_secret = ["YOUR API SECRET"]
```

#### 5. Atualize a localização do seu Bucket S3 e o nome do arquivo:
```
csv_name = ["YOU CSV FILE NAME"]
bucket_location = ["YOUR S3 BUCKET"] 
```

#### 6. Suba a EC2 no AWS e rode os seguintes comandos:
```
sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow
sudo pip install pandas
sudo pip install s3fs
sudo pip install tweepy
```


### Arquitetura
![arquitetura](/docs/architecture.png)

### Tecnologias e Bibliotecas
- Python (Código)
- Pyenv (Ambiente virtual)
- tweepy (API do Twitter)
- pandas (Manipular .csv)
- s3fs (Bucket S3 da AWS)


---
---
---

### Installation and Configuration

#### 1. Clone the repository:

```bash
git clone https://github.com/lorenzouriel/excel-validation-wk-00.git
cd excel-validation-wk-00
```

#### 2. Configure the correct Python version with `pyenv`:

```
bash
pyenv install 3.11.5
pyenv local 3.11.5
```

#### 3. Install project dependencies:

```bash
python -m venv .venv
# Default is .venv
source .venv/bin/activate
# Mac and Linux Users
.venv\Scripts\Activate
# Windows users
pip install -r requirements.txt  
```

#### 4. Update your keys from X API (Twitter):
```
access_key = ["YOUR ACCESS TOKEN"]
access_secret = ["YOUR ACCESS SECRET"]
consumer_key = ["YOUR API KEY"]
consumer_secret = ["YOUR API SECRET"]
```

#### 5. Update your S3 bucket location and csv name:
```
csv_name = ["YOU CSV FILE NAME"]
bucket_location = ["YOUR S3 BUCKET"] 
```

#### 6. Up EC2 on AWS and run the following commands:
```
sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow
sudo pip install pandas
sudo pip install s3fs
sudo pip install tweepy
```


### Arquitetura
![arquitetura](/docs/architecture.png)


### Techs e Libs
- Python (Code)
- Pyenv (Virtual Env)
- tweepy (Twitter API)
- pandas (Manipulate .csv)
- s3fs   (Bucket S3 from AWS)