from flask import Flask, request, redirect,make_response, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap =Bootstrap(app)


todos = ["comprar cafe ", "solicitud de compra ", "Traer"]


@app.errorhandler(404)
def not_found(error):
     return render_template("404.html", error=error)

@app.route("/")
def index():
    user_ip = request.remote_addr
    
    response = make_response(redirect('/hello'))
    response.set_cookie("user_ip", user_ip)
   
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get("user_ip")
    context = { "user_ip":user_ip, "todos":todos,}
    
    return render_template("hello.html", **context)

if __name__ == '__main__':
    app.run(debug=True,port=5000)

