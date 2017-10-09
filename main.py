from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# can also use <int:post_id> to type the parameter
@app.route('/sample/<parm>')
def show_parm_sample(parm):
    app.logger.debug('Parameter: %s' % parm)
    return 'Parameter %s' % parm

# example of VERBS
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do the login'
    else:
        return 'show the login form'



@app.errorhandler(404)
def not_found(error):
    return 'shit not found!'

if __name__ == '__main__':
    app.run()
