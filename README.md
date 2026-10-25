# todo CLI

一个在终端里管理待办事项的小工具，支持添加、查看、完成、删除。

## 功能

- `add`：添加一条待办
- `list`：列出所有待办
- `done`：把某条标记为完成
- `delete`：删除某条待办

## 项目结构

```bash
todo_cli/
├── todo.py           # 主程序：命令行入口 + 核心功能
├── test_todo.py      # 单元测试
├── README.md         # 项目说明
├── .gitignore        # Git 忽略规则
├── data/
│   └── todos.json    # 核心数据存储，不纳入版本控制
└── test_todos.json   # 测试运行时生成，不纳入版本控制
```

## 运行方式

```bash
python todo.py add "买牛奶"      # 添加待办
python todo.py list              # 列出所有待办
python todo.py done 1            # 标记编号 1 为完成
python todo.py delete 1          # 删除编号 1
```

## 运行测试

测试覆盖：
添加（空列表 / 已有数据）、标记完成（存在 / 不存在）、删除（存在 / 不存在）。测试使用独立的 test_todos.json，不会影响 data/todos.json 中的真实数据。


## 数据存储

数据保存在 `data/todos.json`，格式为 JSON 列表，每条待办包含三个字段：

- `id`：整数编号，只增不减，删除后不重编号
- `text`：待办内容
- `done`：是否完成（`true` / `false`）

首次运行会自动创建 `data/` 目录和文件。`data/` 已加入 `.gitignore`，不纳入版本控制。

## 环境要求

Python 3.13+，仅用标准库。
