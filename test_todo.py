import todo
import os

todo.DATA_FILE="test_todos.json"
# 测试代码
def reset():
    """每个测试开始前，删掉测试文件，保证从空状态开始。"""
    if  os.path.exists(todo.DATA_FILE):
        os.remove(todo.DATA_FILE)

def test_add_to_empty():
    """空列表加一条，id 应该是 1。"""
    reset()
    todo.add_todo("买牛奶")
    todos=todo.load_todos()
    assert len(todos) == 1
    assert todos[0]["id"] == 1
    assert todos[0]["done"] is False
    assert todos[0]["text"] == "买牛奶"

def test_add_after_two():
    """已有 id 1、2，再加一条，新 id 应该是 3。"""
    reset()
    todo.add_todo("买牛奶")
    todo.add_todo("买牛")
    todo.add_todo("买")
    todos = todo.load_todos()
    assert len(todos) == 3
    assert todos[2]["id"] == 3

def test_done_existing():
    """标记功能"""
    reset()
    todo.add_todo("买牛奶")
    todo.mark_done("1")
    todos = todo.load_todos()
    assert todos[0]["id"] == 1
    assert todos[0]["text"] == "买牛奶"
    assert todos[0]["done"] is True

def test_done_not_existing():
    """标记不存在"""
    reset()
    todo.add_todo("第一条")
    todo.add_todo("第二条")
    before=todo.load_todos()
    todo.mark_done("99")
    after=todo.load_todos()
    assert before == after



def test_delete_existing():
    """删除一个已经存在的id"""
    reset()
    todo.add_todo("第一条")
    todo.add_todo("第二条")
    todo.add_todo("第三条")
    todo.delete_todo("2")
    todos = todo.load_todos()
    assert len(todos) == 2
    assert todos[0]["id"] == 1
    assert todos[1]["id"] == 3
    assert not any(t["id"] == 2 for t in todos)


def test_delete_not_existing():
    """删除一个不存在的id"""
    reset()
    todo.add_todo("第一条")
    todo.add_todo("第二条")
    before = todo.load_todos()
    todo.delete_todo("99")
    after = todo.load_todos()
    assert before == after

if __name__ == "__main__":
    test_add_to_empty()
    test_add_after_two()
    test_done_existing()
    test_done_not_existing()
    test_delete_existing()
    test_delete_not_existing()
    print("所有测试通过")