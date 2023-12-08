import tkinter as tk
from tkinter import ttk
import googlemaps
import pandas as pd
import threading
import time

# Initialize Google Maps Client
gmaps = googlemaps.Client(key='YOUR_API_KEY')

def fetch_data(location, keyword, progress, label):
    try:
        data = []
        query = {'query': keyword, 'location': location, 'radius': 1000}
        response = gmaps.places(**query)
        total_fetched = 0
        limit = 60  # Default limit set by Google Maps API

        while True:
            results = response.get('results', [])
            for place in results:
                if total_fetched >= limit:
                    return data  # Stop fetching if the limit is reached
                
                # Update progress bar and label
                progress['value'] = (total_fetched + 1) / limit * 100
                label.config(text=f"Entries fetched: {total_fetched + 1}/{limit}")
                progress.update_idletasks()
                label.update_idletasks()

                # Fetching additional details for each place
                place_details = gmaps.place(place_id=place['place_id'])['result']

                # Extracting required information
                name = place_details.get('name', 'N/A')
                phone = place_details.get('formatted_phone_number', 'N/A')
                address = place_details.get('formatted_address', 'N/A')
                website = place_details.get('website', 'No Website')
                reviews_count = len(place_details.get('reviews', []))

                data.append({
                    'Name': name,
                    'Phone': phone,
                    'Address': address,
                    'Website': website,
                    'Reviews Count': reviews_count
                })

                total_fetched += 1

            # Check if there is a next page
            next_page_token = response.get('next_page_token')
            if next_page_token and total_fetched < limit:
                time.sleep(2)  # Delay needed to wait for the next page token to become valid
                response = gmaps.places(**query, page_token=next_page_token)
            else:
                break

        save_to_excel(data)
    except Exception as e:
        print(f"Error fetching data from Google Maps API: {e}")

def save_to_excel(data):
    if data:
        df = pd.DataFrame(data)
        df.to_excel('output.xlsx', index=False)
    else:
        print("No data to save.")

def start_fetching(location, keyword, progress, label):
    threading.Thread(target=fetch_data, args=(location, keyword, progress, label), daemon=True).start()

def main():
    root = tk.Tk()
    root.title("GmapZ - RaviTejaChillara")

    tk.Label(root, text="Coordinates (latitude,longitude):").pack()
    location_entry = tk.Entry(root)
    location_entry.pack()

    tk.Label(root, text="Search keyword:").pack()
    keyword_entry = tk.Entry(root)
    keyword_entry.pack()

    progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=300, mode='determinate')
    progress.pack()

    fetched_label = tk.Label(root, text="Entries fetched: 0 / 60")
    fetched_label.pack()

    fetch_button = tk.Button(root, text="Fetch Data", command=lambda: start_fetching(location_entry.get(), keyword_entry.get(), progress, fetched_label))
    fetch_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
