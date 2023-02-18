from flask import Flask
from utils import*

# Прописываем пути к файлам для чтения в переменных
file_path = os.path.join('data', 'candidates.json')

app = Flask(__name__)


# Создаем роут для начальной страницы
@app.route('/')
def main_page():
    start = output_main_page(load_candidates(file_path))
    return f'<pre>\n{start}\n</pre>'


# Создаем роут с параметрами для страниц: "/skill" и "/candidate"
@app.route('/<direction>/<uid>')
def candidates_skills(direction, uid):
    common = output_sub_pages(load_candidates(file_path), direction, uid)
    return f'<pre>{common}</pre>'


app.run()
