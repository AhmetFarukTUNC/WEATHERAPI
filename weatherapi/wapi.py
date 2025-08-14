from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Tüm origin'lere izin ver

# WeatherAPI bilgileri
URL = "http://api.weatherapi.com/v1/current.json"
ACCESS_KEY = "90d85b1ded144b2eaff173943251408"

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    try:
        # API isteği
        response = requests.get(URL, params={
            "key": ACCESS_KEY,
            "q": city,
            "lang": "en"  # İngilizce sonuçlar
        })
        data = response.json()

        if "error" in data:
            return jsonify({"error": data["error"]["message"]}), 400

        # API'den gelen verileri düzenle
        result = {
            "city": data["location"]["name"],
            "temperature_c": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"].lower()
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
