
import urllib2
from multiprocessing.pool import ThreadPool



class check_404(object):

	def __init__(self, urls):
		self.urls = urls

	def check_url(self, url):
		result = {}
		result['url'] = url
		result['code'] = urllib2.urlopen(url).getcode()
		return result


	def get_results(self):
		pool = ThreadPool(processes=len(self.urls))
		results = [pool.apply_async(self.check_url, (url,)) for url in self.urls]
		data = []
		
		for res in results:

			data.append(res.get())

		return data	




