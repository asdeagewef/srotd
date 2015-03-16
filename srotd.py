import praw, time, random

#for SROTD


r = praw.Reddit(user_agent = "User-Agent: Python/urllib:srotd  (by /u/lizardsrock4)")
print("Logging in")
r.login("SROTDBouncer", "MGK0czpUbz2oHoAkkJBsqw")

meta_bots = ["TotesMessenger", "metaremovertester"]
removedCache = []
approvedCache = []


def run_bot():
    try:
        print("Starting Stream")
        subreddit = r.get_subreddit('subredditoftheday')
        editStream = subreddit.get_edited(limit=200)
        stream = subreddit.get_comments(limit=200)


    



        
        for comment in stream:
            if comment.id not in removedCache and comment.author.name in meta_bots :
                    print("Comment to remove found, comment id:" + comment.id + "User: " + comment.author.name)
                    comment.remove()
                    print("Removed!")
                    removedCache.append(comment.id)
        stream = subreddit.get_comments(limit=200)

        time.sleep(3)
        for comment in editStream:
            if comment.id not in approvedCache and comment.author.name in meta_bots :
                print("Comment to approve found, comment id:" + comment.id + "User: " + comment.author.name)
                comment.approve()
                print("Approved!")


                approvedCache.append(comment.id)





    except Exception:
        pass
        #print("Error, restarting")
        

                    
while True:
    run_bot()
    time.sleep(10)
