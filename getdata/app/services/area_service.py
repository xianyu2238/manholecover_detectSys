from app.models.area import Districts,Points
from app.extensions import db
from sqlalchemy import func
import base64

class AreaService:
    @staticmethod
    def getMap(district):
        district= Districts.query.filter_by(district_name=district).first()
        # print(district)
        return district

    def getPoints(district):
        points=Points.query.filter_by(district=district).all()
        return points

    @staticmethod
    def getErroArea():
        result = db.session.query(
            Points.district.label('region'),
            func.count().label('count')
        ).filter(Points.state != 'good') \
            .group_by(Points.district) \
            .order_by(func.count().desc()) \
            .all()

        return [{"name": row.region, "value": row.count} for row in result]

    @staticmethod

    def submitPoint(data):
        # 1. 获取并处理Base64图片数据
        base64_str = data['pic']
        if 'base64,' in base64_str:
            base64_str = base64_str.split('base64,')[1]

        try:
            binary_data = base64.b64decode(base64_str)
        except Exception as e:
            raise ValueError("Invalid Base64 image data")

        # 2. 查询是否存在相同经纬度的记录
        existing_point = Points.query.filter(
                Points.longitude == data['longitude'],
                Points.latitude == data['latitude']
        ).first()

        # 3. 根据查询结果决定更新或插入
        if existing_point:
            # 更新现有记录
            existing_point.state = data['state']
            existing_point.pic = binary_data
            db.session.commit()
            return "update success"
        else:
            # 插入新记录
            new_task = Points(
                district=data['region'],
                longitude=data['longitude'],
                latitude=data['latitude'],
                state=data['state'],
                pic=binary_data
            )
            db.session.add(new_task)
            db.session.commit()
            return "insert success"
    # 其他业务方法..