Job Scraper Toolkit
A lightweight CLI & GUI tool to scrape internship listings from multiple job boards and save the results as JSON. Supports:

Adzuna

Jooble

The Muse

USAJOBS

Remotive

Use this on your local machine to quickly gather internships for “electrical engineering,” “software engineering,” or any other keyword.

📂 Repository Structure
graphql
Copy
Edit
internship_pipeline/
├── .env.example         # Example environment‐variable file (no real keys)
├── .gitignore           # Files & folders to ignore in Git
├── gui.py               # Tkinter GUI for easy scraping
├── scraper.py           # Core CLI scraper functions
├── requirements.txt     # Python dependencies
└── README.md            # This documentation
Note: Any locally generated files (e.g. jobs_output.json) or your personal .env should be ignored by Git.

🚀 Getting Started
Follow these steps to clone, configure, and run the scraper on your local machine.

1. Clone the repository
Open your terminal (Linux/macOS) or PowerShell (Windows):

bash
Copy
Edit
git clone https://github.com/Jordan-Leis/internship_pipeline.git
cd internship_pipeline
2. Create & activate a virtual environment
It’s best practice to isolate dependencies in a Python virtual environment.

On Linux/macOS:

bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
On Windows (PowerShell):

mathematica
Copy
Edit
python -m venv .venv
.venv\Scripts\Activate.ps1
Your prompt should change to show (.venv) at the beginning, indicating the virtual environment is active.

3. Install dependencies
Run:

css
Copy
Edit
pip install --upgrade pip
pip install -r requirements.txt
This installs:

requests

python-dotenv

4. Configure API keys
Copy .env.example to .env:

bash
Copy
Edit
cp .env.example .env
Open .env in your text editor and fill in your own keys. For example:

ini
Copy
Edit
ADZUNA_APP_ID=your_adzuna_id_here
ADZUNA_APP_KEY=your_adzuna_key_here
JOOBLE_API_KEY=your_jooble_key_here
THE_MUSE_API_KEY=your_themuse_key_here
USA_JOBS_API_KEY=your_usajobs_key_here
USAJOBS_USER_AGENT=youremail@example.com
Note: For USAJOBS, USER_AGENT must be a valid email address your account is registered with.

If you don’t have certain API keys, you can leave those lines blank. The GUI/CLI will skip sites with missing keys.

5. Run the CLI scraper
To simply view how many jobs each source returns:

nginx
Copy
Edit
python scraper.py
You should see output like:

bash
Copy
Edit
adzuna:  20 jobs
jooble:  15 jobs
themuse: 10 jobs
usajobs:  5 jobs
remotive:  25 jobs
If any site reports an authentication or network error, double-check that the corresponding variables in your .env are correct.

🖥 GUI Mode (Tkinter)
For a more user-friendly experience, use the Tkinter GUI:

nginx
Copy
Edit
python gui.py
A window will appear—enter:

Search Query
e.g. electrical engineer intern

Sites to scrape (check/uncheck any combination of Adzuna, Jooble, TheMuse, USAJOBS, Remotive)

Output file
By default, jobs_output.json.

Click “Scrape” to fetch data. After a few seconds, a popup will confirm success. The file you specified will be created in the current directory.

GUI Screenshots
Below is the main window:

<img src="https://github.com/Jordan-Leis/internship_pipeline/raw/main/screenshots/gui_main.png" alt="GUI Main Window" width="800"/>
After clicking Scrape, you’ll see a confirmation dialog, and the JSON will look like this example (abridged):

<img src="https://github.com/Jordan-Leis/internship_pipeline/raw/main/screenshots/jobs_output.png" alt="Sample Output JSON" width="800"/>
📁 Output JSON Format
The JSON file (jobs_output.json) has a top-level key for each selected site. For example:

json
Copy
Edit
{
  "adzuna": [
    {
      "id": "5198180866",
      "title": "Electrical Engineering Intern",
      "company": {
        "display_name": "Intelcom Courier Canada"
      },
      "description": "Ride the next mile with us! The lab’s mission is to develop ...",
      "location": {
        "display_name": "Canada"
      },
      ... (other Adzuna fields) ...
    },
    ...
  ],
  "jooble": [
    {
      "title": "Electrical Engineer Intern",
      "company": "SomeCompany",
      "location": "New York, NY",
      "snippet": "We are seeking an Electrical Engineer Intern to assist with ...",
      "url": "https://jooble.org/...",
      ... (other Jooble fields) ...
    },
    ...
  ],
  "themuse": [ … ],
  "usajobs": [ … ],
  "remotive": [ … ]
}
You can open this in any text editor or parse it in Python/JavaScript to extract whatever fields you need.

🛠 Tips & Troubleshooting
Missing API keys?

If you leave an environment variable blank, that site will show up as “error” in the GUI or CLI. You can still scrape from others.

Network or SSL errors?

Be sure your machine’s date/time is correct.

The code uses requests.get(…, timeout=10). If your connection is slow, you can increase the timeout value inside scraper.py.

Tkinter not found? (Windows)

Normally Windows Python includes Tkinter. If you see an import error, install python3-tk:

powershell
Copy
Edit
pip install tk
On Linux (Ubuntu/Debian):

bash
Copy
Edit
sudo apt update
sudo apt install python3-tk
Updating code

If you clone and pull new changes later, make sure to git pull inside your local folder and then run:

nginx
Copy
Edit
pip install -r requirements.txt
to install any new dependencies.

🎯 Usage Examples
1. Quick CLI check
nginx
Copy
Edit
python scraper.py
2. Full GUI
nginx
Copy
Edit
python gui.py
Enter "software engineer intern"

Check “Adzuna” & “Remotive”

Type software_interns.json as output

Click Scrape

Inspect software_interns.json in your editor

📜 License
This project is licensed under the MIT License. See LICENSE for details.

Attributions & Links
Adzuna API Docs: https://developer.adzuna.com

Jooble API Docs: https://jooble.org/api/about

TheMuse API: https://github.com/TheMuse/Yeah

USAJOBS API: https://developer.usajobs.gov/api-reference/

Remotive API: https://github.com/remotive-com/remote-jobs-api
