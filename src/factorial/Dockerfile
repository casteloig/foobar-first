FROM python

RUN mkdir /app
WORKDIR /app

COPY factorial.py .
COPY func_factorial.py .
COPY requirements.txt .

EXPOSE 4002

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "factorial.py" ]