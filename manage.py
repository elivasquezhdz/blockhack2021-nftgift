from flask import  jsonify, flash,request, Flask, make_response,redirect,render_template

app = Flask(__name__)


app.config['SECRET_KEY'] = '5661528zx0b18ce5c602dgde210wa329'

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
@app.route("/")
def index():
    return render_template("NFTGIFT.html")

@app.route("/photo")
def photo():
    return render_template("NFTGift_Photo.html")
    #return redirect("https://ipfs.io/ipfs/QmUW8XM7JA7qKvZsJijReUcMgnfWSNYpZAjfz1wnLvWXc5?filename=happy_birthday_nft_card.jpg",302)


@app.route("/c")
def cuenta():
    return render_template("cuenta.html")
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
