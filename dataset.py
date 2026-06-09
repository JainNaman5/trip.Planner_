# dataset.py
"""
Curated database of popular Indian travel destinations,
complete with coordinates, descriptions, ideal season, cost structures,
and top attractions for map plotting.
"""

DESTINATIONS = {
    "Jaipur": {
        "name": "Jaipur",
        "state": "Rajasthan",
        "region": "North",
        "category": "Heritage & Culture",
        "description": "Known as the 'Pink City', Jaipur is famous for its magnificent forts, opulent palaces, and vibrant markets reflecting rich Rajasthani heritage.",
        "best_season": "October to March",
        "latitude": 26.9124,
        "longitude": 75.7873,
        "costs": {
            "accommodation": {"Budget": 1200, "Mid-Range": 3500, "Luxury": 12000},
            "food": {"Budget": 400, "Mid-Range": 1000, "Luxury": 2500},
            "transport": {"Budget": 300, "Mid-Range": 800, "Luxury": 2500},
            "activity_avg": 500
        },
        "attractions": [
            {"name": "Amber Palace", "lat": 26.9855, "lon": 75.8513, "type": "Fort", "fee": 500},
            {"name": "Hawa Mahal", "lat": 26.9239, "lon": 75.8267, "type": "Monument", "fee": 200},
            {"name": "City Palace", "lat": 26.9258, "lon": 75.8237, "type": "Palace", "fee": 700},
            {"name": "Jantar Mantar", "lat": 26.9248, "lon": 75.8245, "type": "Observatory", "fee": 200},
            {"name": "Nahargarh Fort", "lat": 26.9374, "lon": 75.8156, "type": "Fort", "fee": 200}
        ]
    },
    "Udaipur": {
        "name": "Udaipur",
        "state": "Rajasthan",
        "region": "North",
        "category": "Romance & Lakes",
        "description": "Often called the 'City of Lakes' and the 'Venice of the East', Udaipur is surrounded by the beautiful Aravalli Hills and stunning palaces.",
        "best_season": "September to March",
        "latitude": 24.5854,
        "longitude": 73.7125,
        "costs": {
            "accommodation": {"Budget": 1500, "Mid-Range": 4500, "Luxury": 18000},
            "food": {"Budget": 450, "Mid-Range": 1200, "Luxury": 3000},
            "transport": {"Budget": 350, "Mid-Range": 1000, "Luxury": 2800},
            "activity_avg": 400
        },
        "attractions": [
            {"name": "City Palace Udaipur", "lat": 24.5764, "lon": 73.6835, "type": "Palace", "fee": 300},
            {"name": "Lake Pichola (Boating)", "lat": 24.5684, "lon": 73.6791, "type": "Lake", "fee": 400},
            {"name": "Jag Mandir", "lat": 24.5678, "lon": 73.6782, "type": "Palace", "fee": 300},
            {"name": "Sajjangarh Monsoon Palace", "lat": 24.5912, "lon": 73.6367, "type": "Palace", "fee": 150},
            {"name": "Saheliyon-ki-Bari", "lat": 24.6006, "lon": 73.6881, "type": "Garden", "fee": 100}
        ]
    },
    "Agra": {
        "name": "Agra",
        "state": "Uttar Pradesh",
        "region": "North",
        "category": "Heritage & Wonders",
        "description": "Home to the iconic Taj Mahal, Agra is a major tourist destination in Uttar Pradesh and a window into the Mughal Empire's architectural legacy.",
        "best_season": "October to March",
        "latitude": 27.1767,
        "longitude": 78.0081,
        "costs": {
            "accommodation": {"Budget": 1000, "Mid-Range": 3000, "Luxury": 10000},
            "food": {"Budget": 350, "Mid-Range": 900, "Luxury": 2200},
            "transport": {"Budget": 250, "Mid-Range": 700, "Luxury": 2200},
            "activity_avg": 600
        },
        "attractions": [
            {"name": "Taj Mahal", "lat": 27.1751, "lon": 78.0421, "type": "Wonder", "fee": 1100},
            {"name": "Agra Fort", "lat": 27.1795, "lon": 78.0211, "type": "Fort", "fee": 650},
            {"name": "Itmad-ud-Daulah (Baby Taj)", "lat": 27.1929, "lon": 78.0311, "type": "Tomb", "fee": 300},
            {"name": "Mehtab Bagh", "lat": 27.1798, "lon": 78.0435, "type": "Garden", "fee": 300},
            {"name": "Fatehpur Sikri", "lat": 27.0945, "lon": 77.6677, "type": "Heritage Site", "fee": 600}
        ]
    },
    "Goa": {
        "name": "Goa",
        "state": "Goa",
        "region": "West",
        "category": "Beaches & Nightlife",
        "description": "India's pocket-sized paradise, Goa is famous for its sandy beaches, Portuguese architecture, delicious seafood, and vibrant nightlife.",
        "best_season": "November to February",
        "latitude": 15.2993,
        "longitude": 74.1240,
        "costs": {
            "accommodation": {"Budget": 1800, "Mid-Range": 5000, "Luxury": 15000},
            "food": {"Budget": 600, "Mid-Range": 1500, "Luxury": 3500},
            "transport": {"Budget": 500, "Mid-Range": 1200, "Luxury": 3000},
            "activity_avg": 800
        },
        "attractions": [
            {"name": "Baga Beach", "lat": 15.5553, "lon": 73.7517, "type": "Beach", "fee": 0},
            {"name": "Basilica of Bom Jesus", "lat": 15.5009, "lon": 73.9116, "type": "Church", "fee": 0},
            {"name": "Aguada Fort", "lat": 15.4926, "lon": 73.7739, "type": "Fort", "fee": 50},
            {"name": "Dudhsagar Falls", "lat": 15.3179, "lon": 74.3142, "type": "Waterfall", "fee": 400},
            {"name": "Anjuna Flea Market", "lat": 15.5798, "lon": 73.7431, "type": "Market", "fee": 0}
        ]
    },
    "Munnar": {
        "name": "Munnar",
        "state": "Kerala",
        "region": "South",
        "category": "Nature & Hill Stations",
        "description": "A picturesque hill station in the Western Ghats, Munnar is known for its lush tea plantations, misty valleys, and rich biodiversity.",
        "best_season": "September to May",
        "latitude": 10.0889,
        "longitude": 77.0595,
        "costs": {
            "accommodation": {"Budget": 1500, "Mid-Range": 4000, "Luxury": 12000},
            "food": {"Budget": 400, "Mid-Range": 950, "Luxury": 2000},
            "transport": {"Budget": 400, "Mid-Range": 1100, "Luxury": 2800},
            "activity_avg": 300
        },
        "attractions": [
            {"name": "Eravikulam National Park", "lat": 10.1500, "lon": 77.0667, "type": "Wildlife", "fee": 200},
            {"name": "Mattupetty Dam", "lat": 10.1060, "lon": 77.1260, "type": "Dam", "fee": 50},
            {"name": "Anamudi Peak", "lat": 10.1685, "lon": 77.0640, "type": "Mountain", "fee": 100},
            {"name": "Tea Museum", "lat": 10.0934, "lon": 77.0531, "type": "Museum", "fee": 150},
            {"name": "Echo Point", "lat": 10.1235, "lon": 77.1610, "type": "Viewpoint", "fee": 30}
        ]
    },
    "Varanasi": {
        "name": "Varanasi",
        "state": "Uttar Pradesh",
        "region": "North",
        "category": "Spiritual & Pilgrimage",
        "description": "One of the oldest continuously inhabited cities in the world, Varanasi is the spiritual heart of India, famous for its sacred Ganges river ghats.",
        "best_season": "October to March",
        "latitude": 25.3176,
        "longitude": 82.9739,
        "costs": {
            "accommodation": {"Budget": 900, "Mid-Range": 2500, "Luxury": 9000},
            "food": {"Budget": 300, "Mid-Range": 750, "Luxury": 1800},
            "transport": {"Budget": 200, "Mid-Range": 600, "Luxury": 1800},
            "activity_avg": 250
        },
        "attractions": [
            {"name": "Kashi Vishwanath Temple", "lat": 25.3109, "lon": 83.0104, "type": "Temple", "fee": 0},
            {"name": "Dashashwamedh Ghat (Ganga Aarti)", "lat": 25.3078, "lon": 83.0102, "type": "Ghat", "fee": 0},
            {"name": "Sarnath", "lat": 25.3762, "lon": 83.0227, "type": "Buddhist Site", "fee": 100},
            {"name": "Assi Ghat", "lat": 25.2899, "lon": 83.0067, "type": "Ghat", "fee": 0},
            {"name": "Banaras Hindu University (BHU)", "lat": 25.2677, "lon": 82.9913, "type": "Campus", "fee": 0}
        ]
    },
    "Manali": {
        "name": "Manali",
        "state": "Himachal Pradesh",
        "region": "North",
        "category": "Adventure & Mountains",
        "description": "Nestled in the Beas River Valley, Manali is a hub for adventure sports, snowy mountain passes, and stunning wooden temples.",
        "best_season": "October to June",
        "latitude": 32.2396,
        "longitude": 77.1887,
        "costs": {
            "accommodation": {"Budget": 1200, "Mid-Range": 3500, "Luxury": 10000},
            "food": {"Budget": 400, "Mid-Range": 1000, "Luxury": 2200},
            "transport": {"Budget": 400, "Mid-Range": 1200, "Luxury": 3000},
            "activity_avg": 700
        },
        "attractions": [
            {"name": "Solang Valley", "lat": 32.3164, "lon": 77.1601, "type": "Adventure Valley", "fee": 500},
            {"name": "Hadimba Temple", "lat": 32.2472, "lon": 77.1798, "type": "Temple", "fee": 0},
            {"name": "Rohtang Pass", "lat": 32.3716, "lon": 77.2435, "type": "Snow Pass", "fee": 1000},
            {"name": "Jogini Waterfalls", "lat": 32.2687, "lon": 77.1953, "type": "Waterfall", "fee": 0},
            {"name": "Old Manali", "lat": 32.2533, "lon": 77.1764, "type": "Culture Hub", "fee": 0}
        ]
    },
    "Kochi": {
        "name": "Kochi",
        "state": "Kerala",
        "region": "South",
        "category": "Coastal & History",
        "description": "Also known as Cochin, this ancient port city features a rich blend of Portuguese, Dutch, British, and Chinese historical influences.",
        "best_season": "October to March",
        "latitude": 9.9312,
        "longitude": 76.2673,
        "costs": {
            "accommodation": {"Budget": 1100, "Mid-Range": 3200, "Luxury": 11000},
            "food": {"Budget": 350, "Mid-Range": 900, "Luxury": 2200},
            "transport": {"Budget": 300, "Mid-Range": 800, "Luxury": 2200},
            "activity_avg": 250
        },
        "attractions": [
            {"name": "Fort Kochi & Chinese Fishing Nets", "lat": 9.9682, "lon": 76.2427, "type": "Heritage Beach", "fee": 0},
            {"name": "Mattancherry Palace (Dutch Palace)", "lat": 9.9592, "lon": 76.2592, "type": "Palace", "fee": 10},
            {"name": "Paradesi Synagogue", "lat": 9.9575, "lon": 76.2595, "type": "Temple", "fee": 10},
            {"name": "St. Francis Church", "lat": 9.9669, "lon": 76.2415, "type": "Church", "fee": 0},
            {"name": "Marine Drive", "lat": 9.9798, "lon": 76.2759, "type": "Walkway", "fee": 0}
        ]
    },
    "Srinagar": {
        "name": "Srinagar",
        "state": "Jammu & Kashmir",
        "region": "North",
        "category": "Lakes & Gardens",
        "description": "The summer capital of J&K, Srinagar is famous for its houseboats, Mughal gardens, shikara rides, and the majestic Dal Lake.",
        "best_season": "April to October",
        "latitude": 34.0837,
        "longitude": 74.7973,
        "costs": {
            "accommodation": {"Budget": 1500, "Mid-Range": 4200, "Luxury": 14000},
            "food": {"Budget": 450, "Mid-Range": 1100, "Luxury": 2500},
            "transport": {"Budget": 450, "Mid-Range": 1200, "Luxury": 3200},
            "activity_avg": 500
        },
        "attractions": [
            {"name": "Dal Lake (Shikara Ride)", "lat": 34.0934, "lon": 74.8492, "type": "Lake", "fee": 500},
            {"name": "Shalimar Bagh Mughal Garden", "lat": 34.1481, "lon": 74.8727, "type": "Garden", "fee": 50},
            {"name": "Nishat Bagh", "lat": 34.1245, "lon": 74.8791, "type": "Garden", "fee": 50},
            {"name": "Indira Gandhi Memorial Tulip Garden", "lat": 34.0908, "lon": 74.8690, "type": "Garden", "fee": 100},
            {"name": "Shankaracharya Temple", "lat": 34.0792, "lon": 74.8427, "type": "Temple", "fee": 0}
        ]
    },
    "Darjeeling": {
        "name": "Darjeeling",
        "state": "West Bengal",
        "region": "East",
        "category": "Nature & Hill Stations",
        "description": "Famed for its black tea plantations and panoramic views of Kanchenjunga, the world's third-highest peak.",
        "best_season": "October to May",
        "latitude": 27.0410,
        "longitude": 88.2627,
        "costs": {
            "accommodation": {"Budget": 1400, "Mid-Range": 3800, "Luxury": 11000},
            "food": {"Budget": 350, "Mid-Range": 900, "Luxury": 2000},
            "transport": {"Budget": 400, "Mid-Range": 1000, "Luxury": 2500},
            "activity_avg": 400
        },
        "attractions": [
            {"name": "Tiger Hill (Sunrise Point)", "lat": 26.9961, "lon": 88.2464, "type": "Viewpoint", "fee": 80},
            {"name": "Batasia Loop & War Memorial", "lat": 27.0168, "lon": 88.2529, "type": "Memorial", "fee": 20},
            {"name": "Padmaja Naidu Himalayan Zoological Park", "lat": 27.0588, "lon": 88.2539, "type": "Zoo", "fee": 100},
            {"name": "Happy Valley Tea Estate", "lat": 27.0537, "lon": 88.2635, "type": "Tea Garden", "fee": 100},
            {"name": "Ghum Monastery", "lat": 27.0099, "lon": 88.2476, "type": "Monastery", "fee": 0}
        ]
    },
    "Bengaluru": {
        "name": "Bengaluru",
        "state": "Karnataka",
        "region": "South",
        "category": "City & Tech",
        "description": "Known as the 'Silicon Valley of India' and the 'Garden City', Bengaluru features pleasant weather, beautiful parks, and a buzzing cafe culture.",
        "best_season": "Throughout the year",
        "latitude": 12.9716,
        "longitude": 77.5946,
        "costs": {
            "accommodation": {"Budget": 1300, "Mid-Range": 4000, "Luxury": 12000},
            "food": {"Budget": 450, "Mid-Range": 1200, "Luxury": 3000},
            "transport": {"Budget": 300, "Mid-Range": 900, "Luxury": 2600},
            "activity_avg": 300
        },
        "attractions": [
            {"name": "Lalbagh Botanical Garden", "lat": 12.9507, "lon": 77.5844, "type": "Garden", "fee": 30},
            {"name": "Bangalore Palace", "lat": 12.9988, "lon": 77.5921, "type": "Palace", "fee": 480},
            {"name": "Cubbon Park", "lat": 12.9779, "lon": 77.5952, "type": "Park", "fee": 0},
            {"name": "Visvesvaraya Industrial & Technological Museum", "lat": 12.9751, "lon": 77.5962, "type": "Museum", "fee": 85},
            {"name": "Nandi Hills", "lat": 13.3702, "lon": 77.6835, "type": "Hill Station", "fee": 50}
        ]
    },
    "Mumbai": {
        "name": "Mumbai",
        "state": "Maharashtra",
        "region": "West",
        "category": "Cosmopolitan & Heritage",
        "description": "The city that never sleeps, Mumbai is India's financial capital and the hub of the Bollywood film industry, located right on the Arabian Sea.",
        "best_season": "October to March",
        "latitude": 19.0760,
        "longitude": 72.8777,
        "costs": {
            "accommodation": {"Budget": 1800, "Mid-Range": 5500, "Luxury": 18000},
            "food": {"Budget": 500, "Mid-Range": 1400, "Luxury": 3500},
            "transport": {"Budget": 300, "Mid-Range": 1100, "Luxury": 3000},
            "activity_avg": 400
        },
        "attractions": [
            {"name": "Gateway of India", "lat": 18.9220, "lon": 72.8347, "type": "Monument", "fee": 0},
            {"name": "Marine Drive", "lat": 18.9433, "lon": 72.8230, "type": "Promenade", "fee": 0},
            {"name": "Elephanta Caves", "lat": 18.9633, "lon": 72.9315, "type": "Heritage Caves", "fee": 300},
            {"name": "Chhatrapati Shivaji Maharaj Terminus", "lat": 18.9400, "lon": 72.8354, "type": "Railway Station / Heritage", "fee": 0},
            {"name": "Siddhivinayak Temple", "lat": 19.0169, "lon": 72.8302, "type": "Temple", "fee": 0}
        ]
    },
    "Hampi": {
        "name": "Hampi",
        "state": "Karnataka",
        "region": "South",
        "category": "Archaeological & Ruins",
        "description": "A UNESCO World Heritage site, Hampi contains the awe-inspiring ruins of the medieval Vijayanagara Empire amidst giant boulder-strewn landscapes.",
        "best_season": "October to March",
        "latitude": 15.3350,
        "longitude": 76.4600,
        "costs": {
            "accommodation": {"Budget": 1000, "Mid-Range": 3000, "Luxury": 10000},
            "food": {"Budget": 350, "Mid-Range": 850, "Luxury": 2000},
            "transport": {"Budget": 300, "Mid-Range": 800, "Luxury": 2200},
            "activity_avg": 200
        },
        "attractions": [
            {"name": "Virupaksha Temple", "lat": 15.3353, "lon": 76.4591, "type": "Temple", "fee": 50},
            {"name": "Vittala Temple (Stone Chariot)", "lat": 15.3427, "lon": 76.4770, "type": "Temple Ruins", "fee": 40},
            {"name": "Hampi Boulders / Matanga Hill", "lat": 15.3325, "lon": 76.4660, "type": "Viewpoint", "fee": 0},
            {"name": "Lotus Mahal", "lat": 15.3312, "lon": 76.4691, "type": "Palace Ruins", "fee": 40},
            {"name": "Royal Enclosure", "lat": 15.3289, "lon": 76.4677, "type": "Ruins", "fee": 0}
        ]
    },
    "Amritsar": {
        "name": "Amritsar",
        "state": "Punjab",
        "region": "North",
        "category": "Spiritual & Food",
        "description": "Amritsar is the spiritual and cultural center of the Sikh religion, famous for the magnificent Golden Temple and warm Punjabi hospitality.",
        "best_season": "October to March",
        "latitude": 31.6340,
        "longitude": 74.8723,
        "costs": {
            "accommodation": {"Budget": 1000, "Mid-Range": 3000, "Luxury": 9000},
            "food": {"Budget": 300, "Mid-Range": 800, "Luxury": 2000},
            "transport": {"Budget": 250, "Mid-Range": 700, "Luxury": 2000},
            "activity_avg": 200
        },
        "attractions": [
            {"name": "Harmandir Sahib (Golden Temple)", "lat": 31.6199, "lon": 74.8765, "type": "Temple", "fee": 0},
            {"name": "Jallianwala Bagh", "lat": 31.6212, "lon": 74.8801, "type": "Memorial", "fee": 0},
            {"name": "Wagah Border (Beating Retreat)", "lat": 31.6067, "lon": 74.5700, "type": "Border Post", "fee": 0},
            {"name": "Partition Museum", "lat": 31.6267, "lon": 74.8785, "type": "Museum", "fee": 10},
            {"name": "Gobindgarh Fort", "lat": 31.6310, "lon": 74.8587, "type": "Fort", "fee": 150}
        ]
    },
    "Darjeeling & Gangtok": {
        "name": "Darjeeling & Gangtok",
        "state": "Sikkim & WB",
        "region": "East",
        "category": "Nature & Monasteries",
        "description": "A popular combined tour of the beautiful Himalayan hill stations, featuring dramatic mountain views, monasteries, and pristine alpine lakes.",
        "best_season": "March to May, October to December",
        "latitude": 27.3314,
        "longitude": 88.6138,
        "costs": {
            "accommodation": {"Budget": 1500, "Mid-Range": 4500, "Luxury": 13000},
            "food": {"Budget": 400, "Mid-Range": 1000, "Luxury": 2400},
            "transport": {"Budget": 500, "Mid-Range": 1400, "Luxury": 3500},
            "activity_avg": 500
        },
        "attractions": [
            {"name": "Tsomgo Lake", "lat": 27.3752, "lon": 88.7621, "type": "Alpine Lake", "fee": 200},
            {"name": "Rumtek Monastery", "lat": 27.2798, "lon": 88.6015, "type": "Monastery", "fee": 10},
            {"name": "Tiger Hill Darjeeling", "lat": 26.9961, "lon": 88.2464, "type": "Viewpoint", "fee": 80},
            {"name": "Nathu La Pass", "lat": 27.3877, "lon": 88.8306, "type": "Border Pass", "fee": 1000},
            {"name": "Ban Jhakri Falls", "lat": 27.3482, "lon": 88.6189, "type": "Waterfall", "fee": 50}
        ]
    },
    "Pondicherry": {
        "name": "Pondicherry",
        "state": "Puducherry",
        "region": "South",
        "category": "Coastal & French Heritage",
        "description": "Known as 'The French Riviera of the East', Pondicherry offers a unique blend of French colonial architecture, spiritual communities, and beaches.",
        "best_season": "October to March",
        "latitude": 11.9416,
        "longitude": 79.8083,
        "costs": {
            "accommodation": {"Budget": 1200, "Mid-Range": 3800, "Luxury": 12000},
            "food": {"Budget": 450, "Mid-Range": 1200, "Luxury": 2800},
            "transport": {"Budget": 300, "Mid-Range": 800, "Luxury": 2200},
            "activity_avg": 200
        },
        "attractions": [
            {"name": "Auroville Matrimandir", "lat": 12.0069, "lon": 79.8105, "type": "Spiritual Center", "fee": 0},
            {"name": "Sri Aurobindo Ashram", "lat": 11.9443, "lon": 79.8344, "type": "Ashram", "fee": 0},
            {"name": "Promenade Beach (Rock Beach)", "lat": 11.9338, "lon": 79.8358, "type": "Beach", "fee": 0},
            {"name": "French Quarter (White Town)", "lat": 11.9360, "lon": 79.8327, "type": "Heritage Architecture", "fee": 0},
            {"name": "Paradise Beach", "lat": 11.8906, "lon": 79.8144, "type": "Beach", "fee": 200}
        ]
    }
}

