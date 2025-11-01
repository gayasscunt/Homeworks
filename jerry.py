import sqlite3  # Для работы с базой данных
import requests  # Для веб-парсинга
from bs4 import BeautifulSoup  # Для обработки HTML
from flask import Flask, request, render_template  # Для создания веб-интерфейса

# Создаем объект базы данных
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sites (url TEXT, content TEXT)''')
        self.conn.commit()

    def add_site(self, url, content):
        self.cursor.execute('INSERT INTO sites (url, content) VALUES (?, ?)', (url, content))
        self.conn.commit()

    def search_sites(self, query):
        self.cursor.execute('SELECT url, COUNT(*) as count FROM sites WHERE content LIKE ? GROUP BY url', ('%' + query + '%',))
        result = self.cursor.fetchall()
        result.sort(key=lambda x: x[1], reverse=True)
        return result

    def clear_database(self):
        self.cursor.execute('DELETE FROM sites')
        self.conn.commit()

# Создаем объект для парсинга сайтов
class WebParser:
    def parse_site(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                return soup.get_text()  # Извлекаем весь текст с HTML страницы
        except Exception as e:
            print("Ошибка при парсинге сайта:", str(e))
        return ""

# Создаем объект пользовательского интерфейса с использованием Flask
app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')  # Рендерим HTML-шаблон главной страницы

# Страница добавления сайта
@app.route('/add_site', methods=['POST'])
def add_site():
    url = request.form['url']
    content = web_parser.parse_site(url)
    if content:
        database.add_site(url, content)  # Добавляем сайт в БД
    return render_template('index.html', message="Сайт добавлен успешно!")

# Страница поиска
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    result = database.search_sites(query)  # Ищем сайты по запросу
    return render_template('search_results.html', results=result)  # Рендерим результаты поиска

# Страница очистки базы данных
@app.route('/clear')
def clear():
    database.clear_database()  # Очищаем базу данных
    return render_template('index.html', message="База данных очищена!")

if __name__ == '__main__':
    # Инициализация базы данных и парсера
    database = Database('sites.db')
    web_parser = WebParser()

    # Запуск веб-приложения Flask
    app.run(debug=True)
