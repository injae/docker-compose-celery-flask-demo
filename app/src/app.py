from flask import Flask
from tasks import celery_app

app = Flask(__name__)

@app.route('/')
def home():
    result = celery_app.send_task('tasks.add', [1,2])
    result.ready()
    return str(result.get())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 
