from flask import Flask, request, Response
import os

app = Flask(__name__)

GROUP_TOKEN = os.environ.get("GROUP_TOKEN")
CONFIRMATION_TOKEN = os.environ.get("CONFIRMATION_TOKEN")
SECRET_KEY = os.environ.get("SECRET_KEY")  # Если используется


@app.route("/", methods=["POST"])
def callback():
    data = request.get_json()

    # Проверка секретного ключа (если используется)
    if SECRET_KEY and data.get("secret") != SECRET_KEY:
        return Response("Forbidden", status=403, mimetype='text/plain')

    # Обработка запроса подтверждения
    if data.get("type") == "confirmation":
        return Response(CONFIRMATION_TOKEN, mimetype='text/plain')

    # Обработка новых сообщений
    if data.get("type") == "message_new":
        user_id = data["object"]["message"]["from_id"]
        message_text = data["object"]["message"]["text"]
        print(f"Сообщение от {user_id}: {message_text}")
        # Добавьте вашу логику обработки сообщений здесь

    return Response("ok", mimetype='text/plain')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
