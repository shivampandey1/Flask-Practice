import csv
import requests
import datetime
from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/json', methods=['GET', 'POST'])
def json():
    if request.method == 'POST':  #this block is only entered when the form is submitted
            data = request.form['data']
            dictToSend = data
            print("data type: ", type(dictToSend))
            print("data : ", dictToSend)
            output = requests.post('http://localhost:5001/', json=dictToSend)
            print('response from server:',output)
            dictFromServer = output.json()
            print("final dict: ", dictFromServer)
            writer(dictFromServer['1700s'],dictFromServer['1800s'],dictFromServer['1900s'],dictFromServer['2000s'])
            return '''<h3>{}</h3>'''.format('check source folder of this server for csv')
    
    return '''<form method="POST">
                      enter json data: <input type="text" name="data"><br>
                      <input type="submit" value="Submit"><br>
                  </form>'''
    
# =============================================================================
#     dictToSend = [{"id": 1,"president": 1,"nm": "George Washington","pp": "None, Federalist","tm": "1789-1797"},{"id": 2,"president": 2,"nm": "John Adams","pp": "Federalist","tm": "1797-1801"}]
#     output = requests.post('http://localhost:5001/', json=dictToSend)
#     print('response from server:',output)
#     dictFromServer = output.json()
#     return "finished"
#     #we're done here
# =============================================================================
  
if __name__ == '__main_':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000
    
def writer(seventeens, eighteens, nineteens, twoks):
    with open("presidentTest.csv", "w", newline="") as file:
     thewriter = csv.writer(file)
     
     #writing headers
     thewriter.writerow(["Name", "Party", "Presidential term", "President Number", "Ingestion Time"])
     
     #writing file content
     #assumed "year president began their team in (mm-dd-yyy)" to mean (yyyy)
     for x in seventeens:
         if "F" not in x['pp']:
             thewriter.writerow([x['nm'], x['pp'], x['tm'][0:4], x['president'], datetime.datetime.now()])
     thewriter.writerow("\n")
     for x in eighteens:
         if "F" not in x['pp']:
             thewriter.writerow([x['nm'], x['pp'], x['tm'][0:4], x['president'], datetime.datetime.now()])
     thewriter.writerow("\n")
     for x in nineteens:
         if "F" not in x['pp']:
             thewriter.writerow([x['nm'], x['pp'], x['tm'][0:4], x['president'], datetime.datetime.now()])
     thewriter.writerow("\n")
     for x in twoks:
         if "F" not in x['pp']:
             thewriter.writerow([x['nm'], x['pp'], x['tm'][0:4], x['president'], datetime.datetime.now()])