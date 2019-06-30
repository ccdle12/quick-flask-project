# Flask Quick Project

## Setup

### 1. Clone the project

### 2. Install dependencies

(OPTIONAL) Setup a virtual environment for this project.

```
$ pip install -r requirements.txt
```

### 3. Create the config.py file in the instance folder.

The instance folder is used to hold configuration variables that are meant to be
kept secret and not checked in to any version control.

In this project we need to add two variables `SECRET` and `CMC_SECRET_KEY`.

- `SECRET` is used to sign jwt tokens.

- `CMC_SECRET_KEY` is the API Key for the Coin Market Cap API. A key can be generated
here: https://coinmarketcap.com/api/

Steps for creating `config.py`:

- Create the file `config.py` at `instance/config.py`.
- Add the following variables

```
CMC_SECRET_KEY = '<Coin Market API Key>'
SECRET_KEY = 'some-secret'
```

### 4. Create the DB.

Create the DB for project to run.

- Enter the python shell in the root of the project.

```
$ python
```

- Import the DB from the project

```
>>> python shell
>>> from simple_app import db
>>> db.create_all()
```

- Check that the DB was created.

```
$ cd /tmp
$ ls

test.db
```

## Run the App

### 1. Launch the app

```
$ python run.py 
```

### 2. Import `postman-collection/quick-flask-project.json` into Postman.

### 3. Use the `Create a User` endpoint. 

The user endpoint needs to have a `name` and `password` sent in the body.
This represents registration for the user.

Update the Body field with:

```
{"name": "some-user-1", "password": "some-password"}
```

### 4. Use the `Login` endpoint.

The login endpoint needs to send a Basic Auth with the request. On postman
this can be achieved by selecting the `Authorization` tab.

Select the type `Basic Auth`.

Enter the `Username` and `Password` entered when creating a user.

A token will be returned. This token will be needed for subsequent calls.

```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI0ZjAzM2MzZS04NTRmLTRhYjgtOWY5OS1iMDRhODA0MGNhZDQiLCJleHAiOjE1NjE5MDc3NDB9.EBatpp0ZL4b_4_DNMl7azR17V4nvKNme1z6pY9ytWAc"
}
```

### 5. Call `Get all Users`

This will return all the users in the system.

The token needs to be sent in the header.

Click on `Headers`.

Enter the following:

```
Key                  Value

x-access-token       eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI0ZjAzM2MzZS04NTRmLTRhYjgtOWY5OS1iMDRhODA0MGNhZDQiLCJleHAiOjE1NjE5MDc3NDB9.EBatpp0ZL4b_4_DNMl7azR17V4nvKNme1z6pY9ytWAc
```

### 6. Call `Get Quote`

This endpoint will send a request to retrieve information and price of a given
coin.

Again the token needs to be included in the header.

Add the symbol as a query string

```
http://127.0.0.1:5000/quote?symbol=btc

{
    "data": {
        "1": {
            "circulating_supply": 17789700,
            "cmc_rank": 1,
            "date_added": "2013-04-28T00:00:00.000Z",
            "id": 1,
            "last_updated": "2019-06-30T14:51:25.000Z",
            "max_supply": 21000000,
            "name": "Bitcoin",
            "num_market_pairs": 7653,
            "platform": null,
            "quote": {
                "USD": {
                    "last_updated": "2019-06-30T14:51:25.000Z",
                    "market_cap": 198552684846.34274,
                    "percent_change_1h": -2.03405,
                    "percent_change_24h": -6.78201,
                    "percent_change_7d": 3.974,
                    "price": 11161.1036075,
                    "volume_24h": 27473185682.4524
                }
            },
            "slug": "bitcoin",
            "symbol": "BTC",
            "tags": [
                "mineable"
            ],
            "total_supply": 17789700
        }
    },
    "status": {
        "credit_count": 1,
        "elapsed": 6,
        "error_code": 0,
        "error_message": null,
        "timestamp": "2019-06-30T14:51:32.458Z"
    }
}
```

## Tests

Run the tests.

```
$ pytest
```

