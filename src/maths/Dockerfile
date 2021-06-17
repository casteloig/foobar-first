FROM python

RUN mkdir -p /src/maths
WORKDIR /src/maths

COPY mathy.py .
COPY funcs.py .
COPY requirements.txt .

ENV PYTHONPATH "${PYTHONPATH}:/"

EXPOSE 4002

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "mathy.py" ]