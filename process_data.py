import json
from datetime import datetime

# Load the cruise history JSON file
try:
    with open('../cruise_history.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: /home/dwhicker/work/homepage/../cruise_history.json not found.")
    exit()

# --- Data Processing Functions ---

def extract_unique_ports(all_itineraries):
    """Extracts a set of unique port names across all cruises."""
    ports = set()
    for cruise in all_itineraries:
        if 'itinerary' in cruise and isinstance(cruise['itinerary'], list):
            # Focus specifically on types explicitly marked as 'port'
            for day in cruise['itinerary']:
                port = day.get('port')
                if port:
                    ports.add(port)
    return sorted(list(ports))

def extract_summary_data(all_itineraries):
    """Creates a simplified, clean list of data points suitable for the index page."""
    summaries = []
    for cruise in all_itineraries:
        # Calculate total days at sea (count instances where type is 'sea_day')
        days_at_sea = sum(1 for day in cruise.get('itinerary', []) if day.get('type') == 'sea_day')

        summary = {
            "cruise_id": cruise.get("cruise_id"),
            "cruise_name": cruise.get("cruise_name", "N/A"),
            "ship": cruise.get("ship", "Unknown Ship"),
            "cruise_line": cruise.get("cruise_line", "N/A"),
            "booking_number": cruise.get("booking_number", "None Provided"),
            # Simple date extraction (Assumes structured data)
            "embarkation_date": cruise.get('embarkation', {}).get('date', 'N/A'),
            "disembarkation_date": cruise.get('disembarkation', {}).get('date', 'N/A'),
            "length_nights": cruise.get("length_nights", '?'),
            "days_at_sea": days_at_sea,
        }
        summaries.append(summary)
    return summaries

def process_and_save(data):
    """Runs full processing pipeline and prints the results required for HTML injection."""
    print("# --- CRUISE DATA PROCESSING REPORT ---")
    
    # Get all unique ports (Useful for future search/filtering features)
    unique_ports = extract_unique_ports(data)
    print(f"UNIQUE_PORTS_START\n{json.dumps(unique_ports)}\nUNIQUE_PORTS_END")

    # Get the simplified list of cruise summaries
    summary_list = extract_summary_data(data)
    print("SUMMARY_LIST_START")
    print(json.dumps(summary_list, indent=2))
    print("SUMMARY_LIST_END")


if __name__ == "__main__":
    process_and_save(data)

# The output of this script will be parsed to populate the 'CRUISE_DATA' array in index.html
