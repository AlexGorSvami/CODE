import requests





for i in range(1,161):
    response = requests.get(url=f'http://parsinger.ru/img_download/img/ready/{i}.png', stream=True)
    with open(f'img/img{i}.png', 'wb') as file:
        for j in response.iter_content(chunk_size=1000):
            file.write(j)

