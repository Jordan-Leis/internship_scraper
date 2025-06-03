# gui.py

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from scraper import fetch_adzuna, fetch_jooble, fetch_themuse, fetch_usajobs, fetch_remotive

class JobScraperGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Job Scraper")
        self.geometry("400x300")
        self.resizable(False, False)

        # Query entry
        ttk.Label(self, text="Search Query:").pack(pady=(20, 0))
        self.query_var = tk.StringVar(value="electrical engineer intern")
        ttk.Entry(self, textvariable=self.query_var, width=40).pack()

        # Checkboxes for sources
        self.sources_frame = ttk.LabelFrame(self, text="Sites to scrape")
        self.sources_frame.pack(pady=15, padx=15, fill="x")
        self.vars = {}
        for site in ["adzuna", "jooble", "themuse", "usajobs", "remotive"]:
            var = tk.BooleanVar(value=True)
            chk = ttk.Checkbutton(self.sources_frame, text=site.capitalize(), variable=var)
            chk.pack(anchor="w", padx=10)
            self.vars[site] = var

        # Output filename
        ttk.Label(self, text="Output file:").pack(pady=(10, 0))
        self.output_var = tk.StringVar(value="jobs_output.json")
        ttk.Entry(self, textvariable=self.output_var, width=40).pack()

        # Scrape button
        ttk.Button(self, text="Scrape", command=self.do_scrape).pack(pady=20)

    def do_scrape(self):
        query = self.query_var.get().strip()
        output_file = self.output_var.get().strip()
        if not query:
            messagebox.showerror("Error", "Please enter a search query.")
            return
        results = {}
        if self.vars["adzuna"].get():
            try:
                results["adzuna"] = fetch_adzuna(query)
            except Exception as e:
                results["adzuna_error"] = str(e)
        if self.vars["jooble"].get():
            try:
                results["jooble"] = fetch_jooble(query)
            except Exception as e:
                results["jooble_error"] = str(e)
        if self.vars["themuse"].get():
            try:
                results["themuse"] = fetch_themuse()
            except Exception as e:
                results["themuse_error"] = str(e)
        if self.vars["usajobs"].get():
            try:
                results["usajobs"] = fetch_usajobs(query)
            except Exception as e:
                results["usajobs_error"] = str(e)
        if self.vars["remotive"].get():
            try:
                results["remotive"] = fetch_remotive(query)
            except Exception as e:
                results["remotive_error"] = str(e)

        # Save JSON
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("Success", f"Results saved to {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not write to {output_file}:\n{e}")

if __name__ == "__main__":
    app = JobScraperGUI()
    app.mainloop()
