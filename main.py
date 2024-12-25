from post_generator import LinkedInPostGenerator

def main():
    generator = LinkedInPostGenerator()
    
    # Get image path from user
    image_path = input("Enter the path to your image: ")
    
    try:
        # Generate post
        post = generator.generate_post(image_path)
        print("\nGenerated LinkedIn Post:")
        print("-" * 50)
        print(post)
        print("-" * 50)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 