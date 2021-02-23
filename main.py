# imports
import requests
import os

# setup
filePath = "feed.xml"
episodeDirectory = "episodes" # leave blank for current
startAt = 13 # chronologically, your first unlistened to episode

# file handling
file = []
f = open(filePath)
for line in f: file.append(line)
f.close()


# generate lists of urls
urls = []
for line in file:
    if "url=" in line:
        line = line[22:]
        index = line.index('\"')
        urls.append(line[:index])
urls.reverse()


# generate lists of titles
titles = []
for line in file[4:]:
    if "<title>" in line:
        if ":" in line: # if the title has a colon, replace w/ hyphen
            index = line.index(":") 
            line = line[:index]+" -"+line[index+1:]
        index = line.index(">") + 1
        line = line[index:]
        index = line.index('<')
        titles.append(line[:index])
titles.reverse()


# generate list of episode paths
paths = []
if episodeDirectory == "": episodeDirectory=str(os.getcwd())
    
for i in range(len(titles)):
    newTitle = titles[i]+".mp3"
    thisPath = episodeDirectory+"\\"+newTitle
    paths.append(thisPath)
    

# access and download episodes
for i in range(startAt,len(urls)):
    r = requests.get(urls[i]) # request that webpage
    newFile = open(paths[i], 'wb+')
    newFile.write(r.content) # create a file, and write to it
    newFile.close()