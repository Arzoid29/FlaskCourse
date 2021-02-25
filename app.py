from flask import Flask, request, redirect,make_response, render_template
app = Flask(__name__)


todos = ["comprar cafe ", "solicitud de compra ", "Traer"]


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

