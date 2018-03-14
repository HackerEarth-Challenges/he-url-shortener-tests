import requests
import sys
import unittest

class TestURLShortener(unittest.TestCase):

	def test_test_1(self):
		"""
		Provide a long url and gte the short url for it.
		Use the shortened url to get the actual url.

		"""

		long_url = 'https://www.hackerearth.com/challenge/hiring/hackerearth-python-developer-hiring-challenge/'

		data = {
			'long_url': long_url,
		}

		end_point = self.end_point + "fetch/short-url/"
		response = requests.post(end_point, data=data)
		self.assertEqual(response.status_code, 200)

		short_url = response.short_url

		data = {
			"short_url": short_url,
		}

		end_point = self.end_point + "fetch/long-url/"
		response = requests.post(end_point, data=data)
		self.assertEqual(response.status_code, 200)

		self.assertEqual(long_url, response.long_url)		


	def test_test_2(self):
		"""
		Provide a list of complete urls and get the long urls.
		Provide the long url and get the short url.

		"""
		long_urls = ['https://www.hackerearth.com/challenges/',
					'https://www.hackerearth.com/challenge/hiring/hackerearth-python-developer-hiring-challenge/']

		data = {
			'long_urls': long_urls
		}

		end_point = self.end_point + "fetch/short-urls/"
		response = request.post(end_point, data=data)
		self.assertEqual(response.status_code, 200)

		short_urls = response.short_urls

		data = {
			"short_urls": short_urls,
		}

		end_point = self.end_point + "fetch/long-urls"
		response = requests.post(end_point, data=data)
		self.assertEqual(response.status_code, 200)

		long_urls = response.short_urls
		# Reverse the short url dictionary
		long_to_short_url_map = {}
		for url in long_urls:
			long_to_short_url_map[long_urls[url]] = url

		for url in long_urls:
			self.assertEqual(short_url[url], long__to_short_url_map.get(url))


if __name__ == '__main__':
	TestURLShortener.end_point = sys.argv[1]
	sys.argv = sys.argv[:1]
	unittest.main()