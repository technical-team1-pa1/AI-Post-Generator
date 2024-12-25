import openai
from image_analyzer import ImageAnalyzer
import os
from dotenv import load_dotenv

class LinkedInPostGenerator:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.image_analyzer = ImageAnalyzer()
    
    def generate_post(self, image_path):
        # Analyze the image
        image_analysis = self.image_analyzer.analyze_image(image_path)
        
        # Create prompt for GPT
        prompt = f"""
        Generate a professional LinkedIn post about the following image:
        Image caption: {image_analysis['caption']}
        Main topics: {', '.join(image_analysis['tags'][:5])}
        Objects detected: {', '.join(image_analysis['objects'])}
        
        The post should:
        1. Start with an engaging hook
        2. Include relevant insights or lessons
        3. End with a call to action
        4. Include 3-4 relevant hashtags
        5. Be professional and engaging
        6. Be between 150-300 words
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional LinkedIn content creator."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content 