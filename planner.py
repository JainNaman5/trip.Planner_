# planner.py
"""
AI Itinerary planner module.
Handles queries to Google Gemini API and generates structured travel plans,
with a robust fallback generator for offline / key-less runs.
"""
import google.generativeai as genai
import random

def get_fallback_itinerary(destination_data, days, budget, group_type):
    """
    Generates a high-quality, structured rule-based itinerary
    when no Gemini API key is available.
    """
    attractions = destination_data["attractions"]
    num_attractions = len(attractions)
    
    markdown = f"### 📅 Custom {days}-Day Itinerary for {destination_data['name']} ({group_type} - {budget} Tier)\n\n"
    markdown += "*Note: Showing a pre-planned schedule (No Gemini API Key provided. Enter a key in the sidebar for full AI personalization).* \n\n"
    
    # Tips block
    markdown += "> **💡 Local Tips for your Trip:**\n"
    markdown += f"> - **Best Time:** The ideal time to visit is during **{destination_data['best_season']}**.\n"
    markdown += f"> - **Vibe:** This is a **{destination_data['category']}** style destination.\n"
    markdown += "> - **Travel Strategy:** Start your days early around 8:30 AM to beat the crowd and midday heat.\n\n"
    
    # Generate schedule per day
    for day in range(1, days + 1):
        markdown += f"#### 🌅 Day {day}: Exploring {destination_data['name']}\n"
        
        # Select attractions for this day
        # We will loop or distribute attractions based on day index
        att_idx_1 = ((day - 1) * 2) % num_attractions
        att_idx_2 = ((day - 1) * 2 + 1) % num_attractions
        
        a1 = attractions[att_idx_1]
        a2 = attractions[att_idx_2]
        
        # Day themes
        themes = ["Heritage and Landmarks", "Local Sightseeing and Walks", "Culture and Scenic Exploration", "Offbeat & Leisure Time"]
        theme = themes[(day - 1) % len(themes)]
        markdown += f"**Theme:** *{theme}*\n\n"
        
        # Morning Activity
        markdown += f"- **09:00 AM - Morning Visit: {a1['name']} ({a1['type']})**\n"
        markdown += f"  - Head out early to visit **{a1['name']}**. Expect about 2 hours here. "
        if a1['fee'] > 0:
            markdown += f"Note: Entry fee is approx. ₹{a1['fee']} per person.\n"
        else:
            markdown += "Note: Free entry.\n"
        markdown += "  - *Tip:* Wear comfortable walking shoes.\n\n"
        
        # Lunch Activity
        markdown += "- **01:00 PM - Lunch Break**\n"
        if budget == "Budget":
            markdown += "  - Dine at a popular local street food spot or local dhaba. Try regional dishes like local thali or street specialties for ₹150-₹250 per person.\n\n"
        elif budget == "Mid-Range":
            markdown += "  - Eat at a highly-rated family restaurant or cafe. Enjoy authentic local cuisine in a cozy atmosphere for ₹400-₹600 per person.\n\n"
        else: # Luxury
            markdown += "  - Book a table at a premium fine dining heritage restaurant. Enjoy luxury dining and curated multi-course specialties for ₹1500+ per person.\n\n"
            
        # Afternoon Activity
        markdown += f"- **03:00 PM - Afternoon Sightseeing: {a2['name']} ({a2['type']})**\n"
        markdown += f"  - Make your way to **{a2['name']}**. Perfect spot to learn about local history or capture stunning scenic photos. "
        if a2['fee'] > 0:
            markdown += f"Entry fee is ₹{a2['fee']}.\n"
        else:
            markdown += "Entry is free.\n"
        markdown += "  - *Tip:* Great lighting for photography during late afternoon.\n\n"
        
        # Evening activity
        markdown += "- **06:00 PM - Evening Walk & Shopping**\n"
        markdown += f"  - Take a stroll around the local market squares of {destination_data['name']}. Shop for handicrafts, souvenirs, and try some local evening snacks.\n"
        markdown += "  - *Activity:* Enjoy the sunset view from a nearby lakefront, park, or viewpoint.\n\n"
        
        # Dinner activity
        markdown += "- **08:30 PM - Dinner**\n"
        markdown += "  - Relax and unwind at a local eatery, wrapping up the day with delicious local desserts (like Kulfi, Jalebi, or Payasam depending on the region).\n\n"
        markdown += "---\n\n"
        
    return markdown

def generate_ai_itinerary(destination_data, days, budget, group_type, api_key=None):
    """
    Attempts to generate a highly detailed, personalized travel plan
    using Google Gemini API, falling back to local generation if unsuccessful or if no key.
    """
    if not api_key:
        return get_fallback_itinerary(destination_data, days, budget, group_type)
        
    try:
        genai.configure(api_key=api_key)
        
        # Construct the system and user prompt
        attractions_str = ", ".join([f"{a['name']} ({a['type']})" for a in destination_data["attractions"]])
        
        prompt = f"""
You are an expert AI Travel Planner specializing in Indian tourism. 
Create a highly detailed, engaging, and premium day-by-day travel itinerary for a trip to {destination_data['name']}, {destination_data['state']}, India.

Trip Details:
- Destination: {destination_data['name']} (Category: {destination_data['category']})
- Duration: {days} days
- Budget Category: {budget}
- Traveler Profile: {group_type}
- Major Attractions to include (but not limited to): {attractions_str}

Please generate the itinerary in clean Markdown format with the following guidelines:
1. Start with a summary of the trip style, including "Best Season" (which is {destination_data['best_season']}), and a 3-4 sentence overview of what makes this destination unique for {group_type} travelers on a {budget} budget.
2. For EACH day (Day 1 to Day {days}), outline:
   - A theme or mood for the day.
   - Specific morning, afternoon, and evening slots with times (e.g., 09:00 AM - 12:00 PM).
   - Food recommendations for lunch and dinner matching the '{budget}' tier (suggest specific famous local dishes or food streets).
   - Practical travel tips for that day (e.g., transport tips, clothing advice, photography warnings).
3. Include a concluding section: "Local Etiquette & Travel Advice" with 3-4 bullet points tailored to {destination_data['name']}.

Ensure the tone is warm, inviting, and highly informative. Keep the text engaging and format with clean emojis and bold labels.
Do not mention metadata like "System Prompt" or "Here is your itinerary". Start directly with the itinerary content.
"""
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        
        if response and response.text:
            return response.text
        else:
            return get_fallback_itinerary(destination_data, days, budget, group_type) + "\n\n*(Note: Gemini API returned an empty response; fell back to standard itinerary).* "
            
    except Exception as e:
        return get_fallback_itinerary(destination_data, days, budget, group_type) + f"\n\n*(Note: Gemini API Error: {str(e)}. Fell back to standard itinerary).* "
