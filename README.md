# Web Scraper

## Overview
This project is a simple web scraper built using Python. It extracts **text-only content** from a specified web page and saves it to a local file. The application features a graphical user interface (GUI) powered by Tkinter, making it user-friendly for non-technical users.

## Features
- Extracts all text content from a web page using the URL provided by the user.
- Saves the extracted content to a specified text file.
- Error handling for invalid URLs, network issues, and file saving errors.

## Requirements
To run this project, you need:

1. Python 3.6 or later
2. The following Python libraries:
   - `tkinter` (comes pre-installed with Python on most platforms)
   - `requests`
   - `beautifulsoup4`

## Installation
1. Clone or download this repository.
2. Install the required Python libraries by running:
   ```bash
   pip install requests beautifulsoup4
   ```

## Usage
1. Run the `main.py` script:
   ```bash
   python main.py
   ```
2. In the GUI:
   - Enter the URL of the web page in the "Enter URL" field.
   - Enter the desired file name (e.g., `output.txt`) in the "File Name" field.
   - Click the "SAVE" button.
3. The extracted text content will be saved to the specified file. Check the status message for success or error feedback.

## Example
- **Input**: URL: `https://example.com`, File Name: `example_output.txt`
- **Output**: A text file `example_output.txt` containing the text-only content of the web page.

## Error Handling
- **Invalid URL**: The application will display an error message if the URL is malformed or unreachable.
- **File Saving Issues**: If the file cannot be saved (e.g., due to invalid file name or permissions), a descriptive error message will be shown.

## Known Limitations
- The scraper does not handle JavaScript-rendered content.
- The output is raw text without formatting or structure.
- Requires internet access to fetch the web page content.

## Future Enhancements
- Add support for JavaScript-rendered pages using a headless browser (e.g., Selenium).
- Improve error messages with more specific diagnostics.
- Allow additional output formats, such as JSON or Markdown.

## License
This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Requests](https://docs.python-requests.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

---
Enjoy using the Web Scraper! Feel free to contribute or suggest improvements.

