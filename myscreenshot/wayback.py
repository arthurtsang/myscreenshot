import os
import tempfile
import urllib.parse

from flask import Flask, request, send_file, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

def take_screenshot(url, file_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=file_path, full_page=True)
        browser.close()


@app.route('/screenshot', methods=['GET'])
def screenshot():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Generate a filename from the URL
    parsed_url = urllib.parse.urlparse(url)
    filename = f"{parsed_url.netloc.replace('.', '_')}.png"
    file_path = os.path.join(temp_dir, filename)

    try:
        take_screenshot(url, file_path)

        if os.path.exists(file_path):
            return send_file(file_path, mimetype='image/png')
        else:
            return jsonify({"error": "Could not retrieve the screenshot"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up: remove the temporary directory and its contents
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(temp_dir):
            os.rmdir(temp_dir)


if __name__ == '__main__':
    app.run(debug=True,port=5050)
