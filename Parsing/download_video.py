import requests 

url='https://parsinger.ru/video_downloads/videoplayback.mp4'
response = requests.get(url=url, stream=True)
with open('file3.mp4', 'wb') as video:
    for piece in response.iter_content(chunk_size=100000):
        video.write(piece)
    

# Если файл очень большой,  или вы не хотите ждать пока файл скачает полностью , то рекомендуется использовать .iter_content() , 
# это метод, который позволяет совершать итерацию по response.content.  
# Для .iter_content() мы должны определить размер скачиваемой части файла. 
# Параметром chunk_size=1000000 где цифра, это размер в байтах.