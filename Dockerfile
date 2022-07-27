FROM python

WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /app/

EXPOSE 8086

COPY . .

COPY ./.venv/Lib/site-packages/flask_apispec/static /usr/local/lib/python3.10/site-packages/flask_apispec/static

CMD [ "waitress-serve", "--port=5000", "app:app" ]