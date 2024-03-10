# goit-cs-hw-03

## Task 1

Run postgres

```
docker run -d --name pgsql-dev -e POSTGRES_PASSWORD=test1234 -e POSTGRES_DB=hw06 -p 5432:5432 postgres
```

Install Venv
```
pip install -r requirements.txt
```

Create db and fill with dummy data
```
python 1.task1.py
```

SQL ex.: 2.task1.sql


## Task 2

Run Mongo locally

```
docker run --name mongodb -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=sa -e MONGO_INITDB_ROOT_PASSWORD=test1234 mongodb/mongodb-community-server:6.0-ubi8
```

Task 2 run
```
python task2.py
```