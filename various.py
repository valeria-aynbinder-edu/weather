# api.openweathermap.org/data/2.5/weather?q=London&appid={API key}

# import requests
#
# # https://openweathermap.org/current
#
# url = "https://api.openweathermap.org/data/2.5/weather"
# response = requests.get(
#     url,
#     params={"q": "Jerusalem", "appid": "91201722ff1cc4a99e9c870bbbe2aafb", "units": "metric"}
# )
#
# if response.status_code == 200:
#
#     print(response.json())
# else:
#     print("Error", response.status_code)


# url = "https://api.kanye.rest"
# response = requests.get(url)
# if response.status_code == 200:
#     print(response.json())
# else:
#     print("Error:", response.status_code)


# response = requests.get(
#     "http://api.positionstack.com/v1/forward",
#     params={"query": "London", "access_key": "9d3e125d43feb5f93c8927b1a58e6fb7"}
# )
#
# print(response.json())


#caching mechanism
# singletone manager class
# worker - request weather in Tel-Aviv, Jerusalem, Haifa, Eilat every 5 min (configuration)
# singletone configuration manager
# user app - get weather for specific city. Check in cache, or request


# import aiohttp
# import asyncio
#
# async def main():
#
#     async with aiohttp.ClientSession() as session:
#         async with session.get("http://api.positionstack.com/v1/forward",
#                                params={"query": "London", "access_key": "9d3e125d43feb5f93c8927b1a58e6fb7"}) as response:
#
#             print("Status:", response.status)
#             print(await response.json())
#
# asyncio.run(main())





