from flask import Flask

app = Flask(__name__)  # '__main__'


@app.route('/')
def hello_method():
    return "hello,World EdMan"


if __name__ == '__main__':
    app.run(port=8080)
