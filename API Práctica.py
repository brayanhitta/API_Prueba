from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos de ejemplo (simulación de una base de datos)
tasks = [
    {"id": 1, "title": "Comprar víveres", "done": False},
    {"id": 2, "title": "Lavar el auto", "done": True}
]

# Endpoint para obtener todas las tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Endpoint para agregar una nueva tarea
@app.route('/tasks', methods=['POST'])
def add_task():
    new_task = {'id': len(tasks) + 1, 'title': request.json['title'], 'done': False}
    tasks.append(new_task)
    return jsonify({'message': 'Tarea agregada', 'task': new_task}), 201

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
