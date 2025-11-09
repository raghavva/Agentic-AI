import streamlit as st
import os
from main import TripCrew
from dotenv import load_dotenv
import time
import json
from datetime import datetime, date
#from tools.flight_tools import FlightTools

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
    st.text_area(
        "Trip Plan Details",
        value=str(result),
        height=500,
        disabled=True,
        help="Your complete trip plan"
    )

def display_flight_results(flight_data):
    """Display flight search results in a formatted way"""
    if isinstance(flight_data, str):
        try:
            flight_data = json.loads(flight_data)
        except:
            st.text_area("Flight Search Results", value=flight_data, height=400)
            return
    
    if isinstance(flight_data, list) and flight_data:
        st.markdown("### ✈️ Flight Options Found")
        
        for i, flight in enumerate(flight_data, 1):
            with st.expander(f"Flight Option {i}: {flight.get('airline', 'Unknown Airline')}"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Price", flight.get('price', 'N/A'))
                    st.metric("Airline", flight.get('airline', 'N/A'))
                
                with col2:
                    st.metric("Departure", flight.get('departure_time', 'N/A'))
                    st.metric("Arrival", flight.get('arrival_time', 'N/A'))
                
                with col3:
                    st.metric("Duration", flight.get('duration', 'N/A'))
                    st.metric("Stops", flight.get('stops', 'N/A'))
    else:
        st.warning("No flight options found. Please try different search parameters.")

# def run_flight_search(origin, destination, departure_date, arrival_date):
#     """Run the flight search using the flight agents"""
#     try:
#         # Import flight tools here to avoid circular imports
#         #from tools.flight_tools import FlightTools
        
#         flight_tools = FlightTools()
        
#         # Scrape flight prices
#         flight_data = flight_tools.scrape_flight_prices(
#             origin, destination, departure_date, arrival_date
#         )
        
#         # Find cheapest option
#         cheapest_flight = flight_tools.find_cheapest_flight(flight_data)
        
#         return flight_data, cheapest_flight
        
#     except Exception as e:
#         st.error(f"Error during flight search: {str(e)}")
#         return None, None

def main():
    # Header
    st.title("🌍 AI Trip Planner")
    st.subheader("Your AI-powered travel companion")
    
    # Create tabs
    tab1, tab2 = st.tabs(["🗺️ Trip Planning", "✈️ Flight Search"])
    
    # Trip Planning Tab
    with tab1:
        st.markdown("### Plan Your Complete Trip")
        
        # Create two columns for better layout
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("#### 📝 Trip Details")
            
            # Form inputs
            origin = st.text_input(
                "📍 Where are you traveling from?",
                placeholder="e.g., New York, San Francisco, London",
                key="trip_origin"
            )
            
            cities = st.text_input(
                "🏙️ What cities are you interested in visiting?",
                placeholder="e.g., Paris, Rome, Barcelona or Japan, Thailand, Vietnam",
                key="trip_cities"
            )
            
            date_range = st.text_input(
                "📅 What is your travel date range?",
                placeholder="e.g., March 15-20, 2024 or Summer 2024",
                key="trip_dates"
            )
            
            interests = st.text_area(
                "🎯 What are your interests and hobbies?",
                placeholder="e.g., Art museums, hiking, local cuisine, nightlife, historical sites, beaches",
                height=100,
                key="trip_interests"
            )
            
            # Plan trip button
            plan_trip = st.button("🚀 Plan My Trip", type="primary", key="plan_trip_btn")
        
        with col2:
            st.markdown("#### ℹ️ How it works")
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
        
        # Handle trip planning form submission
        if plan_trip:
            # Validate inputs
            if not all([origin, cities, date_range, interests]):
                st.error("❌ Please fill in all fields before planning your trip!")
            else:
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
    
    # Flight Search Tab
    # with tab2:
    #     st.markdown("### Find the Best Flight Deals")
        
    #     # Create two columns for better layout
    #     col1, col2 = st.columns([1, 1])
        
    #     with col1:
    #         st.markdown("#### ✈️ Flight Search")
            
    #         # Flight search form
    #         flight_origin = st.text_input(
    #             "🛫 Origin Airport/City",
    #             placeholder="e.g., LAX, JFK, New York, Los Angeles",
    #             key="flight_origin",
    #             help="Enter airport code (LAX, JFK) or city name"
    #         )
            
    #         flight_destination = st.text_input(
    #             "🛬 Destination Airport/City",
    #             placeholder="e.g., SFO, LHR, San Francisco, London",
    #             key="flight_destination",
    #             help="Enter airport code (SFO, LHR) or city name"
    #         )
            
    #         # Date inputs
    #         col_dep, col_arr = st.columns(2)
            
    #         with col_dep:
    #             departure_date = st.date_input(
    #                 "📅 Departure Date",
    #                 value=date.today(),
    #                 key="departure_date",
    #                 help="Select your departure date"
    #             )
            
    #         with col_arr:
    #             arrival_date = st.date_input(
    #                 "📅 Return Date",
    #                 value=date.today(),
    #                 key="arrival_date",
    #                 help="Select your return date (optional for one-way)"
    #             )
            
    #         # Trip type
    #         trip_type = st.radio(
    #             "Trip Type",
    #             ["Round Trip", "One Way"],
    #             key="trip_type"
    #         )
            
    #         # Search flights button
    #         search_flights = st.button("🔍 Search Flights", type="primary", key="search_flights_btn")
        
    #     with col2:
    #         st.markdown("#### ℹ️ Flight Search Features")
    #         st.markdown("""
    #         Our AI-powered flight search provides:
            
    #         **🕷️ Web Scraping**
    #         - Scrapes real-time prices from multiple airlines
    #         - Checks major booking platforms
    #         - Gets current availability and pricing
            
    #         **🤖 AI Analysis**
    #         - Finds the cheapest options
    #         - Analyzes best value flights
    #         - Considers duration vs price trade-offs
    #         - Provides alternative route suggestions
            
    #         **📊 Comprehensive Results**
    #         - Multiple airline options
    #         - Detailed flight information
    #         - Price comparisons
    #         - Duration and stop analysis
    #         """)
        
    #     # Handle flight search form submission
    #     if search_flights:
    #         # Validate inputs
    #         if not all([flight_origin, flight_destination]):
    #             st.error("❌ Please fill in origin and destination!")
    #         elif departure_date < date.today():
    #             st.error("❌ Departure date cannot be in the past!")
    #         elif trip_type == "Round Trip" and arrival_date <= departure_date:
    #             st.error("❌ Return date must be after departure date!")
    #         else:
    #             # Convert dates to string format
    #             dep_date_str = departure_date.strftime("%Y-%m-%d")
    #             arr_date_str = arrival_date.strftime("%Y-%m-%d") if trip_type == "Round Trip" else None
                
    #             # Show loading state
    #             with st.spinner("🔍 Searching for the best flight deals..."):
    #                 try:
    #                     # Run flight search
    #                     flight_data, cheapest_flight = run_flight_search(
    #                         flight_origin, flight_destination, dep_date_str, arr_date_str
    #                     )
                        
    #                     if flight_data:
    #                         # Display flight results
    #                         st.markdown("### 🎯 Flight Search Results")
    #                         display_flight_results(flight_data)
                            
    #                         # Display cheapest option prominently
    #                         if cheapest_flight:
    #                             st.markdown("### 💰 Cheapest Option")
    #                             st.success(cheapest_flight)
                            
    #                         # Add download button for flight results
    #                         st.download_button(
    #                             label="📥 Download Flight Results",
    #                             data=json.dumps(flight_data, indent=2) if isinstance(flight_data, list) else flight_data,
    #                             file_name=f"flights_{flight_origin}_{flight_destination}_{dep_date_str}.json",
    #                             mime="application/json"
    #                         )
    #                     else:
    #                         st.warning("No flight data retrieved. Please check your search parameters.")
                            
    #                 except Exception as e:
    #                     st.error(f"❌ An error occurred during flight search: {str(e)}")
    #                     st.info("💡 Make sure crawl4ai is installed and your API keys are configured")

if __name__ == "__main__":
    main()