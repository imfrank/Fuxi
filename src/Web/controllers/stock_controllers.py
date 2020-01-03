from flask import Flask,render_template,Blueprint

blueprint_dayquotes = Blueprint('dayquotes', __name__,template_folder='templates')

@blueprint_dayquotes.route('/dayquotes')
def Index():
     """日行情
    This is using docstrings for specifications.
    ---
    parameters:
      - name: code
        in: path
        type: string     
        required: true
        default: ""
    
    responses:
      200:
        description: miaoshu
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
     return   render_template("hello.html")