import os
import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def generate_file_content():
    hello_world_count = random.randint(7, 30)
    content = generate_random_string(2500000)
    for _ in range(hello_world_count):
        index = random.randint(0, len(content) - len("HelloWorld"))
        content = content[:index] + "HelloWorld" + content[index + len("HelloWorld"):]
    return content

def create_files():
    if not os.path.exists("randomFiles"):
        os.makedirs("randomFiles")

    for i in range(1, 151):
        filename = f"randomFiles/file_{i}.txt"
        with open(filename, 'w') as file:
            file.write(generate_file_content())

if __name__ == "__main__":
    create_files()
    print("Files created successfully.")
