from .scrap import scrap_news

def gnews(sentence_to_categorize):
    newschannels = ['wion','bbc news english','euronews']
    sentence_to_categorize = "+".join(sentence_to_categorize.split())
    youtube_search_url = "https://www.youtube.com/results?search_query="


    for i in newschannels:
        if i == 'wion':
            global wion
            wion = scrap_news(youtube_search_url+sentence_to_categorize+"+"+i)
        elif i == 'bbc news english':
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
    sd = 0
    for i in nl:
        for j in i:
            if sd == 0:
                clean1_wion.append({'title':j['title'],'channel':j['channel'],'badge':j['verified_badge']})
            elif sd == 1:
                clean1_bbc.append({'title':j['title'],'channel':j['channel'],'badge':j['verified_badge']})
            else:
                clean1_euronews.append({'title':j['title'],'channel':j['channel'],'badge':j['verified_badge']})
        sd = sd+1
    ###this cleaning is where we will keep only the titles from the news channels and also 
    ###we remove the bbc news from the end of the title
    clean2_wion = []
    clean2_bbc= []
    clean2_euronews = []
    list1 = [clean1_wion,clean1_bbc,clean1_euronews]
    ds = 0
    for i in list1:
        j =0
        while j<len(i):
            ch = i[j]['badge']
            if ch == True:
                if ds == 0:
                    clean2_wion.append(i[j])
                elif ds == 1:
                    clean2_bbc.append(i[j])
                elif ds == 2:
                    clean2_euronews.append(i[j])
            else:
                i.pop(j)
                j = j-1        
            j = j+1
        ds = ds + 1
            
            
           
    
    
    return clean2_wion,clean2_bbc,clean2_euronews
    ###i may have to remove non english titles if they exits later on in the data

