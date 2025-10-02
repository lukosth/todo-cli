import json
import os

FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks, category=None, search_result=False):
    # 分类过滤
    if category:
        tasks = [task for task in tasks if task.get('category', 'General') == category]

    if not tasks:
        if category:
            print(f"✅ No tasks in category '{category}'!")
        else:
            print("✅ No tasks! You're all caught up.")
        return

    if search_result:
        print("Search Results:")
    else:
        print("All Tasks:")

    print("ID | Title | Status | Category")
    print("-" * 50)
    for i, task in enumerate(tasks):
        status = '✔️' if task['done'] else '❌'
        category_info = task.get('category', 'General')
        print(f"{i+1}. {task['title']} [{status}] - Category: {category_info}")

def add_task(tasks, title, category="General"):
    tasks.append({"title": title, "done": False, "category": category})

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]

def search_tasks(tasks, keyword, category=None):
    # 按关键词过滤
    results = [task for task in tasks if keyword.lower() in task['title'].lower()]
    # 按分类过滤
    if category:
        results = [task for task in results if task.get('category', 'General') == category]

    if not results:
        print(f"✅ No tasks matching '{keyword}'" + (f" in category '{category}'!" if category else "!"))
        return

    show_tasks(results, category, search_result=True)

def main():
    tasks = load_tasks()

    while True:
        print("\n1. View\n2. Add\n3. Complete\n4. Delete\n5. Search\n6. Exit")
        choice = input("Choose: ")

        if choice == '1':
            category_filter = input("Filter by category (leave empty for all): ")
            show_tasks(tasks, category_filter if category_filter else None)
        elif choice == '2':
            title = input("Task: ")
            category = input("Category (leave empty for General): ") or "General"
            add_task(tasks, title, category)
        elif choice == '3':
            idx = int(input("Task number to complete: ")) - 1
            complete_task(tasks, idx)
        elif choice == '4':
            idx = int(input("Task number to delete: ")) - 1
            delete_task(tasks, idx)
        elif choice == '5':
            keyword = input("Search keyword: ")
            category = input("Filter by category (leave empty for all): ")
            search_tasks(tasks, keyword, category if category else None)
        elif choice == '6':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
