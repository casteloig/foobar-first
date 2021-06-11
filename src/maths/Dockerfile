FROM python

RUN mkdir /app
WORKDIR /app

COPY mathy.py .
COPY funcs.py .
COPY requirements.txt .

EXPOSE 4002

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "mathy.py" ]