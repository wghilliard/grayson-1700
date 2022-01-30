FROM python:3.8
WORKDIR /opt/ner

RUN pip install --upgrade wheel setuptools

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt
RUN python -m spacy download en_core_web_sm

COPY . .
RUN pip --no-cache-dir install .

EXPOSE 8080

ENTRYPOINT ["uvicorn", "--port", "8080", "--host", "0.0.0.0", "--workers", "3", "ner.app:app"]