

from flask import Flask, request, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize Flask app
app = Flask(__name__)

# Initialize ChatterBot
chatbot = ChatBot('WorldbuildingAI')

# Uncomment the following line to enable training with ChatterBot corpus
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train('chatterbot.corpus.english')

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for chatbot interaction
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    bot_response = chatbot.get_response(user_message)
    return str(bot_response)

if __name__ == '__main__':
    app.run(debug=True)
