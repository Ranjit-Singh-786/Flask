from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Example route in your Flask app to trigger sending JSON to the external API
@app.route('/send-data', methods=['GET'])
def send_data():
    # API endpoint from your developer
    api_url = "http://192.168.0.48:1073/addmodifycamerasettings/save-empcam-details"

    # JSON data you want to send
    data_to_send = {
    "indId": "56",
    "cameraId": "78",
    "empcamDirection": "fghfgh",
    "empcamInout": "fghfh",
    "empcamRemark": "ewfrs",
    "empcamDt": "23/09/2023",
    "empcamTime": "23/09/2023 16:27:53"
    
}
    try:
        # Send POST request
        response = requests.post(api_url, json=data_to_send)

        # Optional: Return the response from the external API
        return jsonify({
            "status": "success",
            "api_status_code": response.status_code,
            "api_response": response.json()  # Make sure the external API returns JSON
        })

    except requests.exceptions.RequestException as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
