# My Notes

## Part 2 

* Database Setup
  * changed mysite/settings.py, timezone configuration.
  * Creating models: in our simple poll app we'll ceate two models: 
    * Question: has a question **text** and a publication date.
    * Choice: has the text of choice and a vote tally.
      **Each Choice is associated with a Question**

* Activating Models: 
  To include the app in our project, we need to add a reference to its configuration 
class in the INSTALLED_APPS setting. The **PollsConfig** class is in the 
**polls/apps.py** file, so its dotted path is **'polls.PollsConfig'**.

