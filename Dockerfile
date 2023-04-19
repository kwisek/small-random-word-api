FROM python:3
WORKDIR /app
COPY ./requirements4pip.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src /app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]