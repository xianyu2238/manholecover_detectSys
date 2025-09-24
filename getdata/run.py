import argparse
import sys
from pathlib import Path

from app import create_app

from app.routes.api import api_bp as bp1
from yolov5.detect import bp as bp2

ROOT = Path(r"D:\desktop\project\getdata")  # 直接使用你的绝对路径
sys.path.insert(0, str(ROOT))

app = create_app()


parser = argparse.ArgumentParser()
parser.add_argument('--weights', nargs='+', type=str, default='yolov5/runs/train/exp3/weights/best.pt',
                    help='model.pt path(s)')
# source不需要，直接从客户端传入
# parser.add_argument('--source', type=str, default='inference/images', help='source')  # file/folder, 0 for webcam
parser.add_argument('--output', type=str, default='yolov5/output', help='output folder')  # output folder
parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
parser.add_argument('--conf-thres', type=float, default=0.25, help='object confidence threshold')
parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
parser.add_argument('--view-img', action='store_true', help='display results')
parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
parser.add_argument('--augment', action='store_true', help='augmented inference')
parser.add_argument('--update', action='store_true', help='update all models')
opt = parser.parse_args()

app.config['YOLO_OPT']=opt
#
# bp2=create_detect_blueprint(opt)

app.register_blueprint(bp1,url_prefix='/v1')
app.register_blueprint(bp2,url_prefix='/v2')
if __name__ == '__main__':
    app.run(debug=True)