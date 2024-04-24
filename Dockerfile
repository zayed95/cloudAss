FROM python:3.9-slim

WORKDIR /app

COPY main.py paragraphs.txt /app/

RUN pip install nltk

RUN python -m nltk.downloader stopwords

CMD ["python", "main.py"]
