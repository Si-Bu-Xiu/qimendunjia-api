from flask import Flask, request, jsonify
from qimendunjia.feipan import feipan_zirun
from qimendunjia.mingfa import mingfa_qimen
from qimendunjia.bazi import bazi_paipan, xinpai_paipan, ziwei_paipan

app = Flask(__name__)


@app.route('/api/feipan', methods=['POST'])
def api_feipan():
    """
    飞盘置闰法排盘接口。

    请求参数:
        year (int): 年份
        month (int): 月份
        day (int): 日期
        hour (int): 小时（0-23）
        location (str, optional): 出生地，用于真太阳时校准

    响应:
        JSON 排盘结果，包含 true_solar_time 字段说明是否经过真太阳时校准
    """
    data = request.get_json()
    year = data.get('year')
    month = data.get('month')
    day = data.get('day')
    hour = data.get('hour')
    location = data.get('location', '')

    try:
        result = feipan_zirun(year, month, day, hour, location)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/mingfa', methods=['POST'])
def api_mingfa():
    """
    鸣法奇门排盘接口。

    请求参数:
        year (int): 年份
        month (int): 月份
        day (int): 日期
        hour (int): 小时（0-23）
        location (str, optional): 出生地，用于真太阳时校准

    响应:
        JSON 排盘结果，包含 true_solar_time 字段说明是否经过真太阳时校准
    """
    data = request.get_json()
    year = data.get('year')
    month = data.get('month')
    day = data.get('day')
    hour = data.get('hour')
    location = data.get('location', '')

    try:
        result = mingfa_qimen(year, month, day, hour, location)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/bazi', methods=['POST'])
def api_bazi():
    data = request.get_json()
    year = data.get('year')
    month = data.get('month')
    day = data.get('day')
    hour = data.get('hour')
    gender = data.get('gender', '男')
    location = data.get('location', '')
    
    try:
        result = bazi_paipan(year, month, day, hour, gender, location)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/xinpai', methods=['POST'])
def api_xinpai():
    data = request.get_json()
    year = data.get('year')
    month = data.get('month')
    day = data.get('day')
    hour = data.get('hour')
    gender = data.get('gender', '男')
    location = data.get('location', '')
    
    try:
        result = xinpai_paipan(year, month, day, hour, gender, location)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/ziwei', methods=['POST'])
def api_ziwei():
    data = request.get_json()
    year = data.get('year')
    month = data.get('month')
    day = data.get('day')
    hour = data.get('hour')
    gender = data.get('gender', '男')
    location = data.get('location', '')
    
    try:
        result = ziwei_paipan(year, month, day, hour, gender, location)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200


import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
