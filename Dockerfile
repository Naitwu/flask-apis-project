FROM python:3.13.9-slim

WORKDIR /app

# 先複製 requirements.txt，利用快取
COPY requirements.txt .

# 正確：從 requirements 安裝所有套件
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 再複製原始碼
COPY . .


CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]
