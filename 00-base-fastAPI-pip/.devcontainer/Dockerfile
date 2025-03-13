FROM python:3.12-slim-bookworm

# 安装系统依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    procps \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /workspace

# 安装 Python 依赖（先复制 requirements 文件以利用 Docker 缓存）
COPY . /workspace

RUN pip install --no-cache-dir -r requirements.txt