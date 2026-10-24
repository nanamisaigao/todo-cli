
import sys
import os
import json

def main():
    """程序入口：解析命令行参数，分发到 add / list / done / delete。"""
    if len(sys.argv) < 2:
        print("请提供待办内容，指令为python todo.py add ”买牛奶“")
        return
    elif sys.argv[1] == "add" :
        if len(sys.argv) < 3:
            print("请提供待办内容")
            return
        else:
            add_todos(sys.argv[2])
    elif sys.argv[1] == "list" :
        list_todos()
    elif sys.argv[1] == "done" :
        if len(sys.argv) < 3:
            print("请提供待办编号")
            return
        mark_done(sys.argv[2])
    elif sys.argv[1] == "delete" :
        if len(sys.argv) < 3:
            print("请提供待办编号")
            return
        delete_todo(sys.argv[2])
    else:
        print("未知命令，指令为python todo.py add ”买牛奶“ ")
        return

def add_todos(text):#添加一条待办
    todos=load_todos()
    if todos:
        new_id = max(t["id"] for t in todos) + 1
    else:
        new_id = 1
    todos.append({"id":new_id,"text": text, "done": False})
    save_todos(todos)
    print(f"已添加 [{new_id}] {text}")

def list_todos():#列出所有待办
    todos = load_todos()
    for t in todos:
        if t["done"]:
            mark="[x]"
        else:
            mark="[ ]"
        print(f"{mark} {t['id']}. {t['text']}")

def load_todos():
    """读取 data/todos.json，返回待办列表；文件不存在时返回空列表。"""
    if not os.path.exists("data/todos.json"):
        return []
    try:
        with open("data/todos.json", "r",encoding="utf-8") as f:
            data=json.load(f)
    except json.JSONDecodeError:
        print("文件损坏")
        return []
    if not isinstance(data, list):
        print("文件顶层不是列表")
        return []
    return data

def save_todos(todos):
    """把待办列表写回 data/todos.json，目录不存在则创建。"""
    os.makedirs("data", exist_ok=True)  # 创建文件目录
    with open("data/todos.json", "w",encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def mark_done(todo_id):
    """把指定 id 的待办标记为完成。"""
    if not todo_id.isdigit():
        print(f"编号必须是数字，你输入的是：{todo_id}")
        return
    todos = load_todos()
    todos_id= int(todo_id)
    if todos_id not in [t["id"]for t in todos]:
        print("没有此代办")
        return
    for t in todos:
        if t["id"] == todos_id:
            t["done"] = True

    save_todos(todos)
    print("成功标记")

def delete_todo(todo_id):
    """删除指定 id 的待办。"""
    if not todo_id.isdigit():
        print(f"编号必须是数字，你输入的是：{todo_id}")
        return
    todos = load_todos()
    todos_id = int(todo_id)
    new_todos=[]
    for t in todos:
        if t["id"] != todos_id:
            new_todos.append(t)
    if len(new_todos) != len(todos):
        print(f"已删除id为{todo_id}的待办")
        save_todos(new_todos)
        return
    print(f"未找到id {todo_id}")


if __name__ == "__main__":

    main()