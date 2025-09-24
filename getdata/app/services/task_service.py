from app.models.task import Tasks
from app.extensions import db
import base64
class TaskService:
    @staticmethod
    def getFixTask(district):
        # 查询 district 匹配且 state 在 [0, 1] 的任务
        result = Tasks.query.filter(
            Tasks.district == district,
            Tasks.state.in_([0, 1])  # state 是 0 或 1
        ).all()

        return [{
            "id": item.id,
            "taskType": item.taskType,
            "hole": item.hole,
            "taskDetail": item.taskDetail
        } for item in result]

    @staticmethod
    def getAllTask():
        result = Tasks.query.filter(Tasks.state != 2).all()
        return [{"id":item.id,"area": item.district, "hole": item.hole, "taskType": item.taskType} for item in result]

    @staticmethod
    def publishTask(data):
        hole = data.get('hole')
        if hole == '':  # 处理空字符串
            hole = None
        new_task = Tasks(
            district=data['area'],
            hole=hole,
            taskType=data['taskType'],
            taskDetail=data['description'],
            state=0
        )
        db.session.add(new_task)
        db.session.commit()
        return "success"

    @staticmethod
    def getTaskProgress(id):
        result = Tasks.query.filter_by(id=id).first()
        return result

    @staticmethod
    def submitTask(data):
        base64_str = data['image']
        if 'base64,' in base64_str:
            base64_str = base64_str.split('base64,')[1]

        try:
            binary_data = base64.b64decode(base64_str)
        except Exception as e:
            raise ValueError("Invalid Base64 image data")
        task = Tasks.query.get(data['taskId'])
        task.progress = binary_data  # 假设data['pic']包含progress数据
        task.state = 1
        db.session.commit()
        return "success"

    # checkTask
    @staticmethod
    def checkTask(data):
        task = Tasks.query.get(data['taskId'])
        task.state = 2
        db.session.commit()

        return "success"

    # 其他业务方法..