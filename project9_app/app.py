from flask import Flask, jsonify, request, render_template
from kmp import *

app = Flask(__name__)

# Read the SARS-COV2 genome and store it
with open("sars-cov-2-genome.fasta", "r") as f:
    genome = "".join(line.strip() for line in f.readlines()[1:])

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/seq", methods=['GET', 'POST'])
def sequence():
    # get the sequence from the request
    if request.method == 'POST':
        sequence = request.form['sequence']
       # get the short nucleotide from the request data 
        sequence = sequence.upper()
       # check if the input is correct
        if short_seq_check(sequence):
            occurrences, occ_number = kmp(sequence, genome)

            results_dict = {'Input sequence': sequence,
                    'Occurrences': occurrences.tolist(),
                    'Number of occurrences': occ_number}

            return jsonify (results_dict)
        
        else:
            return make_response('Error! The input must be a nucleotide sequence')

             

if __name__ == "__main__":
    app.run()

