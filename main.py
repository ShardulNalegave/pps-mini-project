
from typing import List
from todo import Todo
from flask import Flask, render_template, request

todos: List[Todo] = [
  Todo("Complete PPS Mini-Project", completed=True),
  Todo("Write Maths Assignment-6", completed=True),
]
app = Flask(__name__)

@app.get("/")
def index():
  return render_template("index.html", todos=todos)

@app.post("/new")
def new_todo():
  data = request.get_json()
  todo = Todo(data["title"])
  todos.append(todo)
  return "Done"

@app.post("/delete/<id>")
def delete_todo(id):
  global todos
  todos = list(filter(lambda t: t.id != id, todos))
  return "Done"

@app.post("/toggle-completed/<id>")
def toggleCompleted(id):
  global todos
  todos = list(map(lambda t: t if t.id != id else Todo(t.title, completed=not t.completed), todos))
  return "Done"

if __name__ == "__main__":
  app.run(port=8080, debug=True)