# Flask-Practice
Pair of servers that build a csv based on user inputted json file regarding presidents.

#HOW TO USE:

-Install flask (pip install flask)
-Navigate to directory where backend.py is saved in terminal
-Run $'export flask flask_app=backend.py'
-Run $'flask run --port 5001'
-Open terminal and navigate to app.py
-Run $'export flask flask_app=app.py'
-Run $'flask run'
-goto http://127.0.0.1:5000/json
-Enter json data into box and hit submit
-navigate to directory where app.py is stored to find your csv

#MY APPROACH:

I started off by working on the part I was most comfortable with, the file operations. I figured that it would make the most sense to develop the logic that the servers would be deploying, then determine how to deploy them. I wanted to convert the keys of dictionaries provided to me after processing the JSON into the forms demanded by the question. After doing this, I could easily write the values to rows corresponding to the keys using the write library. My code focuses on manipulating the existing data to fit the form required as opposed to making copies to increase the algorithmic efficiency of the program. Once I determine the appropriate order, I split the list of dictionaries into set separated by century to meet the guideline without excessive use of for loops (again, for algorithmic efficiency).

I wrote the server code as I mentally envisioned it. The front end app sends a request to the backend for certain processing tasks to be done based on the json input provided, the backend is able to work with this data and produce the desired data. That data is then passed back to the front end app, builds the csv to requirements and tells you where to find it. This logical flow made sense in my head, so . I tried my best to effectively and simply implement it into code.

#DIFFICULTIES:

Originally, I wanted to do the entire process of creating the CSV in the backend, and I planned on passing the csv to the web app for download. However, I tried a bunch of different methods to return the CSV and was unable to find a workable solution. As such, I decided to modify the program flow a little bit to instead build the CSV in the webapp. Finding the most effective way to take input data was also challenging. I considered using an upload button to upload a file, but I felt that a text window was a superior option as theis allowed you to make adjustements to the JSON easily if you needed to.

#POSSIBLE IMPROVEMENTS
-Make an actual functional UI on the web app that allows for ease of use
-Include option for uploading files directly from computer
-Include distributed computing for large datasets
-Utilize a better library system to effectively generate the csv as opposed to generating it step by step
-Implement more explanatory routes so that users can utilize the site more effectively
-Include a status bar/ progress bar indicating how long it is taking for a file to be converted
