from flask import Flask, render_template, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def generate_linkedin_post(topic, include_emojis=True, hashtag_count=3):
    emoji_requirement = "- Add relevant emojis naturally (but don't overuse them)" if include_emojis else "- Do not include any emojis"
    
    prompt = f"""Create a LinkedIn post about {topic}. 
    
Requirements:
{emoji_requirement}
- Include exactly {hashtag_count} relevant hashtags at the end
- Keep it engaging and authentic
- Include a call-to-action that encourages meaningful discussion
- Length should be between 400-600 words
Use following information to refine the paragraph:
- Adding short, abrupt sentences.
- Mixing formal and casual tones.
- Using storytelling instead of rigid formatting.
- Make Subtle grammatical errors

Make it feel like it's written by a real person sharing their thoughts, not a corporate message."""
    
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a guy who writes authentic, engaging LinkedIn posts for tech, business, company, educational content, product launches, Events and startups in a natural human tone. Make 30 percent grammer mistake in the whole content Write in a natural, conversational human language Include a short story, experience or anecdote, Include personal insights or experiences. If needed then provide bullet points. use common conversational words like (You know, I think, etc)"},
            {"role": "user", "content": prompt}
        ],
        model="mixtral-8x7b-32768",
        temperature=0.7,
    )
    
    return response.choices[0].message.content

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    topic = data.get('topic', '')
    include_emojis = data.get('include_emojis', True)
    hashtag_count = int(data.get('hashtag_count', 3))
    
    try:
        post = generate_linkedin_post(topic, include_emojis, hashtag_count)
        return jsonify({'status': 'success', 'post': post})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 