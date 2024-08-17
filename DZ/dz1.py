import ...

app =flask(__name__)

@app.route('/')
def index():
    return render_template('index.html.xsl')

if __name__ == '__main__'
    app.run(debug=true)