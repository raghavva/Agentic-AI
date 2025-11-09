
# from langchain.tools import tool
# from crawl4ai import AsyncWebCrawler
# import asyncio
# import json
# import re
# from typing import Dict, List
# from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, LLMConfig
# from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
# from crawl4ai import LLMExtractionStrategy
# from tools.schema.flight_options import FlightOptions
# import os

# from dotenv import load_dotenv
# load_dotenv()

# class FlightTools:
    
#     @tool("Scrape flight prices from airline websites")
#     @staticmethod
#     def scrape_flight_prices(origin: str, destination: str, departure_date: str, return_date: str = None, provider: str = "openai", model_name: str = "gpt-4o-mini", api_token: str = os.getenv("OPENAI_API_KEY")):
#         """
#         Scrape flight prices from multiple airline websites.
        
#         Args:
#             origin: Origin airport code (e.g., 'LAX', 'JFK')
#             destination: Destination airport code (e.g., 'SFO', 'LHR')
#             departure_date: Departure date in YYYY-MM-DD format
#             return_date: Return date in YYYY-MM-DD format (optional for one-way)
        
#         Returns:
#             JSON string containing flight options with prices
#         """

#         browser_config = BrowserConfig(headless=True)

#         crawler_config = CrawlerRunConfig(
#         cache_mode=CacheMode.BYPASS,
#         word_count_threshold=1,
#         page_timeout=80000,
#         extraction_strategy=LLMExtractionStrategy(
#             llm_config = LLMConfig(
#                 provider=f"{provider}/{model_name}",
#                 api_token=api_token
#             ),
#             schema=FlightOptions.model_json_schema(),
#             extraction_type="schema",
#             instruction="""From the crawled content, extract all information related to the flight options.""",
#             max_scroll_steps=10
#         ),
#     )

#         async def scrape_flights():
#             flight_data = []
#             async with AsyncWebCrawler(config=browser_config) as crawler:
#                         result = await crawler.arun(
#                             url=f"https://www.google.com/flights?hl=en#flt={origin}.{destination}.{departure_date}",
#                             config = crawler_config
#                         )

#                         flight_data.append(result.extracted_content)
                            
            
#             return json.dumps(flight_data, indent=2)
        
#         # Run the async function
#         return asyncio.run(scrape_flights())
    
#     @tool("Find cheapest flight option")
#     @staticmethod
#     def find_cheapest_flight(flight_data_json: str):
#         """
#         Analyze scraped flight data to find the cheapest option.
        
#         Args:
#             flight_data_json: JSON string containing flight options
        
#         Returns:
#             String with the cheapest flight details
#         """
#         try:
#             flight_data = json.loads(flight_data_json)
            
#             if not flight_data:
#                 return "No flight data available"
            
#             cheapest_flight = None
#             min_price = float('inf')
            
#             for flight in flight_data:
#                 # Extract numeric price from string
#                 price_str = flight.get('price', '0')
#                 price_match = re.search(r'[\d,]+', price_str.replace('$', '').replace(',', ''))
                
#                 if price_match:
#                     price = float(price_match.group())
#                     if price < min_price:
#                         min_price = price
#                         cheapest_flight = flight
            
#             if cheapest_flight:
#                 return f"""
#                 CHEAPEST FLIGHT FOUND:
#                 Airline: {cheapest_flight.get('airline', 'N/A')}
#                 Price: ${min_price:.2f}
#                 Departure: {cheapest_flight.get('departure_time', 'N/A')}
#                 Arrival: {cheapest_flight.get('arrival_time', 'N/A')}
#                 Duration: {cheapest_flight.get('duration', 'N/A')}
#                 Stops: {cheapest_flight.get('stops', 'N/A')}
#                 """
#             else:
#                 return "No valid flight prices found"
                
#         except Exception as e:
#             return f"Error processing flight data: {str(e)}"




#     async def extract_structured_data_using_llm(
#         provider: str, 
#         model_name: str,
#         api_token: str = None, 
#         extra_headers: Dict[str, str] = None
#     ):
#         print(f"\n--- Extracting Structured Data with {provider} ---")

#         if api_token is None and provider != "ollama":
#             print(f"API token is required for {provider}. Skipping this example.")
#             return

#         browser_config = BrowserConfig(headless=True)

#         extra_args = {"temperature": 0, "top_p": 0.9, "max_tokens": 2000}
#         if extra_headers:
#             extra_args["extra_headers"] = extra_headers

#         crawler_config = CrawlerRunConfig(
#             cache_mode=CacheMode.BYPASS,
#             word_count_threshold=1,
#             page_timeout=80000,
#             extraction_strategy=LLMExtractionStrategy(
#                 llm_config = LLMConfig(
#                     provider=f"{provider}/{model_name}",
#                     api_token=api_token
#                 ),
#                 schema=FlightOptions.model_json_schema(),
#                 extraction_type="schema",
#                 instruction="""From the crawled content, extract all information related to the different graduate degrees at the university, their benefiits, curriculum and admission requirements and their respecive URL .""",
#                 extra_args=extra_args,
#                 max_scroll_steps=10
#             ),
#         )

#         async with AsyncWebCrawler(config=browser_config) as crawler:
#             result = await crawler.arun(
#                 url="https://www.ut.edu/graduate-degrees", config=crawler_config
#             )
#             print(result.extracted_content)