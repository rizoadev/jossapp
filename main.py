import uvicorn
from fastapi import FastAPI
from rizapubsub import PubSub

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "solat sik cuk"}


@app.get("/update")
async def update():

    c = {
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "client_email": "eviqafriliya-gmailcom@pingbot999.iam.gserviceaccount.com",
        "client_id": "115709660384480806190",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/eviqafriliya-gmailcom%40pingbot999.iam.gserviceaccount.com",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDJWJM4WFQ2rcL/\n3nKTEfFKsji2p1rsesQqtkcWKHE4CibYwAUCcadRFX78wOPnPVsZ+VjxVyuO1m5X\nt6UVxgop14Diy/nfiJdOfv+qU7N6UZ+BHr0LhHFxsdEcw08mO/Fc5haTtUi8xGgV\n8Rd4YWaZTG544EXRdYOeI6cAkzIIdtBZJgspKIkcjMYhrynqUeNcLx/tJEb+89B5\nHQY/IuM/XVDLJ1gbvE0P+0+ayfJ+wyKNjjSaiSC4JkZbLhYZqV6PFptvCv1qJFkf\nfL/H7dbbXRJKSZJOSdoV9Djequx3j9TktoRCMiKgkgqs6mppX7b5oBB/wYY9Dysy\nDfvCYNwDAgMBAAECggEAAaZLujdiPpQsAGtSztnsP36vo7sw4PqUPnXflNLCZnBW\nUfCOqwQw9c4J0HALEBfwMavAG/9pGWoWdzYLsryAw79CyEORJ5UmgLuZ5n81lzoG\n5wzYwP0izABVFZeklOXgjygFB5mSn+ttn2n/c1yihrBVwG+Br7rVArBnSbumujic\nTZkmKIscP3sJCdQbaGxz+/fDFDbHD5mlxoMiwr0MmLG0Z7FrL0Vs1qEUKSVeeOjS\nQ8Hp1VCltwXV1ImiXqPETEGTcnWHMG8mw2Q3G+Q688lTawDGDF02+MJyzxYpPHe7\nScqfd7OyP61FgbCoYy7Cy2ObdycLQ69Yi3paNQ3icQKBgQD9EiZTmExW7IVVJaBD\nZg5bAbSWAsu+I+EGC9mByv+HJGijEA05nd83OnDnLenA4caSk2g0hpzAzppUiiZu\nOon1BXed+9jQthmqKDYW0d+nyrp694d7G6vHsWj+VoFsnT/ymdApEoQkX5NBzBEz\nC+CIcEgrHZLBnW1K9Hi5CDTH5QKBgQDLrSoLTueEChniPMykZ3gJ1l9Gu3+43MUW\nQReuqT8z/L4/Fjg29JPc6YqaecAlNhWO3++WiV0qu8yibeyF/BwKfPePArgYcTGG\nyNkEEiajQ72bTG/WUk8t3h0TRqqmE7M8BxyuX3BKEzLbbXPY6VBXRwm9zEs9YOos\nc2GZuIoFxwKBgQD2gaBdmyL5JKh3mQ/ztsxS72VVHeISEubUueQjXnXq0JcwBqmr\nLtFH/aAOP5XK8OE402cUiu7TjCueH3dxtYm95pZuh+vY2RhEu6h8L/CYg4uDzerl\nCr4X5QKtg9vLzZyFljfCWivnNkW9OKakP3R10lEp1kOmXs8fzORu78Rh1QKBgD+Q\nYk+3J0+w61UMznz8gZzoV0G24GxsEeIZHG/5B+2Mkj8UCyUzfTXzeLsvBgVW9LFr\nN9WONxJQG9QRZECIZqPrTkNGgPe309IRupCnrYFEcdcWqsyDUYyqBf7vDfDYsxYn\nzg6pYFzt0vBiH0Zxwg4K8IJYUJ7uMQcAV1RnIEQfAoGBAIKuApPU18YTVEpn9ujL\njkvZJzo2SRAMHDzOku+xo+Cvx4bcO5Q44nxNFOnp0iYpIHjOFvUddyD5WMcAeVCW\npg6sKyOd+CIBtfDqdU+4rYOXBHL2L/NDFIdfaEIvm7i51x9vaRgn9l4B5/n6BZUa\n+9gPvVjhMQsLnf+Q6r+6GXAo\n-----END PRIVATE KEY-----\n",
        "private_key_id": "9acb9e39eb7547c8dc76aafb1728145d4be7dca1",
        "project_id": "pingbot999",
        "token_uri": "https://oauth2.googleapis.com/token",
        "type": "service_account"
    }

    # begin
    p = PubSub(c)
    publisher = p.pub()
    s = {
        'topic': 'workers-dev',
        'namespace': 'auth',
        'subname': 'auth_register',
        'delay': 1,
        'data': {
            'fullname': 'mas joko',
            'email': 'panas@gmail.com'
        }
    }
    pid = p.send(publisher, s)
    print('send pubsub:', pid)

    return "Hello World!" + pid


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
