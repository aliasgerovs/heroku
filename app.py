from flask import Flask
import requests
import httpx
from datetime import datetime

app = Flask(__name__)

@app.route('/notify_approved')
def notify_approved():
    result = notify_appv("Your custom message")

    return f"Function executed. Result: {result}"

def notify_appv(text) -> None:
    title = f"**Approved** "
    now = str(datetime.now())

    endpoint = ("https://apps-dex-api-prod-eus-001.azurewebsites.net/api/1.0/contents")
    apikey = "ApiKey a5cacf75-70bb-42bb-8978-e65981f97ba9"
    headers = {"Authorization": apikey,
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'en-US,en;q=0.9',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

    request_data = {"title": title,
                    "content": text,
                    "type": "anicura_error"+now,
                    "sourceSystem": "EBX",
                    "entityId": "anicura_error"+now,
                    "url": "revenue.ai",
                    "metadatas": {},
                    "userIds": ["alia.35@insightlynx.ai"],
                    }
    resp = httpx.post(endpoint, json=request_data, headers=headers, timeout=10.0)
    assert resp.status_code == 200, resp.content

    return resp.content

if __name__ == '__main__':
    app.run()
