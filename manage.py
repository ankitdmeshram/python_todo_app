from flask import Flask, jsonify, request

app = Flask(__name__)

# sample data
todos = [
    {'id': 1, 'title': 'Todo 1', 'completed': False},
    {'id': 2, 'title': 'Todo 2', 'completed': True},
    {'id': 3, 'title': 'Todo 3', 'completed': False},
]

# endpoint to get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# endpoint to get a single todo by id
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            return jsonify(todo)
    return jsonify({'message': 'Todo not found'})

# endpoint to create a new todo
@app.route('/todos', methods=['POST'])
def create_todo():
    new_todo = {
        'id': len(todos) + 1,
        'title': request.json['title'],
        'completed': False
    }
    todos.append(new_todo)
    return jsonify(new_todo)

# endpoint to update an existing todo by id
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['title'] = request.json['title']
            todo['completed'] = request.json['completed']
            return jsonify(todo)
    return jsonify({'message': 'Todo not found'})

# endpoint to delete a todo by id
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    for index, todo in enumerate(todos):
        if todo['id'] == todo_id:
            todos.pop(index)
            return jsonify({'message': 'Todo deleted'})
    return jsonify({'message': 'Todo not found'})

if __name__ == '__main__':
    app.run(debug=True)
