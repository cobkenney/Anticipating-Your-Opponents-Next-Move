# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Anticipating your Opponent's Next Move
## Predicting Pass vs. Run in the NFL

### Problem Statement
Can we predict whether or not an offense will run or pass on a given play in the NFL?

### Executive Summary
Wouldn't it be great if you could anticipate your opponent's move? Picture this: You're an NFL Defensive Coordinator. It's Week 16. You need to win this game in order to go to the playoffs. It's the 4th Quarter. 1 minute left in the game. You're up by a touchdown. Your opponent has the ball at midfield. It's 3rd and 2. What are they going to call? This project aims to use the circumstances of a play to predict pass or run. A pass is defined as a forward pass, and a run includes lateral passes/backward passes. The project does not address punts, field goals, kickoffs, and no plays.  The project took form in 5 main steps: Data Collection & Aggregation, Data Cleaning, Exploratory Data Anlaysis, Feature Engineering, and Modeling. The final model was able to achieve 70.6% accuracy in predicting play type versus a baseline accuracy of 57.8%. The final model was simplified and stored for a flask app that takes a scenario and predicts play type.

### Contents of Repo
* [Code](https://git.generalassemb.ly/cobkenney/DSI-Assignments/tree/master/Capstone/code)
* [Data](https://git.generalassemb.ly/cobkenney/DSI-Assignments/tree/master/Capstone/datasets)
* [Flask App](https://git.generalassemb.ly/cobkenney/DSI-Assignments/tree/master/Capstone/app)

### Data Dictionary

|Feature|Type|Description|
|-|-|-|
|**week**|*int*|Week of Game (1-17)|
|**yardline_100**|*int*|Yards to Opponent's Endzone|
|**quarter_seconds_remaining**|*int*|Seconds remaining in quarter|
|**half_seconds_remaining**|*int*|Seconds remaining in half|
|**game_seconds_remaining**|*int*|Seconds remaining in game|
|**drive**|*int*|Numeric drive number in the game|
|**qtr**|*int*|Quarter of the game|
|**down**|*int*|The down for the given play|
|**goal_to_go**|*int*|Binary indicator for whether or not the posteam is in a goal down situation|
|**ydstogo**|*int*|Numeric yards in distance from either the first down marker or the endzone in goal down situations|
|**posteam_timeouts_remaining**|*int*|Number of timeouts remaining for the possession team|
|**defteam_timeouts_remaining**|*int*|Number of timeouts remaining for the team on defense|
|**score_differential**|*int*|Score differential between the posteam and defteam at the start of the play|
|**wp**|*int*|Estimated win probabiity for the posteam given the current situation at the start of the given play.|
|**dome**|*int*|Binary indicator if game was played in a dome or not|
|**temp_range_Cold**|*int*|Binary indicator if temperature is less than 45 degrees farenheit|
|**temp_range_Moderate**|*int*|Binary indicator if temperature is between 46 and 70 degrees farenheit|
|**precipitation**|*int*|Binary indicator if forecast involved rain, snow, or fog|
|**posteam_home**|*int*|Binary indicator if possession team is home or not|
|**run_tendency**|*int*|Rolling average of % run plays for past 5 plays|
|**pass_tendency**|*int*|Rolling average of % pass plays for past 5 plays|
|**down_short**|*int*|Binary interaction term for down of play and yards to go less than 4 yards|
|**down_medium**|*int*|Binary interaction term for down of play and yards to go between 4 and 7 yards|
|**down_long**|*int*|Binary interaction term for down of play and yards to go greater than 7 yards|
|**Poss_team**|*int*|Binary indicator if a given team is in possession|
|**Def_team**|*int*|Binary indicator if a given team is on defense|

### Key Takeaways & Next Steps

Down was the most import feature in predicting play type, but quarter, seconds remaining, yardline, yards to go, and score differential were also strong predictors of play types. The model had the highest accuracy when predicting third and fourth down (excluding non-pass and non-run plays) versus first and second down, the fourth quarter and second quarter versus the first and third quarter, and long plays versus short plays.

Next steps include refining the Flask App that takes inputs and outputs a plat type prediction. I could try to scrape for live play circumstances and give odds for a play type. My only reservation would be how quickly play circumstances are updated - if the play circumstances are not updated quickly, a user could know the result of the play before the source for the scrape does. Additionally, I would like to see more data on who is actually on the field for a play. Specific players could potentially indicate what play is going to be called. Finally, next steps will also include trying to predict direction of a play (right, left, middle) as well as play type.

