from PIL import Image
import urllib.request

def download_and_rotate(item):

    urllib.request.urlretrieve(item[1], "sample.jpg")
    image = Image.open("sample.jpg")
    rotated_image = image.rotate(90, expand=True)
    rotated_image.save(f"rotated_image_{item[0]}.jpg")
    print(f"Image rotated and saved as rotated_image_{item[0]}.jpg")

def serial_runner(image_urls):

    for i,url in enumerate(image_urls, start=1):
        print(i,url)
        download_and_rotate((i,url))

def pool_runner(image_urls, workers=4):

    items = []

    for i,url in enumerate(image_urls, start=1):
        items.append((i,url))



image_urls = [
    "https://picsum.photos/id/10/300/200",
    "https://picsum.photos/id/20/300/200",
    "https://picsum.photos/id/30/300/200",
    "https://picsum.photos/id/40/300/200",
    "https://picsum.photos/id/50/300/200",
    "https://picsum.photos/id/60/300/200",
    "https://picsum.photos/id/70/300/200",
    "https://picsum.photos/id/80/300/200",
    "https://picsum.photos/id/90/300/200",
    "https://picsum.photos/id/100/300/200",
]

# url = "https://picsum.photos/300/200"
# urllib.request.urlretrieve(url, "sample.jpg")
# image = Image.open("sample.jpg")
# rotated_image = image.rotate(90, expand=True)
# rotated_image.save("rotated_sample.jpg")
# print("Image rotated and saved as rotated_sample.jpg")

# Serial Processing of downloading images one by one - rotating - saving

if __name__ == "__main__":

    # serial_runner(image_urls)
                  
    pool_runner(image_urls)

