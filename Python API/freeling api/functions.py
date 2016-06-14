
__author__ = 'Andrei Mihai'
from subprocess import run, PIPE

"""
 ---- ANALYZE ----
"""
def analyze(text_input, analyzer_options):

    input_to_file(text_input)
    option_string = create_options_string(analyzer_options)
    # run("analyze " + option_string+ "--output json <input.txt >json.txt", universal_newlines=True, shell=True)
    json_output = run("analyze " + option_string+ "--output json <input.txt", stdout = PIPE, universal_newlines=True, shell=True)
    return json_output.stdout

def input_to_file(text_input):
    """

    :param text_input:
    :return:
    """
    file = open("input.txt",'w')
    file.write(text_input)
    file.close()

def create_options_string(options):
    """

    :param options:
    :return:
    """

    # Language
    string = "-f "
    if options.language == "en":
        string += "en.cfg "
    elif options.language == "es":
        string += "es.cfg "

    # Output
    string += "--outlv "
    if options.output_type == "morfo":
        string += "morfo "
    elif options.output_type == "tagged":
        string += "tagged "

    # other options
    if not options.numr: string += "--nonumb "
    if not options.dtr: string += "--nodate "
    if not options.qrp: string += "--noquant "
    if not options.ner: string += "--noner "
    if options.output_type == "tagged" and options.nec: string += "--nec "
    if not options.mwd: string += "--noloc "
    if options.phe: string += "--phon "

    return string

# Test the connection with freeling
# options = Options("morfo","en",True,True,True,True,True,True,True)
# out = analyze("Have a test from us. No, really. Here it is.",options)
# print (out)

