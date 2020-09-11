from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


status_info = dict()
@app.route("/", methods = ['POST','GET'])
def hello():
    #return "Hello World!"
    return render_template("test.html")
    
@app.route('/signup', methods = ['POST','GET'])
def signup():
    return render_template("signup.html")
    

@app.route('/store',methods = ['POST', 'GET'])
def store():
    if request.method == 'POST':
        #return (json.dumps(request.form))
        dictionary=request.form
        #x=dict(name=dictionary["fname"], name1=dictionary["lname"])
        #return(x)
        j = json.dumps(dictionary)
        f = open("dict.json","a")
        f.write(j)
        f.close()        
        return render_template("login.html")    


                 
    
@app.route('/login',methods = ['POST', 'GET'])
#if request.method == 'GET':
def login():
    return render_template("login.html")

@app.route('/validate',methods = ['POST', 'GET'])
def validate():
    if request.method == 'POST':
        dictionary=request.form
        name=dictionary["fname"]
        name1=dictionary["lname"]
        #return(name+name1)
        f=open("dict.json", "r")
        x=f.read()
        f.close()
        y=x.replace("}{", "}  {")
        #print(y)
        #print(type(y.split('  ')))
        z=y.split('  ')
        for item in z:
            a=item.split(",")
            o=a[1].replace("}","")[10:]
            n=a[0][10:]
            #return(name+n+name1+o)
            #break
            if name in n and name1 in o:
                #return("valid")
                return('<h1>Welcome you are an authorised user</h1><br><a href="/"><button type="button">Go back to Main page</button>')
        #return("invalid user")
        return('<h1>Hey Sheep!! You are not the valid user. Please signup first and try again logging into it.</h1><br><a href="/"><button type="button">Go back to Main page</button>')



if __name__ == "__main__":
    app.run()