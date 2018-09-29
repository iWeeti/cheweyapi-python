import asyncio
import aiohttp
import json


class Client:
	def __init__(self, token):
		self.token = token

	async def dog(self):
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f'http://api.chewey-bot.ga/dog/?auth={self.token}') as r:
				r = await r.json()
		return r['data']

	async def cat(self):
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f'http://api.chewey-bot.ga/cat/?auth={self.token}') as r:
				r = await r.json()
		return r['data']

	async def birb(self):
		async with aiohttp.ClientSession() as cs:
			async with cs.get(f'http://api.chewey-bot.ga/birb/?auth={self.token}') as r:
				r = await r.json()
		return r['data']