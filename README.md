# PageRankProject
Implementing a demo search engine that works using the page rank algorithm and tf-idf algorithm

# Configuration
## Set up and enter a virtual environment
```
git clone https://github.com/theunixdisaster/PageRankProject.git
cd PageRankProject
python3 -m venv env
source env/bin/activate
```
## Installing required packages
When you are at the root directory of your repo(`PageRankProject`) there will be a `requirements.txt` file with all the requirements.
Install it simply by:
```
pip install -r requirements.txt
```

## Update the database
From the root directory of your repo execute:
```
python3 internet/manage.py makemigrations
python3 internet/manage.py migrate

python3 pgrankserver/manage.py makemigrations
python3 pgrankserver/manage.py migrate
```

# Pending work
__________________

Add a 'Did you mean' feature using Keras
