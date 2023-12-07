import concurrent.futures
import requests

def download_url(url):
    response = requests.get(url)
    filename = url.split("/")[-1]

    with open(filename, "wb") as file:
        file.write(response.content)

if __name__ == "__main__":
    url_list = [
        "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-624ru.exe",
        "https://www.win-rar.com/fileadmin/winrar-versions/winrar-x64-624gl.exe",
        "https://www.win-rar.com/fileadmin/winrar-versions/winrar-x64-624vn.exe",
    ]

    # максимальное количество потоков
    max_threads = 5

    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        executor.map(download_url, url_list)