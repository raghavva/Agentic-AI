import os
from crewai import Crew
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks
#from tools.flight_tools import FlightTools

from dotenv import load_dotenv
load_dotenv()

class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()
        #flight_tools = FlightTools()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()
        #flight_scraper = agents.flight_scraper_agent()
        #flight_analyst = agents.flight_analyst_agent()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests
        )

        identify_city = tasks.identify_city_task(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.date_range,
            self.interests
        )

        # scrape_flights = tasks.scrape_flight_prices_task(
        #     flight_scraper,
        #     self.origin,
        #     self.cities.split(',')[0].strip(),  # Use first city as destination
        #     self.date_range.split(' to ')[0].strip() if ' to ' in self.date_range else self.date_range,
        #     self.date_range.split(' to ')[1].strip() if ' to ' in self.date_range else None
        # )

        # analyze_flights = tasks.analyze_flight_options_task(
        #     flight_analyst,
        #     scrape_flights
        # )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide], #, flight_scraper, flight_analyst],
            tasks=[plan_itinerary, identify_city, gather_city_info], #, scrape_flights, analyze_flights],  # Reorder tasks
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print("-------------------------------")
    
    origin = input(dedent("""From where will you be traveling from? """))
    cities = input(dedent("""What are the cities options you are interested in visiting? """))
    date_range = input(dedent("""What is the date range you are interested in traveling? """))
    interests = input(dedent("""What are some of your high level interests and hobbies? """))

    trip_crew = TripCrew(origin, cities, date_range, interests)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Here is you Trip Plan")
    print("########################\n")
    print(result)