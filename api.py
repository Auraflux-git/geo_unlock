from fastapi import FastAPI, HTTPException
from curl_cffi import requests

app = FastAPI()

@app.get("/fetch")
def fetch(url: str):
    try:
        resp = requests.get(
            url,
            impersonate="chrome116",  # Chrome TLS fingerprint
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/116.0.5845.96 Safari/537.36"
                ),
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
            },
            timeout=30,
            http2=True,
        )
        return {
            "status": resp.status_code,
            "headers": dict(resp.headers),
            "body": resp.text,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
