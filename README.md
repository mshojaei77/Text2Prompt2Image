# Text2Prompt2Image

Text2Prompt2Image is a Flask-based web application that leverages the Replicate API, integrating both `mistralai/mixtral-8x7b-instruct-v0.1` and `playgroundai/playground-v2-1024px-aesthetic` models. This app allows users to effortlessly convert text into professional image generation prompts, producing visually stunning outputs.

## Setup

1. **Clone Repository:**
   ```bash
   git clone <repository_url>
   cd Text2Prompt2Image
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Replicate API Token:**
   - Open `app.py` and replace `"YOUR_REPLICATE_API_TOKEN"` with your actual Replicate API token from [https://replicate.com/account/api-tokens](https://replicate.com/account/api-tokens)

4. **Run the App:**
   ```bash
   python app.py
   ```

5. **Access the App:**
   Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage

1. **Home Page:**
   - Visit the home page to input your text.

![image](https://github.com/mshojaei77/Text2Prompt2Image/assets/76538971/47437d62-a76a-4f22-8cc0-f085e17213ce)

2. **Result Page:**
   - Navigate to the result page to view the generated prompt and corresponding image.

![image](https://github.com/mshojaei77/Text2Prompt2Image/assets/76538971/0c5272cb-8416-4195-9ea5-02d6871cbd54)


## Models Used

- **Prompt Generation:**
  - Model: `mistralai/mixtral-8x7b-instruct-v0.1:7b3212fbaf88310cfef07a061ce94224e82efc8403c26fc67e8f6c065de51f21`

- **Image Generation:**
  - Model: `playgroundai/playground-v2-1024px-aesthetic:42fe626e41cc811eaf02c94b892774839268ce1994ea778eba97103fe1ef51b8`

## Important Notes

- Ensure you have a valid Replicate API token for seamless functionality.
- This app is currently set to run in debug mode. Adjust configurations for production deployment.

Feel free to explore, contribute, and elevate your content effortlessly with Text2Prompt2Image! 🚀 #Text2Prompt2Image
