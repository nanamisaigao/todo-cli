# todo CLI

一个在终端里管理待办事项的小工具，支持添加、查看、完成、删除。

## 功能

- `add`：添加一条待办
- `list`：列出所有待办
- `done`：把某条标记为完成
- `delete`：删除某条待办
- 
## 运行方式

```bash
python todo.py add "买牛奶"      # 添加待办
python todo.py list              # 列出所有待办
python todo.py done 1            # 标记编号 1 为完成
python todo.py delete 1          # 删除编号 1

## 数据存储

```markdown

数据保存在 `data/todos.json`，格式为 JSON 列表，每条待办包含三个字段：

- `id`：整数编号，只增不减，删除后不重编号
- `text`：待办内容
- `done`：是否完成（`true` / `false`）

首次运行会自动创建 `data/` 目录和文件。`data/` 已加入 `.gitignore`，不纳入版本控制。

## 环境要求

Python 3.13+，仅用标准库。

## 当前状态

已完成：`add` / `list` / `done` / `delete`，数据持久化。
待完成：异常处理、测试、代码重构。