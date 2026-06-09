# app.py
"""
Trip Planner - Main Streamlit Application
Interactive Python-only travel application featuring curated Indian datasets,
AI itinerary planning via Google Gemini, dynamic folium mapping, and plotly cost visualizations.
"""
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Import local modules
from dataset import DESTINATIONS
from planner import generate_ai_itinerary
from cost_estimator import calculate_costs, get_pie_chart, get_comparison_chart

# Page Setup
st.set_page_config(
    page_title="Trip Planner - Incredible India",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- SIDEBAR -----------------
st.sidebar.markdown("# ✈️ Trip Settings")
theme_mode = st.sidebar.toggle("🌙 Dark Mode", value=True, help="Toggle between premium Light and Dark mode aesthetics.")

# CSS Variables based on Theme selection
if theme_mode: # Dark Mode
    body_bg = "#0f172a"
    card_bg = "linear-gradient(135deg, #1e293b, #0f172a)"
    card_text = "#ffffff"
    card_desc = "#e2e8f0"
    card_sub = "#cbd5e1"
    kpi_bg = "#1e293b"
    kpi_text = "#ffffff"
    kpi_sub = "#94a3b8"
    kpi_border = "#334155"
    table_th_bg = "#1e293b"
    table_th_text = "#ffffff"
    body_text_color = "#f8fafc"
    sidebar_bg = "#0f172a"
    sidebar_text = "#ffffff"
else: # Light Mode
    body_bg = "#ffffff"
    card_bg = "linear-gradient(135deg, #fffaf4, #fff3e3)"
    card_text = "#1f2937"
    card_desc = "#4b5563"
    card_sub = "#4b5563"
    kpi_bg = "#ffffff"
    kpi_text = "#111827"
    kpi_sub = "#6b7280"
    kpi_border = "#e5e7eb"
    table_th_bg = "#f3f4f6"
    table_th_text = "#111827"
    body_text_color = "#1f2937"
    sidebar_bg = "#f8fafc"
    sidebar_text = "#1f2937"

# Custom Styling / CSS for Premium Indian Heritage Aesthetics
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
        
        /* Main background */
        .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stMainViewContainer"] {{
            background-color: {body_bg} !important;
            color: {body_text_color} !important;
        }}
        
        /* Apply fonts globally */
        html, body, [class*="css"], .stMarkdown {{
            font-family: 'Outfit', sans-serif;
            color: {body_text_color};
        }}
        
        /* Text color overrides */
        .stMarkdown p, h2, h3, h4, h5, h6, label, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {{
            color: {body_text_color} !important;
        }}
        
        /* Target H1 headers except the main title */
        h1:not(.header-title) {{
            color: {body_text_color} !important;
        }}
        
        /* Custom Header styling */
        .header-title {{
            font-size: 2.8rem !important;
            font-weight: 700 !important;
            background: linear-gradient(90deg, #FF9933, #138808) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            color: transparent !important;
            margin-bottom: 0px;
            padding-bottom: 0px;
            display: inline-block;
        }}
        
        .header-subtitle {{
            font-size: 1.1rem;
            color: {kpi_sub} !important;
            margin-top: 5px;
            margin-bottom: 25px;
        }}
        
        /* Premium Destination Card */
        .dest-card {{
            background: {card_bg};
            color: {card_text} !important;
            border-radius: 16px;
            padding: 28px;
            margin-bottom: 30px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.15);
            border-left: 6px solid #FF9933;
        }}
        
        .dest-card .dest-title {{
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 5px;
            color: {card_text} !important;
        }}
        
        .dest-card .dest-state {{
            font-size: 1rem;
            color: {card_sub} !important;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-weight: 600;
            margin-bottom: 15px;
        }}
        
        .dest-card .dest-desc {{
            font-size: 1.05rem;
            line-height: 1.6;
            color: {card_desc} !important;
            margin-bottom: 20px;
        }}
        
        .badge-container {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}
        
        .badge {{
            background-color: rgba(255, 153, 51, 0.15);
            color: #ff9933 !important;
            border: 1px solid rgba(255, 153, 51, 0.3);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }}
        
        .badge-green {{
            background-color: rgba(19, 136, 8, 0.15);
            color: #138808 !important;
            border: 1px solid rgba(19, 136, 8, 0.3);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }}
        
        /* KPI Cost Cards */
        .kpi-box {{
            background-color: {kpi_bg};
            color: {kpi_text} !important;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border: 1px solid {kpi_border};
            border-top: 4px solid #138808;
            text-align: center;
            transition: all 0.3s ease;
        }}
        
        .kpi-box:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        }}
        
        .kpi-box .kpi-label {{
            font-size: 0.85rem;
            color: {kpi_sub} !important;
            text-transform: uppercase;
            font-weight: 700;
            margin-bottom: 8px;
            letter-spacing: 0.5px;
        }}
        
        .kpi-box .kpi-value {{
            font-size: 1.8rem;
            font-weight: 700;
            color: {kpi_text} !important;
        }}
        
        .kpi-box .kpi-sub {{
            font-size: 0.8rem;
            color: {kpi_sub} !important;
            margin-top: 5px;
        }}
        
        /* Table overrides (st.table and standard HTML tables) */
        table, th, td, tr, thead, tbody, div[data-testid="stTable"] {{
            color: {body_text_color} !important;
            background-color: {body_bg} !important;
        }}
        
        div[data-testid="stTable"] table {{
            border-color: {kpi_border} !important;
        }}
        
        /* Sidebar Styling */
        [data-testid="stSidebar"], [data-testid="stSidebarUserContent"], div[data-testid="stSidebar"] {{
            background-color: {sidebar_bg} !important;
            border-right: 1px solid {kpi_border} !important;
            color: {sidebar_text} !important;
        }}
        
        [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label, [data-testid="stSidebar"] [data-testid="stWidgetLabel"], [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {{
            color: {sidebar_text} !important;
        }}
        
        /* Sidebar Inputs & Selectbox style overrides */
        [data-testid="stSidebar"] div[data-baseweb="select"] > div, 
        [data-testid="stSidebar"] div[data-baseweb="input"] > div,
        [data-testid="stSidebar"] input,
        [data-testid="stSidebar"] select,
        [data-testid="stSidebar"] div[role="listbox"] {{
            background-color: {kpi_bg} !important;
            color: {sidebar_text} !important;
            border-color: {kpi_border} !important;
        }}
        
        [data-testid="stSidebar"] div[data-testid="stSelectbox"] div[data-baseweb="select"] span,
        [data-testid="stSidebar"] div[data-testid="stSelectbox"] div[data-baseweb="select"] div {{
            color: {sidebar_text} !important;
        }}
        
        [data-testid="stSidebar"] button[aria-label="Step down"],
        [data-testid="stSidebar"] button[aria-label="Step up"] {{
            background-color: {kpi_bg} !important;
            color: {sidebar_text} !important;
            border-color: {kpi_border} !important;
        }}
        
        [data-testid="stSidebar"] div[data-testid="stSlider"] p, 
        [data-testid="stSidebar"] div[data-testid="stSlider"] span,
        [data-testid="stSidebar"] div[data-testid="stSlider"] div {{
            color: {sidebar_text} !important;
        }}
        
        [data-testid="stSidebar"] div[data-testid="stExpander"] details summary p,
        [data-testid="stSidebar"] div[data-testid="stExpander"] details summary span,
        [data-testid="stSidebar"] div[data-testid="stExpander"] details summary {{
            color: {sidebar_text} !important;
            background-color: {sidebar_bg} !important;
        }}
        
        /* Tabs styling */
        button[data-baseweb="tab"] p {{
            color: {body_text_color} !important;
        }}
        
        button[data-baseweb="tab"][aria-selected="true"] {{
            border-bottom-color: #FF9933 !important;
        }}
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("Configure your Indian getaway parameters below.")

# Destination Selector
dest_options = sorted(list(DESTINATIONS.keys()))
selected_city = st.sidebar.selectbox(
    "Choose Destination City",
    options=dest_options,
    index=0,
    help="Select an Indian city to plan your trip."
)
dest = DESTINATIONS[selected_city]

# Duration Selector
trip_days = st.sidebar.slider(
    "Trip Duration (Days)",
    min_value=1,
    max_value=14,
    value=3,
    step=1,
    help="Number of days you want to plan for."
)

# Budget / Style Selector
budget_tier = st.sidebar.selectbox(
    "Travel Style / Budget",
    options=["Budget", "Mid-Range", "Luxury"],
    index=1,
    help="Budget tier controls accommodations, dining, and transit options."
)

# Number of Travelers
traveler_count = st.sidebar.number_input(
    "Number of Travelers",
    min_value=1,
    max_value=20,
    value=2,
    step=1,
    help="Calculates hotel rooms (assume double sharing) and transit ticket multipliers."
)

# Group Type
group_type = st.sidebar.selectbox(
    "Group Profile",
    options=["Solo", "Couple", "Family", "Friends"],
    index=1,
    help="Helps the AI customize suggested activities."
)

# API Key Configurator (Gemini API)
st.sidebar.markdown("---")
with st.sidebar.expander("🔑 Gemini AI Key (Optional)", expanded=False):
    api_key = st.text_input(
        "Google Gemini API Key",
        type="password",
        help="Get a free key from Google AI Studio. If empty, the app uses a rich pre-programmed fallback itinerary."
    )
    st.markdown(
        "[Get a free API Key](https://aistudio.google.com/)",
        unsafe_allow_html=True
    )

# ----------------- MAIN APP CONTENT -----------------

# Page Header
st.markdown('<h1 class="header-title">🇮🇳 Incredible India Trip Planner</h1>', unsafe_allow_html=True)
st.markdown('<p class="header-subtitle">Plan schedules, map landmarks, and estimate budgets in a heartbeat.</p>', unsafe_allow_html=True)

# Destination Profile Hero Block
st.markdown(f"""
    <div class="dest-card">
        <div class="dest-state">{dest['state']} • {dest['region']} India</div>
        <div class="dest-title">Explore {dest['name']}</div>
        <div class="dest-desc">{dest['description']}</div>
        <div class="badge-container">
            <span class="badge">🌤️ Best Season: {dest['best_season']}</span>
            <span class="badge-green">🏷️ Category: {dest['category']}</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Layout: Tabs
tab_explore, tab_itinerary, tab_cost = st.tabs([
    "🗺️ Explore & Interactive Map",
    "🗓️ AI Travel Itinerary",
    "💰 Estimated Costs & Charts"
])

# ----------------- TAB 1: EXPLORE & MAP -----------------
with tab_explore:
    st.subheader(f"Sightseeing & Landmarks in {dest['name']}")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"#### Top Attractions to Visit")
        st.markdown("Here are some of the primary sites of interest mapped in this city. Feel free to request these in your AI prompt!")
        
        # Create an interactive attractions list
        attractions_df = pd.DataFrame(dest["attractions"])
        # Format the entry fee nicely
        attractions_df["entry_fee_display"] = attractions_df["fee"].apply(lambda x: f"₹{x}" if x > 0 else "Free")
        
        # Clean dataframe for display
        display_df = attractions_df[["name", "type", "entry_fee_display"]].rename(
            columns={"name": "Attraction Name", "type": "Type", "entry_fee_display": "Entry Fee (INR)"}
        )
        st.table(display_df)
        
    with col2:
        st.markdown("#### Interactive Landmarks Map")
        st.caption("Click on pins to view attraction details and entry fees.")
        
        # Draw Folium Map
        m = folium.Map(
            location=[dest["latitude"], dest["longitude"]],
            zoom_start=12 if dest["name"] != "Darjeeling & Gangtok" else 10,
            control_scale=True
        )
        
        # Add city center marker
        folium.Marker(
            [dest["latitude"], dest["longitude"]],
            popup=f"<b>{dest['name']}</b> Center",
            tooltip=f"{dest['name']} Center",
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)
        
        # Add attraction markers
        for att in dest["attractions"]:
            color = "blue"
            if "Fort" in att["type"] or "Palace" in att["type"]:
                color = "orange"
            elif "Beach" in att["type"] or "Lake" in att["type"] or "Waterfall" in att["type"]:
                color = "cadetblue"
            elif "Temple" in att["type"] or "Spiritual" in att["type"] or "Church" in att["type"]:
                color = "purple"
            elif "Garden" in att["type"] or "Park" in att["type"]:
                color = "green"
            
            folium.Marker(
                [att["lat"], att["lon"]],
                popup=f"<b>{att['name']}</b><br>Type: {att['type']}<br>Entry: ₹{att['fee']}",
                tooltip=att["name"],
                icon=folium.Icon(color=color, icon="star")
            ).add_to(m)
            
        # Display the map using streamlit_folium
        st_folium(m, width=700, height=450, returned_objects=[])

# ----------------- TAB 2: AI ITINERARY -----------------
with tab_itinerary:
    st.subheader("🤖 AI-Generated Day-by-Day Travel Plan")
    
    # Check if we should call Gemini or Fallback
    if not api_key:
        st.info("ℹ️ Using standard rule-based itinerary. Enter a **Google Gemini API Key** in the sidebar for a fully customized, AI-personalized itinerary!")
    else:
        st.success("🤖 Google Gemini API Key loaded. Generating bespoke travel itinerary...")

    # Display itinerary
    with st.spinner("Compiling travel logistics and mapping sightseeing schedules..."):
        itinerary_md = generate_ai_itinerary(dest, trip_days, budget_tier, group_type, api_key)
        
    st.markdown(itinerary_md)
    
    # Add Download button
    st.download_button(
        label="📥 Download Itinerary as File",
        data=itinerary_md,
        file_name=f"Itinerary_{dest['name']}_{trip_days}days.md",
        mime="text/markdown"
    )

# ----------------- TAB 3: COST ESTIMATOR -----------------
with tab_cost:
    st.subheader("💰 Tour Expense Estimation")
    
    # Calculate costs
    cost_res = calculate_costs(dest, trip_days, traveler_count, budget_tier)
    
    # Render KPI Cards in columns
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    
    with kpi1:
        st.markdown(f"""
            <div class="kpi-box">
                <div class="kpi-label">Estimated Total</div>
                <div class="kpi-value" style="color: #138808;">₹{cost_res['Total']:,}</div>
                <div class="kpi-sub">Total trip budget (INR)</div>
            </div>
        """, unsafe_allow_html=True)
        
    with kpi2:
        per_person = int(cost_res['Total'] / traveler_count)
        st.markdown(f"""
            <div class="kpi-box">
                <div class="kpi-label">Per Person Cost</div>
                <div class="kpi-value">₹{per_person:,}</div>
                <div class="kpi-sub">For {traveler_count} traveler(s)</div>
            </div>
        """, unsafe_allow_html=True)
        
    with kpi3:
        rooms_needed = cost_res["details"]["rooms"]
        st.markdown(f"""
            <div class="kpi-box">
                <div class="kpi-label">Accommodation</div>
                <div class="kpi-value">₹{cost_res['Accommodation']:,}</div>
                <div class="kpi-sub">{rooms_needed} room(s) for {trip_days} night(s)</div>
            </div>
        """, unsafe_allow_html=True)
        
    with kpi4:
        st.markdown(f"""
            <div class="kpi-box">
                <div class="kpi-label">Travel Style Class</div>
                <div class="kpi-value" style="color: #ff9933;">{budget_tier}</div>
                <div class="kpi-sub">{group_type} Group Type</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Visualizations
    col_v1, col_v2 = st.columns([1, 1])
    
    with col_v1:
        pie_fig = get_pie_chart(cost_res, theme="dark" if theme_mode else "light")
        st.plotly_chart(pie_fig, use_container_width=True)
        
    with col_v2:
        comp_fig = get_comparison_chart(dest, trip_days, traveler_count, theme="dark" if theme_mode else "light")
        st.plotly_chart(comp_fig, use_container_width=True)
        
    # Cost items tabular breakdown
    st.markdown("#### Detail Expense Breakdown (INR)")
    costs_table = {
        "Expense Category": [],
        "Calculation Details": [],
        "Estimated Cost (₹)": []
    }
    
    # Add items manually
    costs_table["Expense Category"].append("Accommodation (Hotels)")
    costs_table["Calculation Details"].append(f"{rooms_needed} room(s) × ₹{dest['costs']['accommodation'][budget_tier]:,} per night × {trip_days} night(s)")
    costs_table["Estimated Cost (₹)"].append(f"₹{cost_res['Accommodation']:,}")
    
    costs_table["Expense Category"].append("Food & Dining")
    costs_table["Calculation Details"].append(f"₹{dest['costs']['food'][budget_tier]:,} per person/day × {traveler_count} traveler(s) × {trip_days} day(s)")
    costs_table["Estimated Cost (₹)"].append(f"₹{cost_res['Food']:,}")
    
    costs_table["Expense Category"].append("Local Transport")
    if budget_tier == "Budget":
        costs_table["Calculation Details"].append(f"Public Transit rate (₹{dest['costs']['transport'][budget_tier]:,}/day) × {traveler_count} traveler(s) × {trip_days} day(s)")
    else:
        costs_table["Calculation Details"].append(f"Private Car rental rate (₹{dest['costs']['transport'][budget_tier]:,}/day) × {trip_days} day(s)")
    costs_table["Estimated Cost (₹)"].append(f"₹{cost_res['Local Transport']:,}")
    
    costs_table["Expense Category"].append("Activities & Landmark entry")
    costs_table["Calculation Details"].append(f"Avg fee ₹{dest['costs']['activity_avg']} per spot × 1.5 spots/day × {traveler_count} traveler(s) × {trip_days} day(s)")
    costs_table["Estimated Cost (₹)"].append(f"₹{cost_res['Activities & Entry Fees']:,}")
    
    costs_table["Expense Category"].append("Emergency Buffer / Misc Shopping")
    costs_table["Calculation Details"].append("15% contingency reserve")
    costs_table["Estimated Cost (₹)"].append(f"₹{cost_res['Emergency Buffer (15%)']:,}")
    
    costs_table["Expense Category"].append("**Grand Total**")
    costs_table["Calculation Details"].append("**Sum of all travel expenses**")
    costs_table["Estimated Cost (₹)"].append(f"**₹{cost_res['Total']:,}**")
    
    costs_df = pd.DataFrame(costs_table)
    st.table(costs_df)
