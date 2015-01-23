Here are the steps for creating a Twitter App.

0.[Optional] Create a new Twitter account to post to (you could post to your own if you would like).
1. Login to your twitter account
2. Go to https://apps.twitter.com/ and click “Create New App”
3. Fill in the Data Twitter asks for (Name, Description, URL don’t matter for our purposes)
  3a. Website must include the protocol (https://)
  3b. Leave the callback url blank, we won’t need it for the Markov project
4. Agree to the Developer Agreement and Create the App
5. Click on the “Permissions” Tab and change the permissions to allow for Read & Write Access, save the form
6. Click on "Keys and Access Tokens”, Click on “Regenerate Consumer Key and Secret”, Confirm the action
7. Scroll to Access Tokens and click “Generate Access Token and Token Secret”

You now will have all of the Tokens / Consumer Keys you need.  You can now create a secrets.sh file in your project folder and put the needed export statements in there. Remember, you’ll need to run source secrets.sh whenever you open a new terminal window.

export VAR_NAME=‘SOME VALUE'

Also, as requested here is the code.

https://github.com/naudo/Twitter-API-Lecture

api.py is the first python file I was working with during lecture.
tweet_machine.py is the second file that performs the actual tweeting.


Cheers,
Nicholas