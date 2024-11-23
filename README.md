# Quizlet Terms Exporter

A collection of scripts written in Python and JavaScript to export terms and definitions from any Quizlet set. This repository is designed to provide multiple methods for scraping and exporting Quizlet content into a usable format.

I might add other tools to this repo in the future, but currently it's just a quizlet term exporter. 😀

---

## Features

- Export terms and definitions from public Quizlet sets.
- Output in various formats such as JSON, CSV, or plain text.
- Scripts currently available in Python and JavaScript.
- Support for additional languages or formats can be added upon request.

---

## File Structure

```plaintext
Quizlet-MultiTool/
├── python/
│   ├── export_quizlet.py        # Python script for single set export
│   ├── batch_export.py          # Python script for batch export
│   ├── utils/                   # Utility modules
│   └── requirements.txt         # Python dependencies
├── javascript/
│   ├── exportQuizlet.js         # Puppeteer-based scraping script
│   └── package.json             # JavaScript dependencies
├── examples/
│   ├── output_sample.json       # Example output (from [Spelling Bee](https://quizlet.com/257331262/spelling-bee-flash-cards/))
│   └── urls.txt                 # Example input for batch processing
└── README.md                    # Documentation
```

---

## Support for Additional Languages

This project is designed with flexibility in mind, and support for exporting Quizlet terms in other programming languages can be added based on user requests. If there's a specific language you'd like supported, feel free to reach out or open an issue in the repository.

---

## Legal Disclaimer

This tool is for educational purposes only. Scraping content from Quizlet may violate their Terms of Service. Use responsibly and ensure you have permission to export any set data.
