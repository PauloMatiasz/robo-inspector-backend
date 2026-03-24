from flask import Blueprint, Response, request, jsonify
from services.camera_service import gerar_frames, processar_dado

camera_bp = Blueprint("camera", __name__)
# Aqui voce vai apenas expor uma CLASSE com os metodos, cada rota deve chamar o metodo que necessitar, e deve tambem instanciar o controller antes
# EX:

# class CameraController:
#     def video(self):
#         return Response(gerar_frames(),
#                         mimetype='multipart/x-mixed-replace; boundary=frame')

# deve instanciar assim la na rota = 
# camera_controller = CameraController()
# e depois usar assim na rota = 
# camera_controller.video()

#Controller tambem deve validar algumas coisas como se todos os dados obrigatorios do request estao presentes, se os dados estao no formato correto, etc...


@camera_bp.route("/video")
def video():
    return Response(gerar_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@camera_bp.route("/api/dados", methods=["POST"])
def receber():
    valor = request.json.get("valor")
    return jsonify(processar_dado(valor))
