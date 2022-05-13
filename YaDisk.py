import requests
from pprint import pprint


class YaUploader:
    HOST = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    
    # Просто проверка подключения
    def get_ya(self):
        url = f'{self.HOST}/v1/disk'
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        pprint(response.json()['user'])


    # Загрузка файла на диск
    def upload(self, file_path: str):
        url = f'{self.HOST}/v1/disk/resources/upload/'
        headers = self.get_headers()  

        # Берём название файла для правильного названия да ЯаДиске
        split_path = file_path.split('\\')
        file_name = split_path[-1] 

        # Получаем ссылку для загрузки                       
        params = {'path': file_name, 'overwrite': True}
        response = requests.get(url, params=params, headers=headers)
        response_url_up = response.json().get('href')

        # Загрузка
        upload_link = response_url_up
        response_up = requests.put(upload_link, data = open(file_path, 'rb'), headers=headers)
        if response_up.status_code == 201:
            print('Ваш файл загрузился')



if __name__ == '__main__':

    path_to_file = input('Введите путь до файла: ')
    token = 'AQAAAABXa545AADLW42L837CWUyMrErw3WGo9tU'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    # uploader.get_ya()