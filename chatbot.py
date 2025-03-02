from flask import Flask, render_template, request
from transformers import pipeline

# Initialize the chatbot model using a pre-trained model from Hugging Face's transformers library
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    # Get the user input from the form
    user_input = request.form['user_input']
    
    # Get the chatbot's response
    response = chatbot(user_input)
    
    # Extract the response from the chatbot output
    bot_output = response[0]['generated_text']
    
    return render_template("index.html", user_input=user_input, bot_output=bot_output)

if __name__ == "__main__":
    app.run(debug=True)
