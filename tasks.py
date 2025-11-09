# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet :

1) Identify desired output : A detailed 5 day trip plan for the user.

2) Task Planning :
    1) Itinerary planning : Develop a detailed plan for each day of the trip.
    2) City selection : Select the best cities for the trip based on weather, season, and prices.
    3) Local expert : Provide the best insights about the selected city.
    4) Flight agent : Provide the best flight options for the trip.
    5) Hotel agent : Provide the best hotel options for the trip.
    6) Packing agent : Provide the best packing suggestions for the trip.
    7) Budget agent : Provide the best budget suggestions for the trip.

3)Assign tasks to agents 

4) Task Decsription Template

"""


class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_date, interests):
        return Task(
            description=dedent(
                f"""
            **Task**: Develop a 5 day itinerary for the user.
            **Description**: Expand research into a a full 5-day travel 
                            itinerary with detailed per-day plans, including 
                            weather forecasts, places to eat, packing suggestions, 
                            and a budget breakdown.                                                
                            
                            You MUST suggest actual places to visit, actual hotels 
                            to stay and actual restaurants to go to.
                            
                            This itinerary should cover all aspects of the trip, 
                            from arrival to departure, integrating the city guide
                            information with practical travel logistics.
                            
            **Parameters**:
            - City: {city}
            - Travel Date: {travel_date}
            - Interests: {interests}

            **Note**: {self.__tip_section()}
                            
        """
            ),
            agent=agent,
        )

    def identify_city_task(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
            **Task**: Identify the best cities for the trip..
            **Description**: Analyze and select the best city for the trip based 
                            on specific criteria such as weather patterns, seasonal
                            events, and travel costs. This task involves comparing
                            multiple cities, considering factors like current weather
                            conditions, upcoming cultural or seasonal events, and
                            overall travel expenses. 
                                                            
                            Make sure you stay inside the country that the user requests.
                            
                            Your final answer must be a detailed
                            report on the chosen city, and everything you found out
                            about it, including the actual flight costs, weather 
                            forecast and attractions.
                            
            **Parameters**:
            - Origin: {origin}
            - Cities: {cities}
            - Interests: {interests}
            - Travel Dates: {travel_dates}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )


    def gather_city_info(self, agent, city, travel_dates, interests):
            return Task(
                description=dedent(
                    f"""
                **Task**: Gather in depth information about the city.
                **Description**: As a local expert on this city you must compile an 
                                in-depth guide for someone traveling there and wanting 
                                to have THE BEST trip ever!
                                Gather information about  key attractions, local customs,
                                special events, and daily activity recommendations.
                                Find the best spots to go to, the kind of place only a
                                local would know.
                                This guide should provide a thorough overview of what 
                                the city has to offer, including hidden gems, cultural
                                hotspots, must-visit landmarks, weather forecasts, and
                                high level costs.
                                                            
                                Make sure you only offer suggestions inside of the country.
                                
                                The final answer must be a comprehensive city guide, 
                                rich in cultural insights and practical tips, 
                                tailored to enhance the travel experience.

                                
                **Parameters**:
                - City: {city}
                - Travel Dates: {travel_dates}
                - Interests: {interests}

                **Note**: {self.__tip_section()}
            """
                ),
                agent=agent,
            )

    def scrape_flight_prices_task(self, agent, origin, destination, departure_date, return_date=None):
        return Task(
        description=dedent(
            f"""
            **Task**: Scrape flight prices from the sources
            **Description**: Use web scraping tools to collect real-time flight price data
                            from various airline websites and booking platforms for the specified route.
                            
                            Scrape data from at least 3 different sources to ensure comprehensive coverage.
                            Extract detailed information including airline, price, departure/arrival times,
                            duration, and number of stops.
                            
            **Parameters**:
            - Origin: {origin}
            - Destination: {destination}
            - Departure Date: {departure_date}
            - Return Date: {return_date if return_date else 'One-way trip'}

            **Note**: {self.__tip_section()}
            """
        ),
        agent=agent,
    )

    def analyze_flight_options_task(self, agent, flight_data):
        return Task(
            description=dedent(
                f"""
                **Task**: Analyze flight options and provide recommendations
                **Description**: Analyze the scraped flight data to identify the best options based on:
                                - Cheapest flights
                                - Best value (price vs convenience)
                                - Alternative routes
                                - Time considerations
                                
                                Provide detailed recommendations with reasoning for each option.
                                
                **Parameters**:
                - Flight Data: {flight_data}

                **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
        )