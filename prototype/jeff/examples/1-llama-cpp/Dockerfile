FROM python

RUN pip install llama-cpp-python

COPY ./app /app
COPY ./models/*.gguf /app
WORKDIR /app

CMD ["python", "test.py"]   