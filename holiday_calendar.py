import datetime

# Holiday Data for Sikkim (Example)
holidays = [
    {"name": "Republic Day", "date": "2024-01-26", "description": "National holiday in India"},
    {"name": "Independence Day", "date": "2024-08-15", "description": "National holiday in India"},
    {"name": "Losar", "date": "2024-03-21", "description": "Tibetan New Year - Sikkim"},
    {"name": "Buddha Jayanti", "date": "2024-05-05", "description": "Buddha’s birthday"},
]

def create_ics(holidays, filename="sikkim_holidays.ics"):
    """Generate an ICS file with holiday data"""
    with open(filename, "w") as file:
        # Write ICS file headers
        file.write("BEGIN:VCALENDAR\n")
        file.write("VERSION:2.0\n")
        file.write("CALSCALE:GREGORIAN\n")

        for holiday in holidays:
            # Extract holiday details
            name = holiday["name"]
            date = holiday["date"]
            description = holiday["description"]

            # Format date to the correct ICS format (YYYYMMDD)
            start_date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y%m%d")

            # Create event for each holiday
            file.write("BEGIN:VEVENT\n")
            file.write(f"SUMMARY:{name}\n")
            file.write(f"DTSTART;VALUE=DATE:{start_date}\n")
            file.write(f"DTEND;VALUE=DATE:{start_date}\n")  # Same day for single-day event
            file.write(f"DESCRIPTION:{description}\n")
            file.write("END:VEVENT\n")
        
        # Write ICS file footer
        file.write("END:VCALENDAR\n")
    
    print(f"ICS file '{filename}' created successfully!")

if __name__ == "__main__":
    create_ics(holidays)
