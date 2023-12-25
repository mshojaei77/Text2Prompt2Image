from flask import Flask, render_template, request
import replicate
import os

# Set the replicate API token
os.environ["REPLICATE_API_TOKEN"] = "YOUR_REPLICATE_API_TOKEN"

# Create the flask app object
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Render the home template
    return render_template('home.html')

# Define the route for the result page
@app.route('/result')
def result():
    # Get the user input from the form
    user_input = request.args.get('user_input')

    # Generate the image prompt using replicate
    prompt_generator = replicate.run(
  "mistralai/mixtral-8x7b-instruct-v0.1:7b3212fbaf88310cfef07a061ce94224e82efc8403c26fc67e8f6c065de51f21",
  input={
    "top_k": 50,
    "top_p": 0.9,
    "prompt": f"rewrite following text to a professional image generation prompt:\n{user_input}",
    "temperature": 0.6,
    "max_new_tokens": 1024,
    "prompt_template": "<s>[INST] {prompt} [/INST] ",
    "presence_penalty": 0,
    "frequency_penalty": 0
  }
)

    prompt = "".join(prompt_generator)

    # Generate the image output using replicate
    output = replicate.run(
        "playgroundai/playground-v2-1024px-aesthetic:42fe626e41cc811eaf02c94b892774839268ce1994ea778eba97103fe1ef51b8",
        input={
            "width": 1024,
            "height": 1024,
            "prompt": prompt,
            "scheduler": "K_EULER_ANCESTRAL",
            "guidance_scale": 3,
            "apply_watermark": False,
            "negative_prompt": "",
            "num_inference_steps": 50
        }
    )

    # Render the result template with the prompt and the output
    return render_template('result.html', prompt=prompt, output=output)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
