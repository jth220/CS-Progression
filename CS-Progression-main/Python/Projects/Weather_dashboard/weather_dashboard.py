import requests
import typer
from rich.console import Console
from rich.table import Table
city = "london"
api_key = "--------------"
headers = { #This is so the server can identify who is sending the requests
      "Accept" : 'application/json',
      "User-Agent": "hello-cloud-ingest/1.0"
    }
params = { "q": city, 
               "appid": api_key, 
               "units": "metric" 
             }
base_url = "https://api.openweathermap.org/data/2.5/forecast"
last_err =""
try:
    weather_retrieve = requests.get(base_url, params=params, headers=headers)
#This would normally be wrapped in a try and except
except requests.exceptions.Timeout as e:
        last_err = str(e)
        print("Request Timed out")



current_weather_json = weather_retrieve.json()


table = Table(title="3-Day Weather Forecast")
table.add_column("Date", justify="right", style="cyan", no_wrap=True)
table.add_column("Temp (°C)", justify="right", style="yellow")
table.add_column("Feels Like", justify="right", style="bright_yellow")
table.add_column("Weather", style="magenta")
table.add_column("Wind (m/s)", justify="right", style="green")
table.add_column("Humidity (%)", justify="right", style="blue")

for entry in current_weather_json["list"][:24]:
    table.add_row(
        entry["dt_txt"],  # timestamp
        f"{entry['main']['temp']}°C",  
        f"{entry['main']['feels_like']}°C",  
        entry["weather"][0]["description"],  
        f"{entry['wind']['speed']} m/s",  
        f"{entry['main']['humidity']}%"  
    )    


console = Console()
console.print(table)