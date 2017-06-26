from check_404 import check_404

urls = ['http://facebook.com', 'http://google.com']

checker = check_404(urls)
results = checker.get_results()

for result in results:
	print("URL: {0} \nSTATUS: {1}\n".format(result['url'],result['code']))

