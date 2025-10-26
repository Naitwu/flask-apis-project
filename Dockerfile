FROM python:3.13.9-slim

WORKDIR /app

# 先複製 requirements.txt，利用快取
COPY requirements.txt .

# 正確：從 requirements 安裝所有套件
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

# 再複製原始碼
COPY . .

EXPOSE 5000

# 指定 Flask app
ENV FLASK_APP=app

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
