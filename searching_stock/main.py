import os
from crypt import methods
from turtle import title
from searching_stock import app
from flask import render_template, request, redirect, url_for

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests


#トップページ
@app.route('/')
def index():
    img_path = '../images/stock.png'
    return render_template(
        'index.html',
        image_path=img_path
    )


#検索ボタン押下時の処理
@app.route('/register', methods=['POST'])
def register():
    
    stock_name = request.form['stock_name']
    
    if stock_name != '':
        symbol = stock_name
        api_key = os.environ['ALPHA_VANTAGE_KEY']
        url = 'https://www.alphavantage.co/query?'\
            f'function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
        data = requests.get(url).json()
        
        daily_data = dict(reversed(data['Time Series (Daily)'].items()))
        date_list = daily_data.keys()
        close_list = [float(x['4. close']) for x in daily_data.values()]
        
        fig, axes = plt.subplots(figsize=(12, 4))
        axes.plot(date_list, close_list)
        axes.xaxis.set_major_locator(mdates.DayLocator(interval=15))
        fig.savefig('searching_stock/images/stock.png')
    
    return redirect(url_for('index'))