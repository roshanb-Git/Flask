from flask import Flask, redirect,url_for
# WSGI application
app=Flask(__name__)   


@app.route('/')       # Decorator for root home page
def welcome():
    return 'Welcome to my application'

@app.route('/logging')       # Decorator for logging page
def loggin():
    return 'This is logging page'

@app.route('/success/<int:score>')       # Decorator for score
def success(score):
    return '<html><body><h1> Congratulations! Your score is:</h1></body></html>'+str(score)
   

@app.route('/fail/<int:score>')       # Decorator for score
def fail(score):
    return 'Oops! Your score is: '+ str(score)

@app.route('/result/<int:marks>')       # Decorator for score
def result(marks):
    result=''
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

if __name__=='__main__':  
    app.run(debug=True)
