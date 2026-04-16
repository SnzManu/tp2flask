FROM python:3.9
ADD . /app
WORKDIR /app
RUN pip install -r app/requirements.txt
EXPOSE 5000
CMD python app/app.py
