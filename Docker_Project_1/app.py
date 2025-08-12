from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    # Will use templates folder as default
    # add template_folder='folder_name' to use a custom folder
    # or use an absolute path; template_folder=os.path.abspath('path/to/custom_folder'))
    # print(app.template_folder) will show active template dir

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    # debug=True shouldn't be used in production -> security risk!!
    # host='0.0.0.0' to accept external connections