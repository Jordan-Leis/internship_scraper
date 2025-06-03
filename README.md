# Internship Scraper Toolkit

A lightweight CLI & GUI tool to scrape internship listings from multiple job boards and save the results as JSON.

### ✅ Supports:
- **Adzuna**
- **Jooble**
- **The Muse**
- **USAJOBS**
- **Remotive**

Use this on your local machine to quickly gather internships for keywords like `"electrical engineering intern"` or `"software developer intern"`.

---

## 📁 Repository Structure

```
internship_pipeline/
├── .env.example         # Example API key file (no secrets)
├── .gitignore           # Ignore .env, venvs, etc.
├── gui.py               # Tkinter GUI interface
├── scraper.py           # Core job scraping logic
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Jordan-Leis/internship_pipeline.git
cd internship_pipeline
```

### 2. Create and activate a virtual environment

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add your API keys

Copy the example file:

```bash
cp .env.example .env
```

Then open `.env` and add your API keys:

```
ADZUNA_APP_ID=your_adzuna_app_id
ADZUNA_APP_KEY=your_adzuna_app_key
JOOBLE_API_KEY=your_jooble_api_key
THE_MUSE_API_KEY=your_themuse_api_key
USA_JOBS_API_KEY=your_usajobs_api_key
USAJOBS_USER_AGENT=your_email@example.com
```

---

## 🖥 GUI Mode

Run the GUI app with:

```bash
python gui.py
```

Then:
1. Enter your search term (e.g., `software engineer intern`)
2. Select which job boards to use
3. Choose an output filename (e.g., `jobs_output.json`)
4. Click “Scrape”

### Example GUI:
![GUI](screenshots/gui_main.png)

---

## 🔍 CLI Mode

To run from the terminal instead:

```bash
python scraper.py
```

It will:
- Print counts for each source
- Save results to `jobs.json` by default

---

## 📄 Output Format

Each API’s results are saved under its own key in the JSON:

```json
{
  "adzuna": [
    {
      "title": "Electrical Engineering Intern",
      "company": { "display_name": "Intelcom" },
      "location": { "display_name": "Canada" },
      "description": "...",
      "redirect_url": "https://adzuna..."
    }
  ],
  "jooble": [...],
  "themuse": [...],
  "usajobs": [...],
  "remotive": [...]
}
```

---

## 🧠 Troubleshooting

- `ModuleNotFoundError`: run `pip install -r requirements.txt`
- Tkinter error on Linux: run `sudo apt install python3-tk`
- GUI won’t open: make sure `.venv` is activated

---

## 📜 License

MIT License — Fork, modify, and build something cool!

---

## 🙌 Author

Made with ❤️ by Jordan Leis

GitHub: https://github.com/Jordan-Leis/internship_pipeline
