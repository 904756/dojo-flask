from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

get_number_of_requests = 0
post_number_of_requests = 0
var_delete = 0
var_put = 0

@app.route('/')
def count_get_post():
    return render_template('index.html')

@app.route('/request-counter', methods=['GET', 'POST', 'DELETE', 'PUT'])
def send_request():
    global get_number_of_requests
    global post_number_of_requests
    global var_delete
    global var_put
    if request.method == 'GET':
        get_number_of_requests += 1
    elif request.method == "POST":
        post_number_of_requests += 1
    elif request.method == "DELETE":
        var_delete += 1
    elif request.method == "PUT":
        var_put += 1
    #return render_template('index.html')
    return redirect('/')

@app.route('/statistics')
def send_statistics():
    return render_template('statistics.html', get_number_of_requests=get_number_of_requests, post_number_of_requests=post_number_of_requests, var_delete = var_delete,
var_put = var_put)


# @app.route('/story', methods=['GET', 'POST'])
# def route_story_add():
#     if request.method == 'POST':
#         # Cast received Form data to normal Python dictionary
#         user_story = {
#             'title': request.form.get('title'),
#             'user_story': request.form.get('user_story'),
#             'acceptance_criteria': request.form.get('acceptance_criteria'),
#             'business_value': request.form.get('business_value'),
#             'estimation': request.form.get('estimation'),
#         }
#
#         data_handler.add_user_story(user_story)
#         return redirect('/')
#
#     empty_user_story = {




if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )