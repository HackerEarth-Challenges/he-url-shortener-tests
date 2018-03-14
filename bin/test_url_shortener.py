import json
import requests
import sys
import unittest

class TestURLShortener(unittest.TestCase):

	def test_1(self):
		"""
		Provide a long url and gte the short url for it.
		Use the shortened url to get the actual url.

		"""
		end_point = self.end_point + "clean-urls/"
		response = requests.post(end_point, data={})

		long_url = 'https://www.hackerearth.com/challenge/hiring/hackerearth-python-developer-hiring-challenge/'

		data = {
			'long_url': long_url,
		}

		end_point = self.end_point + "fetch/short-url/"
		response = requests.post(end_point, data=data)
		self.assertEqual(response.status_code, 200, "Server did not return 200 OK!!!")

		response = json.loads(response.content)
		short_url = response['short_url']

		data = {
			"short_url": short_url,
		}

		end_point = self.end_point + "fetch/long-url/"
		response = requests.post(end_point, data=data)
		self.assertEqual(response.status_code, 200, "Server did not return 200 OK!!!")

		response = json.loads(response.content)
		response_long_url = response['long_url']

		self.assertEqual(long_url, response_long_url, "Long url matching failed!!!")

		count = 1
		for _ in xrange(count):
			response = requests.post(short_url, data={})

		end_point = self.end_point + "fetch/count/"

		data = {
			'short_url': short_url,
		}
		response = requests.post(end_point, data=data)

		response = json.loads(response.content)

		self.assertEqual(count, response['count'], "URL access count did not match!!!")


	def test_2(self):
		"""
		Provide a list of complete urls and get the long urls.
		Provide the long url and get the short url.

		"""
		end_point = self.end_point + "clean-urls/"
		response = requests.post(end_point, data={})

		long_urls = ['https://www.hackerearth.com/challenge/hiring/hackerearth-python-developer-hiring-challenge/']

		data = {
			'long_urls': json.dumps(long_urls)
		}

		end_point = self.end_point + "fetch/short-urls/"
		response = requests.post(end_point, data=data)
		self.assertEqual(response.status_code, 200, "Server did not return 200 OK!!!")

		response = json.loads(response.content)
		long_to_short_url_map = response['short_urls']

		short_urls = long_to_short_url_map.values()

		data = {
			"short_urls": json.dumps(short_urls),
		}

		end_point = self.end_point + "fetch/long-urls/"
		response = requests.post(end_point, data=data)
		self.assertEqual(response.status_code, 200, "Server did not return 200 OK!!!")

		response = json.loads(response.content)
		long_urls = response['long_urls']

		for url in long_urls:
			key = long_urls[url]
			self.assertEqual(long_to_short_url_map[key], url, "Long url matching failed!!!")


if __name__ == '__main__':
	TestURLShortener.end_point = sys.argv[1]
	sys.argv = sys.argv[:1]
	unittest.main()