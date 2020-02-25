#libraries to include
# https://github.com/rcv911/coherence-function/blob/master/coherence_function_EEG.py

import os
from flask import request, jsonify
from app import app
import logger
@app.route('/get/questions/', methods=['GET', 'POST','DELETE', 'PATCH'])
def question():
    if request.method == 'POST':
        average_time = request.form.get('average_time')
        choices = request.form.get('choices')
        created_by = request.form.get('created_by')
        difficulty_level = request.form.get('difficulty_level')
        question = request.form.get('question')
        topics = request.form.get('topics')

# request.args is to get urls arguments 


# if request.method == 'GET':
#     start = request.args.get('start', default=0, type=int)
#     limit_url = request.args.get('limit', default=20, type=int)
#     questions = mongo.db.questions.find().limit(limit_url).skip(start);
#     data = [doc for doc in questions]
#     return jsonify(isError= False,
#                 message= "Success",
#                 statusCode= 200,
#                 data= data), 200

# request.form to get form parameter


