from flask import Blueprint, Response, request, jsonify
from services.camera_service import gerar_frames, processar_dado

camera_bp = Blueprint("camera", __name__)

@camera_bp.route("/video")
def video():
    return Response(gerar_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@camera_bp.route("/api/dados", methods=["POST"])
def receber():
    valor = request.json.get("valor")
    return jsonify(processar_dado(valor))