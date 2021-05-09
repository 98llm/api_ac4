from flask import Flask, jsonify, request


app = Flask(__name__)

usuarios = [{"id": e,
             "nome": "Usuario "+str(e),
             "senha": str(e + 1),
             "idade": str(e + 2)}
            for e in range(1, 11)]

usuario = {"id": 12,
           "nome": 'Aluno',
           "senha": "impacta",
           "idade": 25}

usuarios.append(usuario)


@app.route("/usuarios", methods=['GET'])
def get():
    return jsonify(usuarios)


@app.route("/usuarios/<int:id>", methods=['GET'])
def get_one(id):
    filtro = [e for e in usuarios if e["id"] == id]
    if filtro:
        return jsonify(filtro[0])
    else:
        return jsonify({})


@app.route("/usuarios", methods=['POST'])
def post():
    global usuarios
    try:
        content = request.get_json()
        # gerar id auto
        ids = [e["id"] for e in usuarios]
        if ids:
            nid = max(ids) + 1
        else:
            nid = 1
        content["id"] = nid
        usuarios.append(content)
        return jsonify({"status": "OK",
                        "msg": "usuario adicionado com sucesso"})
    except Exception as ex:
        return jsonify({"status": "ERRO", "msg": str(ex)})


@app.route("/usuarios/<int:id>", methods=['DELETE'])
def delete(id):
    global usuarios
    try:
        usuarios = [e for e in usuarios if e["id"] != id]
        return jsonify({"status": "OK",
                        "msg": "disciplina removida com sucesso"})
    except Exception as ex:
        return jsonify({"status": "ERRO", "msg": str(ex)})


if __name__ == "__main__":
    app.run()
