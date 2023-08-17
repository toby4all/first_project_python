from flask import Flask, request
from db_connector import get_user

app = Flask(__name__)

@app.route('/users/get_user_data/<user_id>')
def getuser(user_id):
    if request.method == 'GET':
        user_name = get_user(user_id)
        if user_name !=None:
            return "<H1 id = 'user'>" + user_name + "</H1>"
        else:
            return "<H1 id = 'no-user'>"'No such user with this id: ' + user_id + "</H1>"

# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=5000)
