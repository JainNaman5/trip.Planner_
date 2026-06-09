# cost_estimator.py
"""
Cost estimation module.
Calculates dynamic trip costs based on duration, traveler count, and style.
Creates responsive Plotly visualizations for cost breakdown.
"""
import math
import pandas as pd
import plotly.express as px

def calculate_costs(destination_data, days, travelers, budget):
    """
    Computes a breakdown of estimated costs.
    Returns a dictionary of costs and a total.
    """
    costs_meta = destination_data["costs"]
    
    # 1. Accommodation: Assume 2 people per room (rounded up)
    rooms = math.ceil(travelers / 2)
    daily_room_rate = costs_meta["accommodation"][budget]
    total_accommodation = daily_room_rate * rooms * days
    
    # 2. Food: Per person per day
    daily_food_rate = costs_meta["food"][budget]
    total_food = daily_food_rate * travelers * days
    
    # 3. Local Transport:
    # Budget assumes public transport (per person). Mid-Range/Luxury assumes private cab (per day).
    daily_transport = costs_meta["transport"][budget]
    if budget == "Budget":
        total_transport = daily_transport * travelers * days
    else:
        total_transport = daily_transport * days
        
    # 4. Activities & Entry Fees:
    # Assume 1.5 attraction visits per day on average per person
    activity_base = costs_meta["activity_avg"]
    total_activities = int(activity_base * 1.5 * days * travelers)
    
    # Subtotal
    subtotal = total_accommodation + total_food + total_transport + total_activities
    
    # 5. Buffer/Emergency: 15% of subtotal
    buffer = int(subtotal * 0.15)
    
    total = subtotal + buffer
    
    return {
        "Accommodation": total_accommodation,
        "Food": total_food,
        "Local Transport": total_transport,
        "Activities & Entry Fees": total_activities,
        "Emergency Buffer (15%)": buffer,
        "Total": total,
        "details": {
            "rooms": rooms,
            "days": days,
            "travelers": travelers,
            "style": budget
        }
    }

def get_pie_chart(cost_breakdown, theme="light"):
    """
    Returns a Plotly Express Pie chart figure for the cost breakdown.
    """
    # Remove total from plotting
    plot_data = {k: v for k, v in cost_breakdown.items() if k not in ["Total", "details"]}
    
    df = pd.DataFrame({
        "Category": list(plot_data.keys()),
        "Cost (₹)": list(plot_data.values())
    })
    
    template = "plotly_dark" if theme == "dark" else "plotly_white"
    text_color = "#ffffff" if theme == "dark" else "#111827"
    
    fig = px.pie(
        df,
        values="Cost (₹)",
        names="Category",
        title="Expense Breakdown (INR)",
        color_discrete_sequence=px.colors.sequential.RdBu,
        hole=0.4
    )
    
    fig.update_traces(
        textposition='inside', 
        textinfo='percent+label',
        hovertemplate="<b>%{label}</b><br>Cost: ₹%{value:,.2f}<br>Percentage: %{percent}"
    )
    
    fig.update_layout(
        template=template,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        margin=dict(t=40, b=40, l=10, r=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Outfit, Inter, sans-serif", size=12, color=text_color)
    )
    
    return fig

def get_comparison_chart(destination_data, days, travelers, theme="light"):
    """
    Returns a Bar Chart comparing the total costs for Budget, Mid-Range, and Luxury tiers.
    """
    tiers = ["Budget", "Mid-Range", "Luxury"]
    totals = []
    
    for tier in tiers:
        res = calculate_costs(destination_data, days, travelers, tier)
        totals.append(res["Total"])
        
    df = pd.DataFrame({
        "Travel Style": tiers,
        "Total Cost (₹)": totals
    })
    
    template = "plotly_dark" if theme == "dark" else "plotly_white"
    text_color = "#ffffff" if theme == "dark" else "#111827"
    
    fig = px.bar(
        df,
        x="Travel Style",
        y="Total Cost (₹)",
        text="Total Cost (₹)",
        title="Cost Comparison by Travel Style",
        color="Travel Style",
        color_discrete_map={
            "Budget": "#2CA02C",      # Greenish
            "Mid-Range": "#FF7F0E",   # Orangeish
            "Luxury": "#D62728"       # Reddish
        }
    )
    
    fig.update_traces(
        texttemplate='₹%{text:,.0f}',
        textposition='outside',
        hovertemplate="<b>%{x} Style</b><br>Total Cost: ₹%{y:,.2f}"
    )
    
    fig.update_layout(
        template=template,
        yaxis_title="Total Cost (₹)",
        xaxis_title="Style Class",
        showlegend=False,
        margin=dict(t=40, b=20, l=10, r=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Outfit, Inter, sans-serif", size=12, color=text_color)
    )
    
    return fig
