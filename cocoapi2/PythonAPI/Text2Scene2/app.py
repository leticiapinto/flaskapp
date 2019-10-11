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
      postfix = datetime.now().strftime("%m%d_%H%M%S")
      #msg_3rd = '1009_011030' 
      print(result)
      option = result['sample']
      print(type(option))
      text_to_send = 'Hola Leti'
      if(int(option) == 1):
        #print(1)
        msg_to_script =  result['sentence1']+','+result['sentence2']+','+result['sentence3']
        result2 = {'Option': 'Abstract', 'Sentence 1': result['sentence1'], 'Sentence 2': result['sentence2'], 'Sentence 3': result['sentence3']}
        os.system('./tools/abstract_demo.py --pretrained=abstract_final'+' "' + msg_to_script +'" "' + postfix +'"')
        hists = os.listdir('static/abstract_scene_'+postfix+'/abstract_samples/')
        hists = ['abstract_scene_'+postfix+'/abstract_samples/' + file for file in hists]
        #result['sample'] = 'Abstract' 
      if(int(option) == 2):
        #print(2)
        msg_to_script2 = result['sentence1'] 
        result2 = {'Option': 'Layout', 'Input': result['sentence1']}
        os.system('./tools/layout_demo.py --pretrained=layout_final'+' "' + msg_to_script2 +'" "' + postfix +'"')
        hists = os.listdir('static/layout_'+postfix+'/layout_samples/')
        hists = ['layout_'+postfix+'/layout_samples/' + file for file in hists]
 
      if(int(option) == 3):
        #print(3)
        msg_to_script2 = result['sentence1']
        result2 = {'Option': 'Layout', 'Input': result['sentence1']}  
        run_system = './tools/composites_demo.py --for_visualization=True --use_super_category=True --use_patch_background=True --n_shape_hidden=256 --where_attn=2 --where_attn_2d=True --pretrained=composites_final'
        os.system( run_system +' "' + msg_to_script2 +'" "' + postfix +'"')
        hists = os.listdir('static/layout_'+postfix+'/layout_samples/')
        hists = ['layout_'+postfix+'/layout_samples/' + file for file in hists]
      
      return render_template('result.html',result = result2, text_to_send = text_to_send, hists = hists)
if __name__ == '__main__':
    app.run()
