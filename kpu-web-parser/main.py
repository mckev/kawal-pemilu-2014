from classes.browser import Browser

url = 'https://pilpres2014.kpu.go.id/c1.php'
content = Browser.browse_url(url)
print(content)
