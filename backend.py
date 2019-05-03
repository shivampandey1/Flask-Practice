import json
import csv
import datetime
import flask
from flask_csv import send_csv
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)
@app.route("/", methods=['POST'])

def home():
    input_json = request.get_json()
    input_json = json.loads(input_json)
    print('data from client:', input_json)
    finalDicts = rewriter2(input_json)
    #dictToReturn = {'answer':42}
    print("final dicts: ", finalDicts)
    print("jsonified: ", jsonify(finalDicts))
    return jsonify(finalDicts)
    

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    

# =============================================================================
# def rewriter(inputDict):
#     data = inputDict
#     #print(data)
#     
#     #defining containers for different centuries
#     eighteens = []
#     nineteens = []
#     twoks = []
#     
#     #sorting file data in alphabetical order
#     sortedData = sorted(data, key = lambda x: x['nm'])
#     
#     #iterating over file data and making changes
#     for x in sortedData:
#         #taking first name of president, then reversing
#         x['nm'] = x['nm'].split(' ', 1)[0][::-1]
#         #print("name: ", x['nm'])
#         
#         #defining holder variable for capital letters
#         caps = []
#         #selecting all capital leters in party names to build acronym
#         for y in x['pp']:
#             if y.isupper():
#                 caps.append(y)
#         x['pp'] = "".join(caps)
#         #print("party: ", x['pp'])
#         
#         #getting beginning of term
#         x['btm'] = x['tm'][0:2]
#         
#         #prints to test changes
#         #print("term: ", x['tm'])
#         #print("term began: ", x['btm'])
#         #print("number: ", x['president'])
#         #print("\n")
#         
#         #adding dicts to correct century
#         if x["btm"] == "18":
#             eighteens.append(x)
#         elif x["btm"] == "19":
#             nineteens.append(x)
#         elif x["btm"] == "20":
#             twoks.append(x)
#             
#     #writing to csv file 
#     with open("presidents.csv", "w", newline="") as file:
#         thewriter = csv.writer(file)
#         
#         #writing headers
#         thewriter.writerow(["Name", "Party", "Presidential term", "President Number", "Ingestion Time"])
#         
#         #writing file content
#         #assumed "year president began their team in (mm-dd-yyy)" to mean (yyyy)
#         for x in eighteens:
#             if "F" not in x['pp']:
#                 thewriter.writerow([x['nm'], x['pp'], x['tm'][0:4], x['president'], datetime.datetime.now()])
#         thewriter.writerow("\n")
#         for x in nineteens:
#             if "F" not in x['pp']:
#                 thewriter.writerow([x['nm'], x['pp'], x['tm'][0:4], x['president'], datetime.datetime.now()])
#         thewriter.writerow("\n")
#         for x in twoks:
#             if "F" not in x['pp']:
#                 thewriter.writerow([x['nm'], x['pp'], x['tm'][0:4], x['president'], datetime.datetime.now()])
# =============================================================================
                
def rewriter2(inputDict):
    data = inputDict
    for x in data:
        print("loop testing: ", x)
    print("data inputted to rewriter: ", data)
    

    #defining containers for different centuries
    seventeens = []
    eighteens = []
    nineteens = []
    twoks = []
     
    #sorting file data in alphabetical order
    sortedData = sorted(data, key = lambda x: (x['nm'], x['tm']))
    
    #iterating over file data and making changes
    for x in sortedData:
        #taking first name of president, then reversing
        x['nm'] = x['nm'].split(' ', 1)[0][::-1]
        print("name: ", x['nm'])
        
        #defining holder variable for capital letters
        caps = []
        #selecting all capital leters in party names to build acronym
        for y in x['pp']:
            if y.isupper():
                caps.append(y)
        x['pp'] = "".join(caps)
        print("party: ", x['pp'])
        
        #getting beginning of term
        x['btm'] = x['tm'][0:2]
        print("beginning of term: ", x['btm'])
        
        #prints to test changes
        print("term: ", x['tm'])
        print("term began: ", x['btm'])
        print("number: ", x['president'])
        print("\n")
        
        #adding dicts to correct century
        if x["btm"] == "18":
            eighteens.append(x)
        elif x["btm"] == "17":
            seventeens.append(x)
        elif x["btm"] == "19":
            nineteens.append(x)
        elif x["btm"] == "20":
            twoks.append(x)
    
    tupleHolder = {"1700s": seventeens, "1800s": eighteens, "1900s": nineteens, "2000s": twoks}
    return tupleHolder