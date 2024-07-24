import sqlite3

from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'главная'


@app.route('/about')
def about():
    import random
    return ('лураррацаиауицапвиыраипыфмавппаивпмрвыивсипвиргавимвыиапнвипавыипыипсимвпыивыипивспыныипивыисвп')
@app.route('/info')
def info():
    return 'gerfdgfdsfgewgterfwdsbfefwfbefwewdsadgtrewqdsafgerfwdsvfedsfefwdsfrewqdsadfegrewfdsvfsdvbgfdedsfb'
if __name__ == '__main__':
        app.run()