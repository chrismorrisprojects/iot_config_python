import requests
from requests.auth import HTTPBasicAuth
def rv_50_request(web_address, timeout_interval, data='', cookie=''):
	headers = {
		'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,video/x-mng,image/png,image/jpeg,image/gif;q=0.2,*/*;q=0.1',
		'Pragma': 'no-cache',
		'Cache-Control': 'no-cache, must-revalidate',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
		'Content-Type': 'text/xml',
		'Origin': web_address,
		'Referer': web_address+'/admin/ACEmanagerX.html',
	}	
	r = requests.post(web_address, headers=headers, data=data, timeout=timeout_interval, cookies=cookie)
	return r.status_code, r.cookies, r.text
	
def gx_440_request(web_address, timeout_interval, data=''):

	r = requests.post(web_address, data=data)
	return r.status_code, r.text