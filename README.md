# Web Image Downloader

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Dependencies](https://img.shields.io/badge/dependencies-requests%20%7C%20beautifulsoup4-brightgreen.svg)](#prerequisites)

A simple, fast, and automated Python script designed to scrape and download all images from any target website URL into a local directory.

---

## Table of Contents

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Setup & Installation](#setup--installation)
- [How to Use](#how-to-use)
- [Pros and Cons](#pros-and-cons)
- [Precautions](#precautions)
- [Contributing](#contributing)
- [License](#license)
- [Thanks](#thanks)

---

## Description

The **Web Image Downloader** automates the tedious task of manually saving images from web pages. By inspecting HTML `<img>` tags, resolving relative URLs, and downloading raw image data, this script pulls all embedded media from a provided web address and stores it neatly in a dedicated folder.

---

## Prerequisites

Before running the application, ensure you have Python installed along with the following required libraries:

- **Python 3.8+**
- `requests` (for making HTTP requests)
- `beautifulsoup4` (for HTML parsing)

---

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/web-image-downloader.git
   cd web-image-downloader
   ```

2. **Install required dependencies:**
   ```bash
   pip install requests beautifulsoup4
   ```

---

## How to Use

### Command to Run

Execute the script from your terminal:

```bash
python scraper.py
```

### Step-by-Step Instructions

1. Run the script using the command above.
2. Enter the full website URL (e.g., `https://example.com`) when prompted.
3. The script will create an `images/` directory if it does not already exist.
4. Images will download automatically and appear in the `images/` folder with incremented filenames (e.g., `image_1.jpg`, `image_2.png`).

---

## Pros and Cons

### Pros
- **Automated:** Saves time by downloading images in bulk.
- **Robust URL Handling:** Automatically converts relative paths (`/img/pic.jpg`) to absolute URLs (`https://example.com/img/pic.jpg`).
- **Dynamic Extensions:** Retains correct original file extensions (`.png`, `.jpg`, `.svg`, etc.).
- **Error Handling:** Gracefully skips broken links without crashing the script.

### Cons
- **Dynamic Content:** Cannot scrape images rendered dynamically via client-side JavaScript (e.g., React/Vue applications without SSR).
- **Rate Limits:** Downloading too many images too quickly may trigger temporary IP bans from strict host servers.

---

## Precautions

- **Copyright Compliance:** Ensure you have permission or the proper rights before downloading and using images from third-party websites.
- **Server Load:** Be respectful of website resources; avoid scraping server-heavy sites excessively.
- **Bot Detection:** Some web services actively block requests lacking standard browser headers or headers associated with scrapers.

---

## Contributing

Contributions, issues, and feature requests are welcome!

1. **Fork** the repository.
2. Create a new feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a **Pull Request**.

---

## License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## Thanks

Special thanks to:
- The [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) team for their excellent HTML parsing library.
- The [Requests](https://requests.readthedocs.io/) team for simplified HTTP interactions.
