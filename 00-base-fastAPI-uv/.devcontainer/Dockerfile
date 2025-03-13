FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.6.6 /uv /uvx /bin/

# 设置工作目录
WORKDIR /app

# 把项目文件拷贝到镜像中
COPY . /app

# 安装依赖
# RUN uv pip install --system fastapi uvicorn
# RUN uv pip install --system --no-cache-dir -r requirements.txt

# 暴露 8000 端口
EXPOSE 8000

# 启动命令
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