# --- Dynamic CSV Loading and Merging ---
def _load_csv_destinations():
    import os
    import pandas as pd
    import json
    import hashlib

    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "Top_Indian_Places_to_Visit.csv")
    coords_path = os.path.join(base_dir, "city_coordinates.json")

    if not os.path.exists(csv_path):
        return

    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"Error loading CSV in dataset.py: {e}")
        return

    # Clean whitespace in columns
    df.columns = [c.strip() for c in df.columns]
    for col in ['City', 'State', 'Zone', 'Name', 'Type', 'Best Time to visit', 'Significance']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    # Load coordinates
    coordinates = {}
    if os.path.exists(coords_path):
        try:
            with open(coords_path, 'r') as f:
                coordinates = json.load(f)
        except Exception:
            pass

    zone_map = {
        "Northern": "North",
        "Western": "West",
        "Southern": "South",
        "Eastern": "East",
        "Central": "Central",
        "North Eastern": "North East"
    }

    def get_attraction_coordinates(city_lat, city_lon, name):
        h = hashlib.md5(name.encode('utf-8')).hexdigest()
        lat_offset = (int(h[:4], 16) / 65535.0 - 0.5) * 0.03
        lon_offset = (int(h[4:8], 16) / 65535.0 - 0.5) * 0.03
        return city_lat + lat_offset, city_lon + lon_offset

    # Group CSV rows by City
    grouped = df.groupby('City')

    for city_name, group in grouped:
        city_name = str(city_name).strip()
        
        # Determine coordinates
        # If city is already in DESTINATIONS, we keep its center coordinates
        if city_name in DESTINATIONS:
            lat = DESTINATIONS[city_name]["latitude"]
            lon = DESTINATIONS[city_name]["longitude"]
        else:
            city_coords = coordinates.get(city_name)
            if city_coords:
                lat = city_coords['latitude']
                lon = city_coords['longitude']
            else:
                # Default coordinates (India center)
                lat, lon = 20.5937, 78.9629

        # Build list of attractions from CSV
        attractions = []
        for _, row in group.iterrows():
            name = str(row['Name']).strip()
            
            # Use original attraction coordinates if matching one exists in DESTINATIONS
            orig_att = None
            if city_name in DESTINATIONS:
                for att in DESTINATIONS[city_name].get("attractions", []):
                    if att["name"].lower() == name.lower():
                        orig_att = att
                        break
            
            if orig_att:
                att_lat = orig_att["lat"]
                att_lon = orig_att["lon"]
            else:
                att_lat, att_lon = get_attraction_coordinates(lat, lon, name)

            fee = 0
            try:
                fee = int(pd.to_numeric(row['Entrance Fee in INR'], errors='coerce') or 0)
            except Exception:
                pass
                
            attractions.append({
                "name": name,
                "lat": att_lat,
                "lon": att_lon,
                "type": str(row['Type']).strip(),
                "fee": fee
            })

        # Calculate average activity cost from CSV
        avg_fee = 300
        try:
            fees = pd.to_numeric(group['Entrance Fee in INR'], errors='coerce').dropna()
            if not fees.empty:
                avg_fee = int(fees.mean())
            if avg_fee < 200:
                avg_fee = 200
        except Exception:
            pass

        first_row = group.iloc[0]
        state = str(first_row.get('State', 'India')).strip()
        zone = str(first_row.get('Zone', '')).strip()
        region = zone_map.get(zone, zone)

        # Category from Type or Significance
        category = str(first_row.get('Type', 'Sightseeing')).strip()
        
        # Best season
        seasons = group['Best Time to visit'].dropna().tolist()
        best_season = seasons[0] if seasons else "October to March"
        if best_season.lower() in ["evening", "afternoon", "morning", "all", "anytime"]:
            best_season = "October to March"  # Replace day times with seasonal default

        landmarks = group['Name'].head(3).tolist()
        description = f"Explore {city_name} in {state}. Highlights include {', '.join(landmarks)}."

        # Setup costs (preserve original costs if city is hardcoded)
        if city_name in DESTINATIONS:
            costs = DESTINATIONS[city_name]["costs"]
            description = DESTINATIONS[city_name].get("description", description)
            best_season = DESTINATIONS[city_name].get("best_season", best_season)
            category = DESTINATIONS[city_name].get("category", category)
            state = DESTINATIONS[city_name].get("state", state)
            region = DESTINATIONS[city_name].get("region", region)
        else:
            # Dynamically calculate popularity multiplier from google reviews & expensive states
            try:
                total_reviews = pd.to_numeric(group['Number of google review in lakhs'], errors='coerce').dropna().sum()
            except Exception:
                total_reviews = 0.0
            
            # Multiplier starts at 0.8 and increases up to 1.4 based on reviews (e.g. 10+ lakhs reviews)
            multiplier = 0.8 + min(total_reviews / 10.0, 0.6)
            
            expensive_states = ['goa', 'maharashtra', 'karnataka', 'delhi', 'kerala']
            if state.lower() in expensive_states:
                multiplier += 0.20
            
            multiplier = max(0.75, min(multiplier, 1.6))
            
            costs = {
                "accommodation": {
                    "Budget": int(1200 * multiplier), 
                    "Mid-Range": int(3500 * multiplier), 
                    "Luxury": int(12000 * multiplier)
                },
                "food": {
                    "Budget": int(400 * multiplier), 
                    "Mid-Range": int(1000 * multiplier), 
                    "Luxury": int(2500 * multiplier)
                },
                "transport": {
                    "Budget": int(300 * multiplier), 
                    "Mid-Range": int(800 * multiplier), 
                    "Luxury": int(2200 * multiplier)
                },
                "activity_avg": avg_fee
            }

        # Update or add the destination profile
        DESTINATIONS[city_name] = {
            "name": city_name,
            "state": state,
            "region": region,
            "category": category,
            "description": description,
            "best_season": best_season,
            "latitude": lat,
            "longitude": lon,
            "costs": costs,
            "attractions": attractions
        }

_load_csv_destinations()
