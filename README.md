# Blackjack!
This is a simple Blackjack game i have built, running on the code institute mock terminal via heroku. 
The goal of the game is to get a total card value of 21, while competeing against the dealer. The first to get 21, or as close to it as possible will win. However, if either party gets a total over 21, they will bust immediately losing! 
![deployed-image](deployed.png)
The app can be viewed at https://blackjack-jmp.herokuapp.com

## Author
Jake McParland

## Table of Contents
Generate after readme is complete for UX and below

## How To Play/Use
- When started, the user will need to cycle through the dealer handing out cards by pressing enter, 2 for the player and 2 for the dealer. 
- After the dealing, the user will need to decide to either hit using the "H" key or stand using the "S" key when prompted. The user will need to choose what to do based on their current total card value. 
-Choosing hit will draw another card for the player, while choosing stand will end the players turn and allow the dealer to reveal his hidden card and decide the winner. 
- Once the game reaches its conclusion after validating a blackjack, or a winning score, the option to restart will be offered to the player. 
The Player can enter "Y" to reset the hand or "N" to quit the game. 

## Features

### Implemented Features
- Random card deck generator :
- Score tracking : 
- User input for decision making : 
- A restart function : 

### Future Features
- Additional players to compete with 
- Multiple decks
- Online Multiplayer 
- Bet function 

## Data Model
For the data model in this project we generate a deck of cards in the Card class, and then assign both a number and unicode value. 

This data is passed through to the Blackjack function and a card is randomly drawn at specific intervals from this deck. 

Once a card has been selected from the deck, it is simultaneously removed from the deck as it would be in a game of blackjack. 

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your features and ensure that they all work as intended in an easy and straightforward way for the users to achieve their goals.

### Validation Testing
You should try to ensure you code is valid and follows proper indentation.  In this section you should write up any websites you used to validate your code. As your projects becomes more complex these tools may change.

