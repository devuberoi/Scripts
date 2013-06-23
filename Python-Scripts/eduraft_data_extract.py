# AUTHOR : DEV UBEROI || twitter: @devuberoi
# THIS SCRIPT IS ONLY FOR EXTRACTING DATA FROM "http://eduraft.com"
# ONLY FOR PERSONAL USE
# THE AUTHOR DOES NOT HOLD ANY RESPOSIBILITY OF ANY UNWATED/UNDESIRED USE OF THIS SCRIPT
# REQUIREMENTS : python 2.7.3+ (i have tested only on this version, should work on above this)
# PACKAGES : lxml , xlwt, xlrd, requests (can be installed through 'pip')

from xlwt import Workbook
import lxml.html
import requests
import sys

# the url is broken in two parts to loop it through several pages

URL1 = "http://eduraft.com/school/Delhi/Delhi/"
URL2 = "/%3Cfilter%3ErankTier%5B%5D=A&rankTier%5B%5D=B&mediumformfilter%5B%5D=English&ownershipformfilter%5B%5D=Private+School&typeformfilter%5B%5D=Boys&typeformfilter%5B%5D=Co-Education&typeformfilter%5B%5D=Girls&classes_toformfilter%5B%5D=12%3Cfilter%3E"


def main():
	try:
		book = Workbook()
		writesheet = book.add_sheet("Name Address")
		writesheet2 = book.add_sheet("Websites")
		r1 = 0
		r2 = 0

		for i in range(1,58):
			url = URL1+str(i)+URL2
			req = requests.get(url)
			doc = lxml.html.fromstring(req.content)
			schoolname = doc.xpath('//span[@itemprop="name"]/text()')
			schooladdress = doc.xpath('//span[@itemprop="streetAddress"]/p/text()')
			schoolwebsite = doc.xpath('//div[@class="smallAlertText js-school-search-result-street"]/p/a/text()')
			schoolyear = doc.xpath('//span[@itemprop="description"]/text()')
			l1 = len(schoolname)
			l2 = len(schoolwebsite)
			year = 3

			for x in range(0,l1):
				writesheet.write(r1,0,schoolname[x])
				writesheet.write(r1,1,schooladdress[x])
				writesheet.write(r1,2,schoolyear[year])
				year = year+5
				r1 = r1+1

			for x in range(0,l2):
				writesheet2.write(r2,0,schoolwebsite[x])
				r2 = r2+1

# the IndexErrors have been skipped because the last page of the results on eduraft may or may-not contain 8 results

	except IndexError:
		pass

	book.save('/home/dev/school_years.xls')

if __name__ == '__main__':
	main()
