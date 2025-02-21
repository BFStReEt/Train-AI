import re

file_path = r'c:\Train-AI\data\input.txt'  

def read_chat_file(file_path):
    """ Đọc file chat và tách các cuộc hội thoại """
    try:
        print(f"Attempting to open file: {file_path}")  # Debug print statement
        with open(file_path, "r", encoding="utf-8") as file:
            chat_data = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []

    conversations = []
    current_convo = []

    for line in chat_data:
        if "======" in line:  
            if current_convo:
                conversations.append(current_convo)
                current_convo = []
        else:
            current_convo.append(line.strip())

    if current_convo:
        conversations.append(current_convo)

    return conversations

chats = read_chat_file(file_path)
print(f"📌 Đã tách {len(chats)} cuộc hội thoại!")
