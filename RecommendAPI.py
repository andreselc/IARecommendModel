from flask import Flask, request, jsonify
import tf_idf as modelo

app = Flask(__name__)

# @app.route('/recomendar_pelicula/<string:mi_parametro>', methods=['GET'])
# def recomendar_pelicula(mi_parametro):
#     # Aquí puedes usar el valor de 'mi_parametro' como desees
#     resultado = modelo.genre_recommendations(mi_parametro)
#     return jsonify(resultado)

@app.route('/recomendar_pelicula/<string:nombre>', methods=['GET'])
def recomendar_pelicula(nombre):
    try:
        resultado = modelo.genre_recommendations(nombre)
        resultado_dict = resultado.to_dict(orient='records')  # Convertir DataFrame a lista de diccionarios
        return jsonify(resultado_dict)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)

