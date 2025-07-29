import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/weatherapi/api/weatherapi-com'

mcp = FastMCP('weatherapi-com')

@mcp.tool()
def realtime_weather_api(q: Annotated[str, Field(description='Query parameter based on which data is sent back. It could be following: Latitude and Longitude (Decimal degree) e.g: q=48.8567,2.3508 city name e.g.: q=Paris US zip e.g.: q=10001 UK postcode e.g: q=SW1 Canada postal code e.g: q=G2J metar: e.g: q=metar:EGLL iata:<3 digit airport code> e.g: q=iata:DXB auto:ip IP lookup e.g: q=auto:ip IP address (IPv4 and IPv6 supported) e.g: q=100.0.0.1')]) -> dict: 
    '''Current weather or realtime weather API method allows a user to get up to date current weather information in json and xml. The data is returned as a Current Object.'''
    url = 'https://weatherapi-com.p.rapidapi.com/current.json'
    headers = {'x-rapidapi-host': 'weatherapi-com.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def forecast_weather_api(q: Annotated[str, Field(description='Query parameter based on which data is sent back. It could be following: Latitude and Longitude (Decimal degree) e.g: q=48.8567,2.3508 city name e.g.: q=Paris US zip e.g.: q=10001 UK postcode e.g: q=SW1 Canada postal code e.g: q=G2J metar: e.g: q=metar:EGLL iata:<3 digit airport code> e.g: q=iata:DXB auto:ip IP lookup e.g: q=auto:ip IP address (IPv4 and IPv6 supported) e.g: q=100.0.0.1')],
                         days: Annotated[Union[int, float, None], Field(description='Number of days of forecast required. Default: 3')] = None,
                         lang: Annotated[Union[str, None], Field(description="Returns 'condition:text' field in API in the desired language ")] = None,
                         dt: Annotated[Union[str, datetime, None], Field(description="If passing 'dt', it should be between today and next 10 day in yyyy-MM-dd format. ")] = None) -> dict: 
    '''Forecast weather API method returns upto next 14 day weather forecast and weather alert as json. It contains astronomy data, day weather forecast and hourly interval weather information for a given city.'''
    url = 'https://weatherapi-com.p.rapidapi.com/forecast.json'
    headers = {'x-rapidapi-host': 'weatherapi-com.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'days': days,
        'lang': lang,
        'dt': dt,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def history_weather_api(q: Annotated[str, Field(description='Query parameter based on which data is sent back. It could be following: Latitude and Longitude (Decimal degree) e.g: q=48.8567,2.3508 city name e.g.: q=Paris US zip e.g.: q=10001 UK postcode e.g: q=SW1 Canada postal code e.g: q=G2J metar: e.g: q=metar:EGLL iata:<3 digit airport code> e.g: q=iata:DXB auto:ip IP lookup e.g: q=auto:ip IP address (IPv4 and IPv6 supported) e.g: q=100.0.0.1')],
                        dt: Annotated[Union[str, datetime], Field(description="For history API 'dt' should be on or after 1st Jan, 2010 in yyyy-MM-dd format ")],
                        lang: Annotated[Union[str, None], Field(description="Returns 'condition:text' field in API in the desired language")] = None,
                        hour: Annotated[Union[int, float, None], Field(description='Restricting history output to a specific hour in a given day. Default: 0')] = None,
                        end_dt: Annotated[Union[str, datetime, None], Field(description="Restrict date output for History API method. Should be on or after 1st Jan, 2010. Make sure end_dt is equal to or greater than 'dt'. ")] = None) -> dict: 
    '''History weather API method returns historical weather for a date on or after 1st Jan, 2010 (depending upon subscription level) as json.'''
    url = 'https://weatherapi-com.p.rapidapi.com/history.json'
    headers = {'x-rapidapi-host': 'weatherapi-com.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'dt': dt,
        'lang': lang,
        'hour': hour,
        'end_dt': end_dt,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def marine_weather_api(q: Annotated[str, Field(description='Query parameter based on which data is sent back. It could be following: Latitude and Longitude (Decimal degree) e.g: q=48.8567,2.3508 city name e.g.: q=Paris US zip e.g.: q=10001 UK postcode e.g: q=SW1 Canada postal code e.g: q=G2J metar: e.g: q=metar:EGLL iata:<3 digit airport code> e.g: q=iata:DXB auto:ip IP lookup e.g: q=auto:ip IP address (IPv4 and IPv6 supported) e.g: q=100.0.0.1')],
                       days: Annotated[Union[int, float, None], Field(description='Default: 1')] = None,
                       lang: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Marine weather API returns upto next 7 day marine and sailing weather forecast and tide data for global marine/sea points.'''
    url = 'https://weatherapi-com.p.rapidapi.com/marine.json'
    headers = {'x-rapidapi-host': 'weatherapi-com.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'days': days,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def future_weather_api(q: Annotated[str, Field(description='Query parameter based on which data is sent back. It could be following: Latitude and Longitude (Decimal degree) e.g: q=48.8567,2.3508 city name e.g.: q=Paris US zip e.g.: q=10001 UK postcode e.g: q=SW1 Canada postal code e.g: q=G2J metar: e.g: q=metar:EGLL iata:<3 digit airport code> e.g: q=iata:DXB auto:ip IP lookup e.g: q=auto:ip IP address (IPv4 and IPv6 supported) e.g: q=100.0.0.1')],
                       dt: Annotated[Union[str, datetime], Field(description="'dt' should be between 14 days and 300 days from today in the future in yyyy-MM-dd format (i.e. dt=2023-01-01) ")],
                       lang: Annotated[Union[str, None], Field(description="Returns 'condition:text' field in API in the desired language ")] = None) -> dict: 
    '''Future weather API method returns weather in a 3 hourly interval in future for a date between 14 days and 300 days from today in the future.'''
    url = 'https://weatherapi-com.p.rapidapi.com/future.json'
    headers = {'x-rapidapi-host': 'weatherapi-com.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'dt': dt,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_autocomplete_api(q: Annotated[str, Field(description='Query parameter based on which data is sent back. It could be following: Latitude and Longitude (Decimal degree) e.g: q=48.8567,2.3508 city name e.g.: q=Paris US zip e.g.: q=10001 UK postcode e.g: q=SW1 Canada postal code e.g: q=G2J metar: e.g: q=metar:EGLL iata:<3 digit airport code> e.g: q=iata:DXB auto:ip IP lookup e.g: q=auto:ip IP address (IPv4 and IPv6 supported) e.g: q=100.0.0.1')]) -> dict: 
    '''Search or Autocomplete API returns matching cities and towns.'''
    url = 'https://weatherapi-com.p.rapidapi.com/search.json'
    headers = {'x-rapidapi-host': 'weatherapi-com.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def time_zone_api(q: Annotated[str, Field(description='Query parameter based on which data is sent back. It could be following: Latitude and Longitude (Decimal degree) e.g: q=48.8567,2.3508 city name e.g.: q=Paris US zip e.g.: q=10001 UK postcode e.g: q=SW1 Canada postal code e.g: q=G2J metar: e.g: q=metar:EGLL iata:<3 digit airport code> e.g: q=iata:DXB auto:ip IP lookup e.g: q=auto:ip IP address (IPv4 and IPv6 supported) e.g: q=100.0.0.1')]) -> dict: 
    '''Time Zone API method allows a user to get up to date time zone and local time information in json.'''
    url = 'https://weatherapi-com.p.rapidapi.com/timezone.json'
    headers = {'x-rapidapi-host': 'weatherapi-com.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def iplookup_api(q: Annotated[str, Field(description='e.g: q=auto:ip IP address (IPv4 and IPv6 supported) e.g: q=100.0.0.1')]) -> dict: 
    '''IP Lookup API method allows a user to get up to date information for an IP address in json.'''
    url = 'https://weatherapi-com.p.rapidapi.com/ip.json'
    headers = {'x-rapidapi-host': 'weatherapi-com.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def astronomy_api(q: Annotated[str, Field(description='Query parameter based on which data is sent back. It could be following: Latitude and Longitude (Decimal degree) e.g: q=48.8567,2.3508 city name e.g.: q=Paris US zip e.g.: q=10001 UK postcode e.g: q=SW1 Canada postal code e.g: q=G2J metar: e.g: q=metar:EGLL iata:<3 digit airport code> e.g: q=iata:DXB auto:ip IP lookup e.g: q=auto:ip IP address (IPv4 and IPv6 supported) e.g: q=100.0.0.1')],
                  dt: Annotated[Union[str, datetime, None], Field(description='Date')] = None) -> dict: 
    '''Astronomy API method allows a user to get up to date information for sunrise, sunset, moonrise, moonset, moon phase and illumination in json.'''
    url = 'https://weatherapi-com.p.rapidapi.com/astronomy.json'
    headers = {'x-rapidapi-host': 'weatherapi-com.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'dt': dt,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def sports_api(q: Annotated[str, Field(description='')]) -> dict: 
    '''Sports API method allows a user to get listing of all upcoming sports events for football, cricket and golf in json.'''
    url = 'https://weatherapi-com.p.rapidapi.com/sports.json'
    headers = {'x-rapidapi-host': 'weatherapi-com.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def alerts_api(q: Annotated[str, Field(description='')]) -> dict: 
    '''Alerts API returns alerts and warnings issued by government agencies (USA, UK, Europe and Rest of the World) as an array if available for the location provided.'''
    url = 'https://weatherapi-com.p.rapidapi.com/alerts.json'
    headers = {'x-rapidapi-host': 'weatherapi-com.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
