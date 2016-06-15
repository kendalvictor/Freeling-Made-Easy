from flask import request
from Options import Options
from dict2table import dict2table
from functions import analyze
from json import decoder, loads

__author__ = 'Andrei Mihai'
from flask import Flask

app = Flask(__name__)

text = ""

#http://localhost:5000/freeling/analyze/tagging/en/1/1/1/1/1/1/1
@app.route('/freeling/analyze/<string:output_type>/<string:language>/<int:numr>/<int:dtr>/<int:qrp>/<int:ner>/<int:nec>/<int:mwd>/<int:phe>', methods=['GET'])
def get_analysis(output_type,language,numr,dtr,qrp,ner,nec,mwd,phe):
    # output_type can be "tagging" or "morfo"
    # language can be "en" - for english or "es" - for spanish
    # for all the rest 0 means False and something else means True

    # get the output from freeling
    options = Options(output_type, language, numr, dtr, qrp, ner, nec, mwd, phe)
    json_output = analyze(text, options)

    # dict = loads(json_output)
    # html_table = dict2table(dict)
    # parse the outpu
    # parsed = parse(output, options)

    #return the json with the result
    return json_output

#http://localhost:5000/freeling/text
@app.route('/freeling/text', methods=['POST'])
def post_text():
    global text
    json = request.json
    text = json["text"]
    return "Sucsessfully uploaded text."

if __name__ == '__main__':
    app.run(debug=True)