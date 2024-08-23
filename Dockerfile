FROM python:3.10-slim

ADD hackernews.py .

RUN pip install requests beautifulsoup4

CMD ["python3", "./hackernews.py"]