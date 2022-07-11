from flask import Flask
import utils


app = Flask(__name__)


#Вывод на главную страницу"""
@app.route("/")
def page_index():

   message = utils.get_all()
   return f'''
   <pre>{message}</pre>'''


#Вывод на страницу кандидата по номеру
@app.route("/candidates/<int:pk>")
def page_candidate(pk):
   message = utils.get_by_pk(pk)
   return f'''
   <pre>{message}</pre>'''


#Вывод на странцицу кандидатов с навыками

@app.route("/skills/<skill>")
def page_skills(skill):
   message = utils.get_by_skill(skill)
   return f'''
   <pre>{message}</pre>'''
      
app.run()