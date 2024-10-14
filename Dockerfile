FROM python

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

#EXPOSE 4200
EXPOSE 80

CMD ["python", "app.py"]
