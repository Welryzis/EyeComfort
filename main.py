from flask import Flask
from pywebio.platform.flask import webio_view
from WebUI import main_menu
from config import FLASK_SECRET_KEY


app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

app.add_url_rule("/", "webio_view", webio_view(main_menu), methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
