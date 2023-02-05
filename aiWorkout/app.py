from flask import Flask, render_template, request

app = Flask(__name__)
import openai

# Initialize the OpenAI API client
openai.api_key = "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"

# Define a list of keywords related to workouts
allowed_keywords = ["fitness","exercise","training","workout","lifting","weightlifting","weights","cardio","aerobic","anaerobic","strength","muscle","endurance","gym","training","yoga","pilates","run","jog","walk","swim","cycle","dumbbell","barbell","kettlebell","bodyweight","HIIT","crossfit","plyometrics","calisthenics","arms","biceps","triceps","forearms","shoulders","chest","back","lats","abs","core","stomach","legs","quads","hamstrings","calves","glutes","butt","hips"]

results = []
asks = []
# Continuously ask the user for input
def askQuestion(input):
    user_input = input

    contains_allowed_keyword = False
    for keyword in allowed_keywords:
        if keyword in user_input.lower():
            contains_allowed_keyword = True
            break
    
    # If the input does not contain any of the allowed keywords, ask the user to try again
    if not contains_allowed_keyword:
        return ("Please ask a workout-related question!")
    
    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{user_input}\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    return response

    # response = askQuestion("Give me a push pull leg schedule")
    # if request.method == "POST":
    #     response = request.formData("userInput")
    #     askQuestion(response)
    # print(response)

# Render html page with the form
# User then enters data and sends a post request
# To which I grab the users input, and store it into a variable
# I now have user input, i throw it into the chatgpt function to get result
# How do i throw result back into the same route

@app.route("/")
def index():
    return render_template('main.html')


@app.route("/result", methods = ["POST", "GET"])
def result():
    if request.method =="POST":
        response = request.form.get("userInput")
        result = askQuestion(response)
        asks.append(response)
        results.append(result)

    return render_template('result.html', length = len(asks), results = results, asks = asks)

#perhaps not needed
if __name__ == "__main__":
    app.debug = True
    app.run()









