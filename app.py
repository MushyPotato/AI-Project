from flask import Flask, render_template, request, jsonify
from groq import Groq

client = Groq(api_key="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")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process-form", methods=["POST"])
def process_form():
    user_input = request.form.get("userInput")

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": """You are an AI coding assistant that helps fix/generate code. Make sure to format the code for the user depending on language."""},
            {"role": "user", "content": f"""{user_input}"""},
        ],
        model="llama-3.3-70b-versatile",
    )
    response = chat_completion.choices[0].message.content

    return jsonify({"message": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

