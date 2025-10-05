import streamlit as st
import os
from main import TripCrew
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="🌍 AI Trip Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def display_trip_plan(result):
    """Display the trip plan in a simple text box"""
    # Use Streamlit's built-in text display
    st.text_area(
        "Trip Plan Details",
        value=str(result),
        height=500,
        disabled=True,
        help="Your complete trip plan"
    )

def main():
    # Header
    st.title("🌍 AI Trip Planner")
    st.subheader("Let AI create the perfect travel itinerary for you")
    
    # Create two columns for better layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📝 Trip Details")
        
        # Form inputs
        origin = st.text_input(
            "📍 Where are you traveling from?",
            placeholder="e.g., New York, San Francisco, London"
        )
        
        cities = st.text_input(
            "🏙️ What cities are you interested in visiting?",
            placeholder="e.g., Paris, Rome, Barcelona or Japan, Thailand, Vietnam"
        )
        
        date_range = st.text_input(
            "📅 What is your travel date range?",
            placeholder="e.g., March 15-20, 2024 or Summer 2024"
        )
        
        interests = st.text_area(
            "🎯 What are your interests and hobbies?",
            placeholder="e.g., Art museums, hiking, local cuisine, nightlife, historical sites, beaches",
            height=100
        )
        
        # Plan trip button
        plan_trip = st.button("🚀 Plan My Trip", type="primary")
    
    with col2:
        st.markdown("### ℹ️ How it works")
        st.markdown("""
        Our AI travel agents work together to create your perfect trip:
        
        **🧑‍💼 Expert Travel Agent**
        - Creates detailed 5-day itineraries
        - Includes budget estimates and packing suggestions
        - Provides flight and hotel recommendations
        
        **🏙️ City Selection Expert**
        - Analyzes weather, season, and prices
        - Compares multiple destinations
        - Selects the best city for your trip
        
        **🗺️ Local Tour Guide**
        - Provides insider knowledge
        - Suggests hidden gems and local spots
        - Shares cultural insights and practical tips
        """)
    
    # Handle form submission
    if plan_trip:
        # Validate inputs
        if not all([origin, cities, date_range, interests]):
            st.error("❌ Please fill in all fields before planning your trip!")
            return
        
        # Show loading state
        with st.spinner("🤖 Our AI travel agents are working hard to create your perfect itinerary..."):
            try:
                # Create and run the trip crew
                trip_crew = TripCrew(origin, cities, date_range, interests)
                result = trip_crew.run()
                
                # Display results
                st.markdown("### 🎯 Your Personalized Trip Plan")
                display_trip_plan(result)
                
                # Add download button for the trip plan
                st.download_button(
                    label="📥 Download Trip Plan",
                    data=str(result),
                    file_name=f"trip_plan_{origin}_{cities.replace(',', '_')}.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"❌ An error occurred while planning your trip: {str(e)}")
                st.info("💡 Make sure your OpenAI API key is set in the .env file")

if __name__ == "__main__":
    main()