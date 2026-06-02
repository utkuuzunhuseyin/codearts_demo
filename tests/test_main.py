import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    """Test root endpoint returns service info."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "running"
    assert "version" in data


def test_health_check(client):
    """Test health endpoint returns healthy."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_get_all_tasks(client):
    """Test fetching all tasks."""
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.get_json()
    assert "tasks" in data
    assert "total" in data
    assert data["total"] >= 0


def test_get_single_task(client):
    """Test fetching a single task by ID."""
    response = client.get("/tasks/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1
    assert "title" in data
    assert "done" in data


def test_task_not_found(client):
    """Test 404 for non-existent task."""
    response = client.get("/tasks/9999")
    assert response.status_code == 404
    assert "error" in response.get_json()


def test_create_task(client):
    """Test creating a new task."""
    payload = {"title": "New Demo Task"}
    response = client.post(
        "/tasks",
        json=payload,
        content_type="application/json"
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "New Demo Task"
    assert data["done"] is False


def test_create_task_missing_title(client):
    """Test validation: title is required."""
    response = client.post(
        "/tasks",
        json={},
        content_type="application/json"
    )
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_update_task(client):
    """Test updating a task's done status."""
    response = client.put(
        "/tasks/2",
        json={"done": True},
        content_type="application/json"
    )
    assert response.status_code == 200
    assert response.get_json()["done"] is True
