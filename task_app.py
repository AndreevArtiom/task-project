import json
import os

DEFAULT_PRIORITY = "normal"

DATA_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def add_task(title):
    tasks = load_tasks()
    new_task = {"id": len(tasks) + 1, "title": title, "status": "todo"}
    tasks.append(new_task)
    save_tasks(tasks)

def mark_done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "done"
    save_tasks(tasks)

def filter_by_status(status):
    tasks = load_tasks()
    filtered = [t for t in tasks if t["status"] == status]
    for t in filtered:
        print(f"[{t['status']}] {t['title']}")

def validate_priority(priority):
    if priority not in ["low", "normal", "high"]:
        raise ValueError("Неверный приоритет")
    return priority

def sort_tasks_by_priority():
    tasks = load_tasks()
    priority_order = {"high": 1, "normal": 2, "low": 3}
    tasks.sort(key=lambda x: priority_order.get(x.get("priority", "normal"), 2))
    for t in tasks:
        print(f"[{t.get('priority', 'normal')}] {t['title']}")

print("ОШИБОЧНЫЙ КОД")