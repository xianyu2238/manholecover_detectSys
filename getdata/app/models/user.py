from app.extensions import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=True)
    phonenum = db.Column(db.String(255), nullable=True)
    power = db.Column(db.Integer, nullable=True)
    area = db.Column(db.String(255), nullable=True)
    # 添加其他字段...

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password':self.password,
            'phonenum': self.phonenum,
            'power': self.power,
            'area':self.area
            # 其他字段...
        }