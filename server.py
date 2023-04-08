from flask import Flask, render_template, request, redirect, session # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "any string you want"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():

    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 1

    return render_template("index.html", count = session)




@app.route('/handle_form', methods=['post'])
def handle_it():
    if request.form["change"] == "add":
        session["count"] += 0
        return redirect("/")
    elif request.form["change"] == "goback":
        session["count"] = 0
        return redirect("/destroy_session")
    
# the original way-----------------------------------------------
    # def handle_it():
    # if request.form["change"] == "add":
    #     session["count"] += 0
    # elif request.form["change"] == "goback":
    #     session["count"] = 0





    # print("steve")
    # print(request.form['favorite_color'])
    # session['view'] = 1
    
   


    # session['favorite_color'] = request.form['favorite_color']
    
    
@app.route('/destroy_session')
def destroy():
    session.clear()	
    return redirect("/")	# clears all keys

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

