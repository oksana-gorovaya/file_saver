FROM python:3
ADD app.py /
RUN pip install httpserver
CMD ["python", "./app.py"]