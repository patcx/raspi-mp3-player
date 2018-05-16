import ntpath
import player as ply
from flask import Flask, flash, render_template, request, Response, abort
from os import listdir, stat
from os.path import isfile, join, abspath
from pwd import getpwuid
import sys
import manualController

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def play():
    id = request.args.get('id')
    print(id)
    sound = {}
    sound['-12'] = 'a1.wav'
    sound['-10'] = 'a1s.wav'
    sound['-8'] = 'b1.wav'
    sound['-7'] = 'c1.wav'
    sound['-5'] = 'c1s.wav'
    sound['-3'] = 'c2.wav'
    sound['-1'] = 'd1.wav'
    sound['0'] = 'd1s.wav'
    sound['2'] = 'e1.wav'
    sound['4'] = 'f1.wav'
    sound['5'] = 'f1s.wav'
    sound['7'] = 'g1.wav'
    sound['9'] = 'g1s.wav'
    sound['11'] = 'b1.wav'
    sound['12'] = 'c1.wav'

    ply.play('default', 'wav/' + sound[id])
    return ""

if __name__ == '__main__':
    print('Starting...')
    app.run(host='0.0.0.0', port=5000)
    print('Shutting down...')