import json
def contar_elementos_json(json_str):
    try:
        data = json.loads(json_str)
        if isinstance(data, list):
            return len(data)
        else:
            print("El JSON no es una lista.")
            return 0
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
        return 0