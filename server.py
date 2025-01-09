from flask import Flask, request
import os

app = Flask(__name__)

# Переменные окружения
GROUP_TOKEN = os.environ.get("GROUP_TOKEN")
CONFIRMATION_TOKEN = os.environ.get("CONFIRMATION_TOKEN")

@app.route("/", methods=["POST"])
def callback():
    data = request.get_json()

    # Подтверждение сервера
    if data["type"] == "confirmation":
        return CONFIRMATION_TOKEN

    # Обработка событий
    if data["type"] == "message_new":
        user_id = data["object"]["message"]["from_id"]
        message_text = data["object"]["message"]["text"]
        print(f"Сообщение от {user_id}: {message_text}")
    return "ok"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
