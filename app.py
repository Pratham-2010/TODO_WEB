from flask import Flask, abort, render_template, redirect, url_for, flash, request,g

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Dummy authentication (replace later with real check)
        if username == "admin" and password == "123":
            return redirect(url_for("home"))
        else:
            return "Invalid credentials", 401

    return render_template("login.html")

@app.route("/secret")
def secret_login():
    return f"""
    <div style='margin:100px auto; width:400px; padding:20px;
                border:1px solid #ccc; border-radius:8px; text-align:center;'>
      <h2>🤫 Secret Credentials</h2>
      <p><strong>Username:</strong> admin </p>
      <p><strong>Password:</strong> 123 </p>
      <a href='{url_for("login")}'><button>Go to Login</button></a>
    </div>
    """
    
if __name__=="__main__":
    app.run(debug=True)