import auth
from datetime import datetime
import praw
import re
import sys

def get():
    map = {}
    contained = False

    for i in range(1, len(sys.argv) - 1):
        arg = sys.argv[i]
        if re.search("^-\w+", arg):
            if arg.lower() == "-contains":
                contained = True
            else:
                contained = False
                map[arg] = sys.argv[i + 1]
        elif contained:
            if "-contains" not in map:
                map["-contains"] = []
            map["-contains"].append(sys.argv[i])

    if "-subreddit" not in map:
        print("-subreddit not specified")
        return

    if "-contains" not in map:
        print("-contains not specified")
        return

    if "-limit" not in map:
        map["-limit"] = 100 # maximum Reddit will allow per request

    if "-flair" in map:
        map["-flair"] = map["-flair"].lower()

    reddit = praw.Reddit(client_id=auth.client_id, client_secret=auth.client_secret, user_agent=auth.user_agent)

    """
    Uncomment the following line if you'd like to PM the matches.

    reddit = praw.Reddit(client_id=auth.client_id, client_secret=auth.client_secret, user_agent=auth.user_agent, username=auth.username, password=auth.password)
    """

    new_posts = reddit.subreddit(map["-subreddit"]).new(limit=int(map["-limit"]))
    matches = []

    for post in new_posts:
        if "-country_code" in map:
            if "-state_code" in map:
                if not re.search("\[" + country_code + "-" + state_code + "\].*", post.title):
                    continue
            else:
                if not re.search("\[" + country_code + "-\w+\].*", post.title):
                    continue
        else:
            if not re.search("\[\w+-\w+\].*", post.title):
                continue
        if "-flair" in map:
            if post.link_flair_text and map["-flair"] != post.link_flair_text.lower():
                continue
        for txt in map["-contains"]:
            if txt.lower() in post.title.lower():
                matches.append([str(datetime.fromtimestamp(post.created_utc)), post.link_flair_text, post.title, post.url])

    msg = "\n\nMatched " + str(len(matches)) + " posts in r/" + map["-subreddit"] + " containing any of the following: *" + ", ".join(map["-contains"]) + ".*\n\n"

    n = 1

    for match in matches:
        msg += "---------- \n\n**MATCH " + str(n) + "**\n" + match[0] + "\n" + match[1] + "\n" + match[2] + "\n[LINK](" + match[3] + ")\n\n"
        n += 1

    print(msg)

    """
    Uncomment the following code block if you'd like to PM the matches to a Reddit account.

    msg_title = "Matched posts in r/" + map["-subreddit"]
    reddit.redditor(auth.to_username).message(msg_title, msg)
    """
