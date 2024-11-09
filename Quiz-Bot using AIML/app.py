from flask import Flask, render_template, request, jsonify
import aiml

app = Flask(__name__)

# Initialize AIML kernel
kernel = aiml.Kernel()
kernel.learn("brain/start.aiml")
kernel.learn("brain/categories.aiml")
kernel.learn("brain/questions.aiml")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get("message")
    bot_response = kernel.respond(user_message)
    return jsonify(response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)
