from .scrap import scrap_news

def gnews(sentence_to_categorize):
    newschannels = ['wion','bbc','euronews']
    sentence_to_categorize = "+".join(sentence_to_categorize.split())
    youtube_search_url = "https://www.youtube.com/results?search_query="


    for i in newschannels:
        if i == 'wion':
            global wion
            wion = scrap_news(youtube_search_url+sentence_to_categorize+"+"+i)
        elif i == 'bbc':
            global bbc
            bbc = scrap_news(youtube_search_url+sentence_to_categorize+"+"+i)
        else:
            global euronews
            euronews = scrap_news(youtube_search_url+sentence_to_categorize+"+"+i)
    ###this cleaning is where we are taking just the title and channel name and link
    clean1_wion= []
    clean1_bbc= []
    clean1_euronews = []
    nl = [wion,bbc,euronews]
    for i in nl:
        for j in i:
            if str(i) == "wion":
                clean1_wion.append({'title':j['title'],'channel':j['channel']})
            elif str(i) == "bbc":
                clean1_bbc.append({'title':j['title'],'channel':j['channel']})
            else:
                clean1_euronews.append({'title':j['title'],'channel':j['channel']})
    ###this cleaning is where we will keep only the titles from the news channels and also 
    ###we remove the bbc news from the end of the title
    clean2_wion = []
    clean2_bbc= []
    clean2_euronews = []
    list1 = [clean1_wion,clean1_bbc,clean1_euronews]
    for i in list1:
        j =0
        print(str(i))
        print(i)
        while j<len(i):
            ch = i[j]['channel']['channel_name']
            if ch == 'WION' or ch == 'BBC News' or ch == 'euronews':
                if ch == "BBC News":
                    temp = i[j]['title'].split()
                    temp = " ".join(temp[:-3])
                    i[j]['title'] = temp
            else:
                i.pop(j)
                j = j-1
           
            print(len(i))
            if ch == 'WION':
                clean2_wion.append(i[j])
            elif ch == 'BBC News':
                clean2_bbc.append(i[j])
            elif ch == 'euronews':
                clean2_euronews.append(i[j])
            j = j+1
            
            
           
    print(clean2_wion[0])
    print('hi dude')
    
    return clean2_wion,clean2_bbc,clean2_euronews
    ###i may have to remove non english titles if they exits later on in the data

