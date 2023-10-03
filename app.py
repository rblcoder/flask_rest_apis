import os
from flask import Flask
import yaml
import pprint

app = Flask(__name__)


@app.route("/")
def hello_world():
    # name = os.environ.get("NAME", "World")
    # return "Hello {}!".format(name)

    with open('.github/workflows/changed-files.yml', 'r') as file:
        load_yaml = yaml.safe_load(file)
        print(type(load_yaml))
        result_yaml = pprint.pformat(load_yaml)
        print(result_yaml)
        return str(load_yaml)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
