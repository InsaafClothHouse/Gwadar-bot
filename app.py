from flask import Flask, request
app = Flask(__name__)
@app.route("/bot", methods=["POST"])
def bot():
    msg = request.form.get("Body", "").lower()
    if "hi" in msg or "salam" in msg or "hello" in msg:
        reply = "Assalam o Alaikum! Gwadar Fabric Store me khush amdeed! Order ke liye number likhen: 1 - Collection, 2 - Payment, 3 - Shop ka pata, 4 - Order karna hai"
    elif msg == "1":
        reply = "Hamari collection dekhne ke liye batayen konsa kapra chahiye? Lawn, Cotton, Wash and Wear?"
    elif msg == "2":
        reply = "Payment: 1 se 3 suit tak - Full payment advance hogi. 3 se zyada suit par - Sirf Half payment advance hogi. COD nahi hai. Shukriya!"
    elif msg == "3":
        reply = "Hamari Shop: Jannat Bazar, Bina Plaza, Gwadar"
    elif msg == "4":
        reply = "Order ke liye batayen kitne suit chahiye? Aur apna naam aur pata bhej den."
    else:
        reply = "Apka message mil gaya! Jawab ke liye 1, 2, 3 ya 4 likhen."
    return f"""<?xml version="1.0" encoding="UTF-8"?><Response><Message>{reply}</Message></Response>"""
if __name__ == "__main__":
    app.run()
