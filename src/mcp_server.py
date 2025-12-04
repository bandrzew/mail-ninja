from flask import Flask, request, Response
from azure_openai_client import AzureOpenAIClient
import yaml
import json

# Load styles
with open("src/styles.yml", "r") as file:
    styles = yaml.safe_load(file)["styles"]

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    user_input = data.get("user_input", None)
    style_name = data.get("style", None)

    if not user_input:
        return Response(
            json.dumps({"error": "Invalid input."}, ensure_ascii=False),
            status=500,
            mimetype="application/json"
        )

    selected_style = next(
        (style for style in styles if style["name"] == style_name), None)
    if not selected_style:
        return Response(
            json.dumps({"error": "Invalid style."}, ensure_ascii=False),
            status=500,
            mimetype="application/json"
        )

    client = AzureOpenAIClient()
    response = client.get_response(user_input, selected_style["description"])

    if response:
        return Response(
            json.dumps(response, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    else:
        return Response(
            json.dumps({"error": "Failed to process the request."},
                       ensure_ascii=False),
            status=500,
            mimetype="application/json"
        )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
