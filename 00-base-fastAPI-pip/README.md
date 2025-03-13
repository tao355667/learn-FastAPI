# fastAPI
基础fastAPI项目，用pip管理python环境。

## 启动命令

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## pip环境导入导出

从requirements.txt导入环境：

```bash
pip install --no-cache-dir -r requirements.txt
```


导出环境到文件requirements.txt：

```bash
pip freeze > requirements.txt
```
