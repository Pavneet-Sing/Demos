"""
Script to demonstrate the various features of Beautiful Soup for web scraping
"""
from bs4 import BeautifulSoup
import requests
import re
content = '''
<!DOCTYPE html>               --> 1
<html>                        --> 2
  <head>                      --> 3
    <title>List of Game Engines</title>
    <style type="text/css">   --> 4
      table, th, td{
        border: solid 2px black;
        border-collapse: collapse;
        border-color: lightgrey;
        padding: 4px;
      }
      table th{
        color: blue;
        font-size:  20px;
      }
      table td{
        color: green;
        font-size: 25px;
      }
    </style>
  </head>
  <body>                      --> 5
    <div>                     --> 6
      <table>                 --> 7
        <tr>
          <th>Name</th>
          <th>Language</th>
          <th>Platform</th>
        </tr><br>
        <tr>
          <td>Unreal Engine</td>
          <td>C++</td>
          <td>Cross platform</td>
        </tr>
      </table>
    </div>
  </body>
</html>
'''

URL = 'https://en.wikipedia.org/wiki/List_of_game_engines'
EXAMPLES = ["print rows",
            "print pretty response",
            "print all rows",
            "demonstrate attribute class based search with 'wikitable sortable' value",
            "demonstrate the importance of regex to find all 'Id Tech' engines",
            "demonstrate string and limit parameters to find max 2 'C' language links ",
            "demonstrate tag 'soup.table.tr' and 'soup.title' properties",
            "demonstrate link with href parameter",
            "demonstrate function passing, 'isAnchorTagWithLargeText'",
            "demonstrate select to parse nested tags, selec('html head title')"]

def run(arg, URL = '', parser = 'html.parser', content = ''):
    if(arg == 0):
        content = requests.get(URL)
        soup = BeautifulSoup(content.text, parser)
        row = soup.find('tr') # Extract and return first occurrence of tr
        print(row)            # Print row with HTML formatting
        print("=========Text Result==========")
        print(row.get_text()) # Print row as text
    elif(arg == 1):
        content = requests.get(URL)
        soup = BeautifulSoup(content.text, parser)
        soup.prettify()
        print(soup)
    elif(arg == 2):
        content = requests.get(URL)
        soup = BeautifulSoup(content.text, parser)
        rows = soup.find_all('tr')
        for row in rows:
            print(row.get_text())
    elif(arg == 3):
        content = requests.get(URL)
        soup = BeautifulSoup(content.text,parser)
        row  = soup.find('table')
        contentTable  = soup.find('table', { "class" : "wikitable sortable"})
##        row  = soup.find_all('table', class_ ="wikitable sortable")
        rows  = contentTable.find_all('tr')
        for row in rows:
            print(row.get_text())
        print(row)
    elif(arg == 4):
        content = requests.get(URL)
        soup = BeautifulSoup(content.text,parser)
        contentTable  = soup.find('table', { "class" : "wikitable sortable"})
        rows  = contentTable.find_all('a', title = re.compile('^Id Tech .*'))
        print('\n' * 10)
        for row in rows:
            print(row.get_text())
    elif(arg == 5):
        content = requests.get(URL)
        soup = BeautifulSoup(content.text,parser)
        contentTable  = soup.find('table', { "class" : "wikitable sortable"})
        rows  = contentTable.find_all('a', string = 'C', limit = 2
                                      #, recursive = False
                                      )
        print('\n' * 10)
        print(rows)
    elif(arg == 6):
        content = requests.get(URL)
        soup = BeautifulSoup(content.text, parser)
        print('\n' * 10)
        print(soup.title)
        print(soup.table.tr)
    elif(arg == 7):
        content = requests.get(URL)
        soup = BeautifulSoup(content.text,parser)
        tags = soup.find_all(href = True, limit = 10)
        print(tags)
    elif(arg == 8):
        content = requests.get(URL)
        soup = BeautifulSoup(content.text,parser)
        tags = soup.find_all(isAnchorTagWithLargeText, limit = 10, text = True)
        for row in tags:
            print(row.get_text())
    elif(arg == 9):
        content = requests.get(URL)
        soup = BeautifulSoup(content.text,parser)
        print(soup.select("html head title")[0].get_text())
    print('\n' * 5) # For convenient visual

def isAnchorTagWithLargeText(tag):
    return True if tag.name == 'a' and len(tag.get_text()) > 50 else False

def printSelection():
    print('Press:')
    for i in range(0, len(EXAMPLES)):
        print('',i,'to',EXAMPLES[i], sep = ' ')
    


if __name__ == '__main__':
    while(True):
        printSelection()
        choice = input('Enter choice: ')
        run(int(choice), URL)
        exitLoop = input('Continue? Y/N : ').lower()
        if(exitLoop == 'n'):
            break
