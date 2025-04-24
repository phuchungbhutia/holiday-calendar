# 🗓️ Holiday Calendar for Sikkim – ICS Generator

Welcome to the **Holiday Calendar Generator** project by [@phuchungbhutia](https://github.com/phuchungbhutia)!  
This tool helps you generate `.ics` (iCalendar) files from custom holiday lists — ideal for importing Sikkim-specific public holidays and personal events directly into **Google Calendar** or other calendar apps.

---

## 📌 Features

- ✅ Generate `.ics` files for regional, personal, or recurring holidays
- 📅 Supports fixed and variable dates
- 🔁 Allows repeat setup for recurring events (e.g., Republic Day every year)
- 🧠 Easy to extend with your own CSV or JSON holiday data
- 🔗 Compatible with Google Calendar, Apple Calendar, Outlook, and more

---

## 📂 Project Structure

```
holiday-calendar/
├── README.md               # Project info and usage guide
├── LICENSE                 # MIT License
├── .gitignore              # Files/folders ignored by Git
├── holiday_calendar.py     # Main script to generate ICS files
├── holidays_data/          # Optional: CSV or JSON holiday inputs
│   └── sikkim_holidays.csv # Example CSV with Sikkim holidays
├── output/                 # Generated ICS files
│   └── sikkim_holidays.ics # Your calendar output
└── requirements.txt        # Python dependencies
```

---

## 🛠️ Installation

### ✅ Prerequisites

- Python 3.8+
- Git (for cloning)
- Internet connection (to install dependencies)

### 📥 Clone the Repository

```bash
git clone https://github.com/phuchungbhutia/holiday-calendar.git
cd holiday-calendar
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Usage

Run the script to generate an `.ics` file using the built-in holiday list:

```bash
python holiday_calendar.py
```

Output will be saved in the `/output` directory as `sikkim_holidays.ics`.

To import into **Google Calendar**:
1. Go to [Google Calendar](https://calendar.google.com).
2. Click ⚙️ > **Settings** > **Import & Export**.
3. Upload your `.ics` file and choose a calendar to import to.

---

## ✍️ Customize Your Holiday List

You can manually edit the `holidays` list in `holiday_calendar.py`, or:

1. Add your custom holiday data as a CSV in `holidays_data/`.
2. Modify the script to load holidays from that file using `pandas`.

---

## 🔄 Recurring Events

For holidays like:
- **Second Saturday**
- **Fourth Saturday**

You can set recurrence rules manually after importing into Google Calendar, or extend the script for recurrence logic.

---

## 📊 GitHub Stats & Widgets

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=phuchungbhutia&show_icons=true&theme=default&count_private=true)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=phuchungbhutia&layout=compact)

---

## 🪪 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Have improvements or new features in mind?
- Fork the repo
- Create a feature branch
- Submit a pull request!

---

## 🙌 Author

Made with ❤️ by [Phuchung Bhutia](https://github.com/phuchungbhutia)

```

---
