import wikipedia

enwp = wikipedia.getSite('en','wikipedia')

amazonurl = '*.amazon.com'

linkset = enwp.linksearch(amazonurl, limit=1000000)

totallinks = 0
mainlinks = 0

try:
    for page in linkset:
        print page
        totallinks += 1
        if page.namespace() == 0:
            print page
            mainlinks += 1
except KeyError:
    print totallinks

print totallinks
print mainlinks
