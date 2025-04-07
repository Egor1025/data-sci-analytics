FROM python:3.9-slim
WORKDIR /app
RUN pip install --no-cache-dir requests beautifulsoup4
COPY ../server-files .
CMD ["python", "save_programs_info.py"]