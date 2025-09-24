from app.extensions import db
import base64

class Tasks(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    taskType = db.Column(db.String(255), nullable=True)
    hole = db.Column(db.Integer, primary_key=False,nullable=True)
    taskDetail = db.Column(db.String(255), nullable=True)
    state = db.Column(db.Integer, primary_key=False)
    progress = db.Column(db.LargeBinary(16777216))
    district = db.Column(db.String(255), nullable=True)
    # 添加其他字段...

    def to_dict(self):
        return {
            'id': self.id,
            'taskType':self.taskType,
            'hole':self.hole,
            'taskDetail':self.taskDetail,
            'state': self.state,
            'progress': self.progress,
            'district': self.district,
            # 其他字段...
        }