- [CSS Validator](https://jigsaw.w3.org/css-validator/) Note, any error associated with root: color variables were ignored.
- [HTML Validator](https://validator.w3.org/)
- [JS validation](https://jshint.com) for each .js file/ , if using ES6, add this before pasting in your file: `/*jshint esversion: 6 */ `
- [JSON validation](https://jsonlint.com/) for each .json file 
- [PEP8 Validator](http://pep8online.com/) include a screenshot of results

Note any errors or warnings you are ignoring and why. IT IS BEST NOT to have ERRORS, but NINJA, COLOR VARIABLES sometimes are ok to ignore if you say the IDE that has the correct linters noted no errors. Or you can take the rendered HTML and run it through the HTML validator for the Flask html templates.

If the line is too long just add 
```$python 
# noqa
```
There is a space before the # and after it to skip the quality assurance for that line.

### Manual Testing

You can track your test in various ways.  

But for any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. 

1. Markdown
>  A particularly useful form for describing your testing process is via scenarios, such as:
> 
>  **Register Page**
>  Go to the Register page: http://<YOUR APPP>.herokuapp.com/register
>    - [x] Try to submit the empty form and verify that an error message about the required fields appears
>    - [x] Try to submit the form with an invalid username format and verify that a relevant error message appears
>    - [x] Try to submit the form with an invalid password format and verify that a relevant error message appears
>    - [x] Try to submit the form with an existing username, should re-render page with relevant error message/warning
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on profile page
>    - [x] Be logged in and go to register page url http://<YOUR APPP>.herokuapp.com/register, should have error saying you are already registered and be on profile page

2. Spreadsheet    
> Here is a [Manual Testing Template](https://docs.google.com/spreadsheets/d/189VpSeEG9oevSRhvb2WZl8zCk9L3s2iWQyrJ_1jjAGQ/edit?usp=sharing) that you can use as a starting point to keep track of your testing efforts. Make a copy of it in your own account and update as needed to reflect the browsers you are testing and features.  

3. GitHub Issues, Milestones & Boards
> You can also use agile tools in github to help track your testing and defects. Here's a document that I put together about that [process](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit?usp=sharing)
> 
> For more information you can visit: https://docs.github.com/en/issues/organizing-your-work-with-project-boards/managing-project-boards/about-project-boards 

It's ok to spot check specific functionality across devices and browsers but each page should be viewed as a whole for each device/browser combo at least once.

### Defect Tracking

You can use git hub issues to track any bugs rather than a spread sheet and just link to that page for your repository.

![image](https://user-images.githubusercontent.com/23039742/130149053-bf506388-a791-426e-8ffc-a56c1212e01c.png)

You should created issues in real time and close them out as you fix the bugs. Include steps to recreate and screenshots.

Create a link to the issues dashboard  of your repository
[ci_insights isssues](https://github.com/maliahavlicek/ci_mentor_insights/issues)

### Defects of Note
Some defects are more pesky than others. Highlight 3-5 of the bugs that drove you the most nuts and how you finally ended up resolving them.


### Outstanding Defects
It's ok to not resolve all the defects you found. If you know of something that isn't quite right, list it out and explain why you chose not to resolve it.

### Commenting Code

Make sure you  use triple double quotes to document fuctions and classes.
 Here'a  documentation worthy example:
```$python
def yes_no(question):
    """
    Function to ask a simple yes no question of the user.
    :param question: String displayed as the question
    :return: answer: String equal to "1" or "2" representing yes or no respectfully
    """
    print(question)
    print("yes = 1")
    print("no = 2")
    answer = input("enter your answer here \n").strip()
    while answer not in ("1", "2"):
        print("please choose 1 for yes and 2 for no")
        answer = input("enter your answer here \n").strip()
    return answer

```

## Deployment

### Requirements
If the user is required to have certain keys and credentials you should include this section with diretions on how to get the necessary information.
ex)
1. **Google Account:** In order to have this program work, you need a google account. If you don't have one  [Create a google account](https://accounts.google.com/Signup)
2. **Google APIs**
    1. in a new incognito tab, log into your new google account.
    1. then update the url to be: https://console.cloud.google.com/getting-started?pli=1 
        
        **GOOGLE DRIVE API Access**
        1.  create a new project for this, call it XXXXXX (You might want to refer to what you see in this video: https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/ at the bottom of the screen to write out steps.)
        2. Then click on Add APIs and Services and select Libraries
        3. Search for Google Drive
        4. Click Enable
        5. Click Create Credentials
        6. Select Google Drive API from the drop down, Application Data, then no and click the Next Button
        7.  (https://developers.google.com/drive/api/v3/enable-drive-api) 
        8. for service account details fill in a service account name ex) xxx_API, then click Create and Continue
        9. For the Accoun acces, select Role: Basic/Editor then continue
        10. Then Click Done
        11. Now select the newly created service account
        12. Click on the KEYS Tab
        13. Click Add Key
        14. Select JSON type (right click to show in folder so you know where the file was saved.
        
        **GOOGLE SHEETS API Access**
        You may need to us the back button get to the APIS & SErvices section from where you were.
        1. click the Libray  Tab and serarch for Google Sheets
        2. click enable

3. The downloaded credentialsJSON file is basically your creds.json file that you need to put into your heroku settings or gitpod environment to access your google drive.

4. Google Sheet Template
  - If you had to create specific sheets for your project, instruct users to make their own copy of it from yours and rename it back to what the python project expects
  - And don't forget to share the spreadsheet in question with the client_email from the creds.json 
### Gitpod
This section should describe the process someone would have to go through to get the local working in gitpod.  Such as install requirements.txt  and setting up a creds.json file that is in the gitignore and keeping their workspace.

If you have project settings required such as a creds.json file from the GOOGLE DRIVE API acess, please provide an example of that file in the writeup with the project key values:
```$python
{
    "type": "service_account",
    "project_id": "<YOUR_VALUE>",
    "private_key_id": "<YOUR_VALUE>",
    "private_key": "<YOUR_VALUE>",
    "client_email": "<YOUR_VALUE>",
    "client_id": "<YOUR_VALUE>",
    "auth_uri": "https://accoutns.google.com/0/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cer_url": "https://www.googleapis.com/oauth2/v1/certs",
    "clien_x509_cert_url": "<YOUR_VALUE>"
}
```

If you have any dependencies, you should instruct users to install them
```$python
pip3 install -r requirements.txt
```



### Heroku
This section should describe the process you went through to deploy the project to Heroku. Include screenshots if you think they would make the process easier.

You may want to re-watch the [python essentials deployment video](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/e3b664e16366444c8d722c5d8340b340/?child=first) when writing up this section.


If you have project settings required for Heroku, provide a table of the keys and values.
Do not share your personal keys but either cut them out of the screen shot or say <YOUR_VALUE> and include links on how the user would obtain such values.

#### Fork the repository
Make a fork so you have a copy of the repository in your own git hub account: https://github.com/maliahavlicek/portfolio_project_03

![image](https://user-images.githubusercontent.com/23039742/132136504-eb79a6f3-0205-4c82-80c2-eef136ec7e4c.png)


#### New Project
Log into Heroku and create a new project. Name it something like XXX_coders_bistro.


#### Settings
On the settings tab you have to address two things:
1. **Config Vars**

  ![image](https://user-images.githubusercontent.com/23039742/132135869-215d2e0f-805d-40a8-a8c2-fb1098e2645d.png)

  At a bar minimum you should show the user that they need to add the PORT. 8000 key value pair.


2. **Build Packs**

  ![image](https://user-images.githubusercontent.com/23039742/132135918-28cac112-7766-4277-905c-4a4963d8442d.png)

  add Python Then Node.js


#### Deploy
1. Set up to github and select the correct repository:

  ![image](https://user-images.githubusercontent.com/23039742/132136113-c257c921-d10c-4ccc-af09-6a1d25136395.png)

2. Deploy either manual or automatic

![image](https://user-images.githubusercontent.com/23039742/132136241-9d76fabb-39f0-4696-bc5f-047398fdaf41.png) 



## Credits

To avoid plagiarism amd copyright infringement, you should mention any other projects, stackoverflow, videos, blogs, etc that you used to gather imagery or ideas for your code even if you used it as a starting point and modified things. Giving credit to other people's efforts and ideas that saved you time acknowledges the hard work others did. 

-[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

### Content

Use bullet points to list out sites you copied text from and cross-reference where those show up on your site

### Media

Make a list of sites you used images from. If you used several sites try to match up each image to the correct site. This includes attribution for icons if they came from font awesome or other sites, give them credit.

### Acknowledgments

This is the section where you refer to code examples, mentors, blogs, stack overflow answers and videos that helped you accomplish your end project. Even if it's an idea that you updated you should note the site and why it was important to your completed project.

If you used a CodeInstitute Instructional project as a starting point. Make note of that here too.