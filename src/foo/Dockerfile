FROM python

RUN mkdir /app
WORKDIR /app

COPY proto/ ./proto/
COPY foo.py .
COPY requirements.txt .

EXPOSE 4000

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "foo.py" ]