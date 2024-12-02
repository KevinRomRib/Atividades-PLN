from flask import Flask, request, jsonify
from Chatbot import chatbot

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    entrada_usuario = request.json.get("mensagem")
    resposta = chatbot(entrada_usuario)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)
