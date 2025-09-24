from flask import Flask
from .extensions import db, cors
from .routes.api import api_bp
from .config import Config  # 使用相对导入


def create_app(config_class=Config):  # 直接使用类而不是字符串
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 初始化扩展
    db.init_app(app)
    cors.init_app(app)

    # 注册蓝图
    # app.register_blueprint(api_bp, url_prefix='/api')

    return app