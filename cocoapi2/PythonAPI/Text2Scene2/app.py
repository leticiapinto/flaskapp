from flask import Flask, render_template, request
from flask import send_from_directory, send_file

import subprocess
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      msg_ideal = 'Mike talks to the dog.,Jenny kicks the soccer ball.,The duck wants to play.'
      postfix = datetime.now().strftime("%m%d_%H%M%S")
      #msg_3rd = '1009_011030' 
      print(result)
      print(msg_ideal)
      msg_to_script =  result['sentence1']+','+result['sentence2']+','+result['sentence3']
      text_to_send = 'hola leti'
      os.system('./tools/abstract_demo.py --pretrained=abstract_final'+' "' + msg_to_script +'" "' + postfix +'"')
      hists = os.listdir('static/abstract_scene_'+postfix+'/abstract_samples/')
      hists = ['abstract_scene_'+postfix+'/abstract_samples/' + file for file in hists]
      return render_template('result.html',result = result, text_to_send = 'hi leti', hists = hists)
if __name__ == '__main__':
    app.run()
