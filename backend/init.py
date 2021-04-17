from flask import Flask

# App initialization.
backend = Flask(__name__)


@backend.route("/status", methods=["GET"])
def status():
    return "OK"

# @mgr.route("/pga/<int:pga_id>/start", methods=["PUT"])
# def start_pga(pga_id):
#     """
#     Starts the PGA identified by the pga_id route param.


@backend.route("/doSomething", methods=["GET"])
def doForText():
    return "Hi"


@backend.route("/doSomething", methods=["GET"])
def doForFile():
    return "Hi"


if __name__ == "__main__":
    backend.run(host="0.0.0.0")
