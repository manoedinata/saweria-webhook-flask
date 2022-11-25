from flask import Blueprint
from flask import request
import json

main = Blueprint("main_routes", __name__)

def add_comma(num):
    return f"{num:,}"

@main.route("/")
def home():
    return "Hello, World!"

@main.route("/webhook", methods=["POST"])
def webhook():
    req = request.json
    headers = request.headers

    if req["type"] == "donation" and headers.get("Saweria-Callback-Signature"):
        jumlah = req["amount_raw"] - req["cut"]
        jumlah = add_comma(jumlah)

        print("")
        print("Nama donatur: " + req["donator_name"])
        print("Email donatur: " + req["donator_email"])
        print("Jumlah: Rp. " + str(jumlah))
        print("Pesan: " + req["message"])
        print("")

    # print(json.dumps(req, indent=4))
    return "Pesan diterima!"
