#Faz uma api response para padronizar o retorno das resposta, ela deve conter os seguintes campos:
# - status: "success" ou "error"
# - data: objeto com os dados da resposta (pode ser nulo em caso de erro)
# - message: mensagem de erro ou sucesso (pode ser nulo em caso de sucesso)
# - code: código de status HTTP (200, 400, 500, etc) (usar http.HTTPStatus para isso, nao usar o numero diretamente)