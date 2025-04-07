import requests

def download_from_github(share_url, output_path):
    share_url = share_url.replace('github.com', 'raw.githubusercontent.com').replace('blob/', '')
    r = requests.get(share_url)
    with open(output_path, 'wb') as f:
        f.write(r.content)

def download_from_yadisk(share_url, output_path):
    response = requests.get(
        'https://cloud-api.yandex.net/v1/disk/public/resources/download',
        params={'public_key': share_url}
    )

    download_url = response.json()['href']
    r = requests.get(download_url)
    with open(output_path, 'wb') as f:
        f.write(r.content)
