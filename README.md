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

## Updating the database and creating a superuser
Go to the `migrations` directory inside `internet/sites` and delete everything except for `__init__.py`  
Now remove `db.sqlite3` if present in the `internet` folder inside the root directory using `rm -rf db.sqlite3`  
  
Similary go to the `migrations` directory inside `pgrankserver/server` and delete everything except for `__init__.py`  
Now remove `db.sqlite3` if present in the `pgrankserver` folder inside the root directory using `rm -rf db.sqlite3`  
  
Now move back to the root directory of the repo(`PageRankProject`) and run:
```
python3 internet/manage.py makemigrations
python3 internet/manage.py migrate
python3 internet/manage.py createsuper #and set a superuser

python3 pgrankserver/manage.py makemigrations
python3 pgrankserver/manage.py migrate
python3 pgrankserver/manage.py createsuperuser
```

## Starting the two servers
Open up two terminals with the virtualenv activated one in the `internet` directory and the other in `pgrankserver` directory  
In the one opened inside `internet` start the server at port `8000`
```
python3 manage.py runserver 8000
```
And in the one opened inside `pgrankserver` start the server at port `8001`
```
python3 manage.py runserver 8001
```


# Pending work
__________________

Add a 'Did you mean' feature using Keras
