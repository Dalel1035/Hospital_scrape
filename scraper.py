# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import urlparse
import lxml.html

def scrape_table(root):
  rows = root.cssselect("table.Trolley tr")
  for row in rows:
    record = {}
    table_cells = row.cssselect("td")
    if table_cells:
      record['Date']=table_cells[0].text
      record['Hospital']=table_cells[1].text
      record['Region']=table_cells[2].text
      record['Trolley Total']=table_cells[3].text
      record['Ward Total']=table_cells[4].text
      
      print record, '--------------'
      scraperwiki.sql.save(["Hospital"], record)
      
def scrape_and_look_for_next_link(url):
  html=scraperwiki.scrape(url)
  print html
  root = lxml.html.fromstring(html)
  scrape_table(root)
  
starting_url='http://inmo.ie/6022'
scrape_and_look_for_next_link(starting_url)
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
