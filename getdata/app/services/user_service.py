from app.models.user import User
from app.extensions import db


class UserService:
    @staticmethod
    def userLog(name):
        user = User.query.filter_by(name=name).all()
        return user

    def getArea(name):
        user=User.query.filter_by(name=name).first()
        # print(user.area)
        return user.area

    @staticmethod
    def getFixer():
        user=User.query.filter_by(power=0).all()

        # print(user.area)
        return [{"name": row.name, "phonenum": row.phonenum,"area": row.area} for row in user]

    @staticmethod
    def registerPerson(data):
        new_user = User(
            name=data['name'],
            password=data['password'],
            power=0,  # 默认权限为 'user'
            area=data['area'],
            phonenum=data['phonenum']
        )
        db.session.add(new_user)
        db.session.commit()
        return "success"
    # 其他业务方法..