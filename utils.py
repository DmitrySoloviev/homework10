import json

def load_candidates():
    #list_candidates = []
    #Смотреть как из корня папки, а не диска C
    with open('candidates.json', 'r', encoding='utf-8') as file:
        list_candidates = json.load(file)
        file.close()
        return list_candidates

def