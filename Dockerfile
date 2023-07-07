FROM python:3.9-slim

WORKDIR /app

COPY code.py .

EXPOSE 8000

CMD ["python", "code.py"]

