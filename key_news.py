from bs4 import BeautifulSoup
import requests

ls = ["v060r", "fxcne", "4ijzo", "7o40h", "vjkf0", "96xmi", "7hmxu", "lefjd", "alien", "vejhb", "mz9a6", "tgihv", "utohw", "rp3g1", "fnsdm", "gstfd", "o020f", "i8z4b", "e9uak", "k9qxx", "9jh01", "89rcx", "yrxnh", "2y1b3", "xw5np", "276xh", "x2s57", "2b6f7", "t76dy", "il0d5", "ff8vi", "m7c30", "a5b38", "s94o9", "w17qs", "44bd3", "wnpxm", "mars", "epmqk", "ki0ag", "rs500", "etdbc", "nu5q2", "223j4", "ue9sp", "8bue1", "me6mc", "n0sh4", "3hqk3", "w8xh4", "i5cxs", "0rmqe", "kpisp", "jck0j", "k3dip", "oywsu", "eej3o", "wixg4", "62al1", "tjgzq", "jhpfy", "o4zx6", "wup33", "m88dt", "tvygb", "24hcw", "pjfb8", "3dfng", "wzeai", "0z6uz", "zaden", "pcxjo", "z732w", "jdjws", "byzms"]
for n in ls:
	url = "https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/secret_json/"+n+".json"
	r = requests.get(url)
	data = r.text
	s = data.encode('utf-8')
	str = s[16:len(s)-18]
	print str
#for sorting the output got to this url: http://ideone.com/74QjhV