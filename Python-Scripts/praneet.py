# AUTHOR : DEV UBEROI || twitter: @devuberoi
# THIS SCRIPT IS ONLY FOR EXTRACTING DATA FROM http://eduraft.com
# ONLY FOR PERSONAL USE, THE AUTHOR DOES NOT HOLD ANY RESPOSIBILITY OF ANY UNWATED/UNDESIRED USE OF THIS SCRIPT

from xlwt import Workbook
import lxml.html
import requests
import sys

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
			content = doc.xpath('//span[@itemprop="name"]/text()')
			content2 = doc.xpath('//span[@itemprop="streetAddress"]/p/text()')
			content3 = doc.xpath('//div[@class="smallAlertText js-school-search-result-street"]/p/a/text()')
			content4 = doc.xpath('//span[@itemprop="description"]/text()')
			c1 = len(content)
			c3 = len(content3)
			year = 3

			for x in range(0,c1):
				writesheet.write(r1,0,content[x])
				writesheet.write(r1,1,content2[x])
				writesheet.write(r1,2,content4[year])
				year = year+5
				r1 = r1+1

			for t in range(0,c3):
				writesheet2.write(r2,0,content3[t])
				r2 = r2+1

	except IndexError:
		pass

	book.save('/home/dev/school_years.xls')

if __name__ == '__main__':
	main()
