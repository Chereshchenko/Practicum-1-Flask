from flask import Flask

app = Flask(__name__)
app.secret_key = 'cb02820a3e94d72c9f950ee10ef7e3f7a35b3f5b'

from app import routes