FROM python

RUN mkdir -p /src/foo
WORKDIR /src/foo

COPY proto/ ./proto/
COPY foo.py .
COPY requirements.txt .

ENV PYTHONPATH "${PYTHONPATH}:/"

EXPOSE 4000

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "foo.py" ]