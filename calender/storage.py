def save_data(text):
    with open("notes.txt", "a") as file:
        file.write(text + "\n")

def read_data():
    try:
        with open("notes.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "No events saved yet."