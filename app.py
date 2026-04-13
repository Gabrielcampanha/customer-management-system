from flask import Flask, request, jsonify
from crud import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# TESTE
@app.route('/')
def home():
    return "API rodando!"

# CREATE
@app.route('/customers', methods=['POST'])
def create():
    data = request.json

    nome = data.get('nome')
    idade = data.get('idade')

    if not nome or not idade:
        return jsonify({'erro': 'O nome e a idade são obrigatórios!'}), 400

    create_customer(nome, idade)
    return jsonify({'mensagem': 'Cliente criado com sucesso!'}), 201

# READ
@app.route('/customers', methods=['GET'])
def read():
    customers = get_customers()
    return jsonify(customers)

# RANGE
@app.route('/customers/range', methods=['GET'])
def get_range():
    id_inicio = request.args.get('inicio')
    id_fim = request.args.get('fim')

    if not id_inicio or not id_fim:
        return jsonify({'erro': 'Parâmetros inicio e fim são obrigatórios!'}), 400

    if not id_inicio.isdigit() or not id_fim.isdigit():
        return jsonify({'erro': 'IDs devem ser números!'}), 400

    id_inicio = int(id_inicio)
    id_fim = int(id_fim)

    if id_inicio > id_fim:
        return jsonify({'erro': 'Intervalo inválido!'}), 400

    customers = get_customers_by_range(id_inicio, id_fim)

    return jsonify(customers)

# UPDATE
@app.route('/customers/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    idade = data.get('idade')

    if not idade:
        return jsonify({'erro': 'A idade é obrigatória!'}), 400

    update_customer(id, idade)
    return jsonify({'mensagem': 'Cliente atualizado!'})

# DELETE
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete(id):
    delete_customer(id)
    return jsonify({'mensagem': 'Cliente deletado!'})

# CLEAR
@app.route('/customers/clear', methods=['DELETE'])
def clear():
    clear_table()
    return jsonify({'mensagem': 'Tabela limpa!'})

# MULT POST
@app.route('/customers/bulk', methods=['POST'])
def create_bulk():
    data = request.json

    if not isinstance(data, list):
        return jsonify({'erro': 'envie uma lista de clientes'}), 400

    # validação básica
    for c in data:
        if 'nome' not in c or 'idade' not in c:
            return jsonify({'erro': 'todos os clientes precisam de nome e idade'}), 400

    create_customers_bulk(data)

    return jsonify({'mensagem': f'{len(data)} clientes inseridos com sucesso'}), 201

#IMPORTAR EXCEL
@app.route('/customers/upload', methods=['POST'])
def upload_excel():
    from flask import request, jsonify
    import pandas as pd

    if 'file' not in request.files:
        return jsonify({'erro': 'arquivo não enviado'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'erro': 'arquivo inválido'}), 400

    df = pd.read_excel(file)

    clientes = df.to_dict(orient='records')

    create_customers_bulk(clientes)

    return jsonify({'mensagem': f'{len(clientes)} clientes importados com sucesso'})

#EXPORTAR EXCEL
@app.route('/customers/export', methods=['GET'])
def export_excel():
    import pandas as pd
    from flask import send_file
    import io

    customers = get_customers()

    df = pd.DataFrame(customers)

    output = io.BytesIO()
    df.to_excel(output, index=False)

    output.seek(0)

    return send_file(
        output,
        download_name="clientes.xlsx",
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)
print(request.content_type)