import os
import random
import requests
from bs4 import BeautifulSoup
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

def get_random_image_url(search_term):
    # Construct the Google Images search URL
    base_url = "https://www.google.com/search?q="
    url = base_url + f"{search_term}&tbm=isch"

    print(url)
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the image URLs from the search results
    image_urls = []
    for img_tag in soup.findAll('img', attrs={'src': True, 'class': 'Q4LuWd'}):
        image_url = img_tag['src']
        if image_url.endswith(('.jpg', '.jpeg', '.png')):
            image_urls.append(image_url)

    return image_urls

def download_image(image_url, output_folder):
    image_response = requests.get(image_url)
    with open(os.path.join(output_folder, os.path.basename(image_url)), 'wb') as f:
        f.write(image_response.content)

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size)
        img.save(output_path)

def process_images_parallel(input_folder, output_folder, search_term, num_processes, target_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_urls = get_random_image_url(search_term)

    if not image_urls:
        print("No images found.")
        return

    selected_urls = random.sample(image_urls, min(num_processes, len(image_urls)))

    with ThreadPoolExecutor() as executor:
        for image_url in selected_urls:
            input_path = os.path.join(output_folder, os.path.basename(image_url))
            executor.submit(download_image, image_url, input_path)

    # Ресайз изображений
    input_paths = [os.path.join(output_folder, filename) for filename in os.listdir(output_folder) if filename.lower().endswith(('.jpg', '.jpeg', '.png'))]

    with ThreadPoolExecutor() as executor:
        for input_path in input_paths:
            output_path = os.path.join(output_folder, f"resized_{os.path.basename(input_path)}")
            executor.submit(resize_image, input_path, output_path, target_size)

if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images"
    search_term = "cat"
    num_processes = 2
    target_size = (300, 300)

    process_images_parallel(input_folder, output_folder, search_term, num_processes, target_size)
