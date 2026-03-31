from flask import request
import os
from src.utils.ApiResponse import ApiResponse
from http import HTTPStatus
from src.domain.services.camera_service import processar_dado


class CameraController:

    def video(self):
        """
        Retorna a URL do stream de vídeo
        ---
        tags:
          - Câmera
        responses:
          200:
            description: URL do stream obtida com sucesso
        """
        stream_url = os.getenv("STREAM_URL")

        if not stream_url:
            return ApiResponse.error(
                message="URL do stream não configurada",
                code=HTTPStatus.INTERNAL_SERVER_ERROR
            )

        return ApiResponse.success(
            data={"url": stream_url},
            message="URL do stream obtida com sucesso",
            code=HTTPStatus.OK
        )

    def receber_dados(self):
        """
        Recebe e processa um valor
        ---
        tags:
        - Processamento
        parameters:
        - name: body
            in: body
            required: true
            schema:
            type: object
            required:
                - valor
            properties:
                valor:
                type: number
                example: 10
        responses:
        200:
            description: Dados processados com sucesso
            schema:
            type: object
            properties:
                success:
                type: boolean
                example: true
                data:
                type: object
                message:
                type: string
                example: Dados processados com sucesso
        400:
            description: Erro de validação
        """
        data = request.get_json()
        if not data or "valor" not in data:
            return ApiResponse.error(
                message="Campo 'valor' é obrigatório",
                code=HTTPStatus.BAD_REQUEST
            )
        valor = data["valor"]
        
        resultado = processar_dado(valor)
        
        return ApiResponse.success(
            data=resultado,
            message="Dados processados com sucesso",
            code=HTTPStatus.OK
        )