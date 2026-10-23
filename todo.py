"""
Todo CLI —— 命令行待办事项管理器
数据保存在 data/todos.json，重启程序不丢数据。
"""

# ===== 数据结构设计 =====
# 一条待办：
#   {"id": ..., "text": ..., "done": ...}
#   字段含义：id = 编号  text = 内容  done = 完成情况
#
# 整个 todos.json 顶层是：列表 / 字典（二选一，写理由）
#   选择理由：列表，然后内层用字典，列表天然有序，list 直接遍历，add 直接 append，不需要维护键
#
# id 生成策略：id 用 max+1 生成，删除中间项不重用，但删除最大 id 后新增会重用该编号。阶段 1 接受这个行为，不额外处理
# 用户看到的编号 = 真实 id（删除后可能有洞），done/delete 直接按 id 匹配
#   为什么不用 len(列表)+1：删掉中间一条后再新增，len+1 会和已有 id 撞号

# ===== 文件读写模式 =====
# 读 todos.json 用 open(..., "r")
# 写 todos.json 用 open(..., "w")
# 为什么写不能用 "a" 模式：a 只能末尾追加，每次保存会把整份 JSON 再追加一遍，文件里出现两份 JSON，下次 json.load 会报 JSONDecodeError

# ===== 预见的出错情况（读文件时）=====
# 1. todos.json不存在
# 2.文件内容是坏的（JSON 格式错误，比如手动改过），会抛 JSONDecodeError
# 3.文件顶层不是列表

"""

如果 len(sys.argv) < 2：
打印用法
退出

命令 = sys.argv[1]

如果 命令 == "add"：
如果 len(sys.argv) < 3：
    打印“请提供待办内容”
    退出
调用 add_todo(sys.argv[2])

否则如果 命令 == "list"：
调用 list_todos()

否则如果 命令 == "done"：
# 阶段 1 先不做，写“打印暂未实现”

否则如果 命令 == "delete"：
# 同上

否则：
# 未知命令怎么提示？
打印未知命令，然后贴出正确用法

"""
import sys
todos=[]
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
    else:
        print("未知命令，指令为python todo.py add ”买牛奶“ ")
        return

def add_todos(text):#添加一条待办
    if todos:
        new_id = max(t["id"] for t in todos) + 1
    else:
        new_id = 1
    todos.append({"id":new_id,"text": text, "done": False})
    print(f"已添加 [{new_id}] {text}")

def list_todos():#列出所有待办
    for t in todos:
        if t["done"]:
            mark="[x]"
        else:
            mark="[ ]"
        print(f"{mark} {t['id']}. {t['text']}")

if __name__ == "__main__":
    main()