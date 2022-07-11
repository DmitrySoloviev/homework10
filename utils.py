import json

def load_candidates():
    """Загружает список кандидатов из файла"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        list_candidates = json.load(file)
        file.close()
        return list_candidates

def get_all():
    """Выводит список всех кандидатов"""
    list_candidates = load_candidates()
    message = ""
    for candidate in list_candidates:
        message = message + candidate['name'] + "\n"
        message = message + candidate['position'] + "\n"
        message = message + candidate['skills'] + "\n" + "\n"
    return message



def get_by_pk(pk):
    """Возвращает кандидатов по номеру"""
    list_candidates = load_candidates()
    message = ""
    for candidate in list_candidates:
        if candidate["pk"] == pk:
            picture_link = candidate['picture']
            message = message + candidate['name'] + "\n"
            message = message + candidate['position'] + "\n"
            message = message + candidate['skills'] + "\n" + "\n"
        else:
            pass
    return f"<img src='({picture_link})'>\n{message}"

def get_by_skill(skill_name):
    """Возвращает кандидатов по навыкам"""
    list_candidates = load_candidates()
    message = ""
    for candidate in list_candidates:
        list_skills = (candidate["skills"]).split(', ')
        if skill_name.lower() in list_skills or skill_name.title() in list_skills:
            message = message + candidate['name'] + "\n"
            message = message + candidate['position'] + "\n"
            message = message + candidate['skills'] + "\n" + "\n"
        else:
            pass
    return message

