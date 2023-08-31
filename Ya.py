import requests

class YaUploader:

    host = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        headers = {'Authorization': 'OAuth '+token}
        params = {"path": file_path, "overwrite": "true"}
        resp = requests.get(self.host, params=params, headers=headers).json()
        url = resp['href']
        with open(file_path, 'rb') as f:
            resp = requests.put(url, files= {'file': f},params=params, headers=headers)
        print(resp.status_code)
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'cat.jpeg'
    token = open("Token").read()
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
