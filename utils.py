# Импорт требуемых библиотек
import os
import json


def load_candidates(file_path):
    """Загружает список кандидатов из файла json"""
    with open(file_path, 'rt', encoding='utf-8') as file:
        candidates_ = json.loads(file.read())
    return candidates_


def output_sub_pages(candidates_list, direction, uid):
    """Выводит данные в виде строки либо по требуемому кандидату (для страницы "/candidate") либо по навыку("/skill")"""
    page_data = []
    for candidate in candidates_list:
        if direction == 'candidate':
            if candidate["name"] == uid:
                page_data.append(f'<img src={candidate["picture"]}>\n\n<pre>\n {candidate["name"]}'
                                 f'\n {candidate["position"]}\n {candidate["skills"]}\n</pre>')
                break
        elif direction == 'skill':
            if uid in candidate["skills"].lower():
                page_data.append(f' {candidate["name"]}\n {candidate["position"]}\n {candidate["skills"]} ')
        else:
            return 'Такой страницы не существует'
    return '\n\n'.join(page_data)


def output_main_page(candidates_list):
    """Выводит данные по всем кандидатам для начальной страницы"""
    page_data = []
    for candidate in candidates_list:
        page_data.append(f' {candidate["name"]}\n {candidate["position"]}\n {candidate["skills"]} ')
    return '\n\n'.join(page_data)
