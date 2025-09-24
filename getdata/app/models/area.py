from app.extensions import db
import base64

class Districts(db.Model):
    __tablename__ = 'districts'

    id = db.Column(db.Integer, primary_key=True)
    district_name = db.Column(db.String(80), unique=True, nullable=False)
    center_longitude = db.Column(db.String(255), nullable=True)
    center_latitude = db.Column(db.String(255), nullable=True)
    # 添加其他字段...

    def to_dict(self):
        return {
            'id': self.id,
            'district_name':self.district_name,
            'center_longitude':self.center_longitude,
            'center_latitude':self.center_latitude
            # 其他字段...
        }

class Points(db.Model):
    __tablename__ = 'points'

    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String(255), nullable=True)
    longitude = db.Column(db.String(255), nullable=True)
    latitude = db.Column(db.String(255), nullable=True)
    state = db.Column(db.String(255), nullable=True)
    pic = db.Column(db.LargeBinary(16777216))

    # 添加其他字段...

    def to_dict(self):
        return {
            'id': self.id,
            'district':self.district,
            'longitude':self.longitude,
            'latitude':self.latitude,
            'state':self.state,
            'pic': base64.b64encode(self.pic).decode('utf-8') if self.pic else None
            # 其他字段...
        }