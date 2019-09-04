import numpy as np
import pandas as pd
import pickle
import re
from flask import Flask, request, Response, render_template

#instantiating app
app = Flask('PlayPredictor')

#creating form page
@app.route('/form')

def form():
    return render_template('form.html')

#creating output page
@app.route('/submit')

def submit():
    user_input = request.args

# check that time was inputted in the correct format using regex
    time_match = re.match('^[0-9]{1,2}\:[0-9]{2}',user_input['time'])

    if not time_match:
        error_message = 'Error: Time must be the format minute:seconds.'
        return render_template('form.html', error_message=error_message)

# parse through time to get minute and seconds
    minute = int(user_input['time'].split(':')[0])
    second = int(user_input['time'].split(':')[1])

# create error messages for times outside of scope of a game
    if minute not in range(0,16):
        error_message = 'Error: Minute must be greater than or equal to 0 and less than or equal to 15.'
        return render_template('form.html', error_message=error_message)

    if second not in range(0,60):
        error_message = 'Error: Seconds must be greater than or equal to 0 and less than 60.'
        return render_template('form.html', error_message=error_message)

# create quarter_seconds_remaining, game_seconds_remaining, half_seconds_remaining variables given time and quarter
    quarter_seconds_remaining = minute*60 + second

    if int(user_input['qtr']) == 1:
        game_seconds_remaining = minute*60 + second + 2700
        half_seconds_remaining = minute*60 + second + 900
    elif int(user_input['qtr']) == 2:
        game_seconds_remaining = minute*60 + second + 1800
        half_seconds_remaining = minute*60 + second
    elif int(user_input['qtr']) == 3:
        game_seconds_remaining = minute*60 + second + 900
        half_seconds_remaining = minute*60 + second + 900
    elif int(user_input['qtr']) == 4:
        game_seconds_remaining = minute*60 + second
        half_seconds_remaining = minute*60 + second

# create list that contains dictionary of inputs for model
    data = [{'down': int(user_input['down']),
            'qtr': int(user_input['qtr']),
            'game_seconds_remaining': game_seconds_remaining,
            'half_seconds_remaining': half_seconds_remaining,
            'quarter_seconds_remaining': quarter_seconds_remaining,
            'ydstogo': int(user_input['ydstogo']),
            'score_differential': int(user_input['score_differential']),
            'yardline_100': int(user_input['yardline_100'])
            }]

# load pickled model
    model = pickle.load(open('model.p', 'rb'))

# create dataframe of scenario
    scenario = pd.DataFrame(data,index=[0])

# the order of the columns matters because using predict in XGBoost models requires numpy arrays
# the code below reorders the columns correctly since pandas makes them alphabetical initially
    scenario = scenario[['down','qtr','game_seconds_remaining',
    'half_seconds_remaining','quarter_seconds_remaining','ydstogo',
    'score_differential','yardline_100']]

# make prediction using pickled model
    pass_probability = model.predict_proba(scenario.values)[0][0]
    run_probability = model.predict_proba(scenario.values)[0][1]
    raw_prediction = model.predict(scenario.values)[0]
    prediction_dict = {0:'Pass',1:'Run'}
    prediction_play = prediction_dict[raw_prediction]

# change background based on which play is predicted
    if prediction_play == 'Pass':
        url = 'https://i.imgur.com/yFeF801.jpg'
    else:
        url = 'https://i.imgur.com/ga8y1hJ.jpg'

# return results html with prediction
    return render_template('results.html', prediction=prediction_play,
                            pass_probability=round(pass_probability*100,2),
                            run_probability=round(run_probability*100,2),
                            url=url)

if __name__ == '__main__':
    app.run(debug=True)
