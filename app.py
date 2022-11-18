from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

""" import story instance in stories.py file so can use the attributes and methods within Story class"""
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "some key"

debug = DebugToolbarExtension(app)


"""Show form on homepage with story.prompts as the input labels"""
@app.route('/')
def show_form():
    """ set 'prompts' equal to story.prompts which is a list of words passed in when create an instance of Story ('story') in stories.py file. i.e. story = Story(['place', 'noun', 'verb', 'adjective', 'plural_noun']"""
    """render_template generates output from 'form.html file' by using 'prompts' to create html """
    return render_template('form.html', prompts = story.prompts)

  


"""/story is called when 'submit' button is clicked in form"""
@app.route('/story')
def show_story():
    """Shows the resulting story from form inputs (values of request.args)"""
    """request.args is a list of key value pairs with keys = story.prompts and values = input values from the form, i.e. request.args=[('place', 'here'), ('noun', 'toad'), ('verb', 'run'), ('adjective', 'silly'), ('plural_noun', 'cats')]"""
    
    text = story.generate(request.args)

    """render the html from the story.html file with 'msg' as the return of the story.generate method with input of a list with key/value pairs (request.args) """
    return render_template('story.html', msg = text)

  



    