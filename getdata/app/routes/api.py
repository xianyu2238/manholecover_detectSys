import argparse
import sys

from flask import Blueprint, jsonify,request
from app.services.user_service import UserService
from app.services.area_service import AreaService
from app.services.task_service import TaskService
import base64
import os

api_bp = Blueprint('api1', __name__)


@api_bp.route('/userLog', methods=['POST'])
def userLog():
    data=request.get_json()
    name=data["username"]
    password=data["password"]
    users = UserService.userLog(name)

    res=0
    if users==[]:
        res=2
    else:
        dic = [user.to_dict() for user in users]
        # 成功 区分身份
        if password==dic[0]["password"]:
            if dic[0]["power"]==0:
                res=0
            else:
                res=1
        else:
            res=2
    return jsonify({
        'status': 'success',
        'data': res
    })

@api_bp.route('/getArea', methods=['POST'])
def getArea():
    data = request.get_json()
    name=data["name"]
    # print(name)
    area=UserService.getArea(name)
    return jsonify({
        'status': 'success',
        'data': area
    })

@api_bp.route('/getMap', methods=['POST'])
def getMap():
    data = request.get_json()
    district=data["district"]
    res=AreaService.getMap(district)
    # print(center.center_longitude)
    return jsonify({
        'status': 'success',
        # 'data':"1"
        'data':{
            'longitude':res.center_longitude,
            'latitude':res.center_latitude
        }
    })

@api_bp.route('/getPoints', methods=['POST'])
def getPoints():
    data = request.get_json()
    points=AreaService.getPoints(data['district'])
    points_data = [point.to_dict() for point in points]
    return jsonify({
        'status': 'success',
        # 'data':"1"
        'data':points_data
    })


@api_bp.route('/getErrorArea',methods=["get"])
def getErroArea():
    data=AreaService.getErroArea()
    return jsonify({
        'status': 'success',
        'data':data
    })


@api_bp.route('/getFixTask',methods=['POST'])
def getFixTask():
    data = request.get_json()
    res=TaskService.getFixTask(data['district'])
    return jsonify({
        'status': 'success',
        'data':res
    })

@api_bp.route('/getAllTask',methods=['get'])
def getAllTask():
    res=TaskService.getAllTask()
    return jsonify({
        'status': 'success',
        'data':res
    })

@api_bp.route('/getAllFixer',methods=['get'])
def getAllFixer():
    res=UserService.getFixer()
    return jsonify({
        'status': 'success',
        'data':res
    })

@api_bp.route('/registerPerson',methods=['POST'])
def registerPerson():
    data = request.get_json()
    res=UserService.registerPerson(data)
    return jsonify({
        'status': 'success',
        'data':res
    })

@api_bp.route('/getTaskProgress',methods=['POST'])
def getTaskProgress():
    data = request.get_json()
    res=TaskService.getTaskProgress(data['taskId'])
    image_base64 = base64.b64encode(res.progress).decode('utf-8')
    return jsonify({
        'status': 'success',
        'data':image_base64
    })

@api_bp.route('/publishTask',methods=['POST'])
def publishTask():
    data = request.get_json()
    res=TaskService.publishTask(data)
    return jsonify({
        'status': 'success',
        'data':res
    })

# submitPoint
@api_bp.route('/submitPoint',methods=['POST'])
def submitPoint():
    data = request.get_json()
    res=AreaService.submitPoint(data)
    return jsonify({
        'status': 'success',
        'data':res
    })

@api_bp.route('/submitTask',methods=['POST'])
def submitTask():
    data = request.get_json()
    res=TaskService.submitTask(data)
    return jsonify({
        'status': 'success',
        'data':"1"
    })

@api_bp.route('/checkTask',methods=['POST'])
def checkTask():
    data = request.get_json()
    res=TaskService.checkTask(data)
    return jsonify({
        'status': 'success',
        'data':res
    })