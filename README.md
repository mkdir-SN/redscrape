# redscrape

## Greetings
Hello! I made a pretty simple scraper for r/mechmarket, since I was tired of manually searching for specific posts throughout the day.

I figured I should make this scraper applicable to any other subreddits which have a selling format similar to r/mechmarket. To be more specific, subreddits which contain posts that have [<country_code>-<state_code>] formatting. And so you have it!

## Setup
1. [Install PRAW](https://praw.readthedocs.io/en/stable/getting_started/installation.html)
2. [OAuth setup](https://redditclient.readthedocs.io/en/latest/oauth/)
3. Input the credentials you received from following OAuth setup into `auth.py`

## Scraping
Open the directory you cloned this repo into.

You have the following command line args to work with:
* `-subreddit` - the subreddit you'd like to scrape
* `-contains` - text entries to match posts against*
* `-limit` - number of posts to scrape (default is 100)
* `-flair` ex. `selling`
* `-country_code` ex. `US`, `USA`
* `-state_code` ex. `CA`

*If a text entry has spaces in it, then put double quotes around it. ex. `"Tofu 60"` instead of `Tofu 60`

Here's an example command for the command line:

`python3 main.py -subreddit mechmarket -contains "KBD67 Lite" Portico Tofu65`

And here's another:

`python3 main.py -subreddit hardwareswap -contains 3080 -country-code USA -state-code CA -flair selling -limit 100`

There are two ways to run the command you wrote:
* Run the command directly on the command line
* Paste the command into `command.txt` and run `sh command.txt` on the command line (useful if you have different commands for different subreddits you're scraping)

## PMing
Say you would like to PM matches to yourself or any other Reddit user. This is probably a better option than reading the matches on the command line, since Reddit formatting is much easier on the eyes.

Open `auth.py` then:
* Input the correct `username` and `password` of the Reddit account you're sending from
* Input a Reddit username for `to_username`

Open `scrape.py` then:
* Uncomment the code blocks which are reserved for PMing users
