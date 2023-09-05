FROM python
RUN pip install pika
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY receive.py .
CMD ["python", "/usr/src/app/receive.py"]
