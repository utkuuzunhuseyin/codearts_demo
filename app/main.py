from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory task store (demo purposes)
tasks = [
    {"id": 1, "title": "Setup CodeArts Project", "done": True},
    {"id": 2, "title": "Configure CI/CD Pipeline", "done": False},
    {"id": 3, "title": "Deploy to Production", "done": False},
]

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "service": "CodeArts Demo - Task Manager API",
        "version": "1.0.0",
        "status": "running"
    })

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks, "total": len(tasks)})

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json()
    task["done"] = data.get("done", task["done"])
    task["title"] = data.get("title", task["title"])
    return jsonify(task)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
