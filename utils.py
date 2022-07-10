import json

def load_candidates():

    #Смотреть как из корня папки, а не диска C
    with open('candidates.json', 'r', encoding='utf-8') as file:
        list_candidates = json.load(file)
        file.close()
        return list_candidates

def get_all():
    list_candidates = load_candidates()
    all_names = []
    for candidate in list_candidates:
        all_names.append(candidate["name"])
    return all_names

def get_by_pk(pk):
    list_candidates = load_candidates()
    for candidate in list_candidates:
        if candidate["pk"] == pk:
            return(candidate["name"])
        else:
            pass


def get_by_skill(skill_name):
    list_candidates = load_candidates()
    candidates_with_skill = []
    for candidate in list_candidates:
        list_skills = (candidate["skills"]).split(', ')
        if skill_name.lower() in list_skills or skill_name.title() in list_skills:
            candidates_with_skill.append(candidate["name"])
        else:
            pass
    return candidates_with_skill

