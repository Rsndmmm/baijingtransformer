# coding=utf-8
import time

import flask
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/upload', methods=['POST', 'GET'])  # 添加路由
def upload():
    if request.method == 'POST':
        aoligei = request.form['aoligei']
        # aoligei_list = aoligei.split('')
        res = ''
        for i in aoligei:
            if i not in [" ",",", ".", ".", "。", "？", "!", "，", "?", "！", ":", "：", """'""", '''"''']:
                i = i + '儿'
            res = res + i
        baijinghua = res

        return render_template('upload_ok.html', val1=time.time(), res_list=baijinghua)

    return render_template('upload.html')


app.run(host='0.0.0.0', port=81, debug=True, use_reloader=False)
