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

# Endpoint para eliminar una tarea por su ID   
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task_to_delete = next((task for task in tasks if task['id'] == task_id), None)
    
    if task_to_delete:
        tasks.remove(task_to_delete)
        return jsonify({'message': 'Tarea eliminada', 'task': task_to_delete}), 200
    else:
        return jsonify({'message': 'Tarea no encontrada'}), 404
# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
