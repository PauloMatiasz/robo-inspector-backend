mover_doc = {
    "tags": ["Robô"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "direcao": {
                        "type": "string",
                        "example": "frente"
                    }
                },
                "required": ["direcao"]
            }
        }
    ],
    "responses": {
        200: {
            "description": "Movimento executado com sucesso"
        },
        400: {
            "description": "Falta de direção no sistema "
        },
        500: {
            "description": "Robô nao esta comunicando com o sistema "
        }
    }
}