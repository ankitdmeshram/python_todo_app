from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# connect to MySQL database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python_todo'
)

# endpoint to get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM todos")
    todos = mycursor.fetchall()
    return jsonify(todos)

# endpoint to get a single todo by id
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM todos WHERE id = %s", (todo_id,))
    todo = mycursor.fetchone()
    if todo:
        return jsonify(todo)
    return jsonify({'message': 'Todo not found'})

# endpoint to create a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    title = request.json['title']
    isCompleted = 0
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO todos (title, completed) VALUES (%s, %s)", (title, isCompleted))
    mydb.commit()
    todo_id = mycursor.lastrowid
    todo = {'id': todo_id, 'title': title, 'completed': False}
    return jsonify(todo)

# endpoint to update an existing todo by id
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    title = request.json['title']
    completed = request.json['completed']
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE todos SET title = %s, completed = %s WHERE id = %s", (title, completed, todo_id))
    mydb.commit()
    if mycursor.rowcount:
        todo = {'id': todo_id, 'title': title, 'completed': completed}
        return jsonify(todo)
    return jsonify({'message': 'Todo not found'})

# endpoint to delete a todo by id
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM todos WHERE id = %s", (todo_id,))
    mydb.commit()
    if mycursor.rowcount:
        return jsonify({'message': 'Todo deleted'})
    return jsonify({'message': 'Todo not found'})

if __name__ == '__main__':
    app.run(debug=True)
