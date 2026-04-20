import requests

class TriviaClient:

    API_URL = "https://opentdb.com/api.php"

    def get_questions(self, amount=5, category=None, difficulty=None, qtype="multiple"):
        """
        Obtiene preguntas desde la API Open Trivia DB.

        :param amount: Número de preguntas
        :param category: ID de categoría (opcional)
        :param difficulty: dificultad (easy, medium, hard) opcional
        :param qtype: tipo de pregunta (multiple o boolean)
        :return: lista de preguntas o None si falla
        """
        params = {
            "amount": amount,
            "type": qtype
        }

        if category:
            params["category"] = category

        if difficulty:
            params["difficulty"] = difficulty

        try:
            response = requests.get(self.API_URL, params=params)
            data = response.json()

            # response_code 0 = OK
            if data.get("response_code") != 0:
                return None

            return data.get("results", [])

        except Exception as e:
            print("Error al obtener preguntas:", e)
            return None
