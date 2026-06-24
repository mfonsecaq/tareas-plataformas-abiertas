from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/estudiantes/api/v1/hola')
def hola():
    return jsonify({
        "mensaje": "Hola mundo"
    })

@app.route('/estudiantes/api/v1/saludo')
def saludo():
    nombre = request.args.get('nombre')

    if not nombre:
        return jsonify({
            "mensaje": "Debe de ingresar el nombre del estudiante."
        })

    return jsonify({
        "saludo": f"Hola {nombre}"
    })

if __name__ == '__main__':
    app.run(debug=True)