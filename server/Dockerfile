FROM python:3.9

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./backend /src/backend

EXPOSE 3001

CMD ["uvicorn", "backend.server:app", "--host", "0.0.0.0", "--port", "3001"]
