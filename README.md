# sql-alchemy-review


## To install 

1. create a virtual environment 
```
python3 -m venv venv 

```

2. activate the virtual environment 
```
source venv/bin/activate
```

3. install requirements 
```
pip install -r requirements.txt
``` 

4a. run code. (app.py for flask_alchemy)
```
python app.py

``` 

4b. run code (sqlalchemy)

NOTE: First run setup_db() by modifying main as seen below 
```
if __name__ == '__main__':
	setup_db()

```
Then to run code 
```
python sql-alchemy-review.py
```

to test of queries 
```
if __name__ == '__main__':
	query_db()
```



