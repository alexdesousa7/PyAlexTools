import requests

class TriviaClient:

    API_URL = "https://opentdb.com/api.php"

    def get_questions(self, amount=5, category=None, difficulty=None, qtype="multiple"):
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

            if data["response_code"] != 0:
                return None

            return data["results"]

        except Exception as e:
            print("Error al obtener preguntas:", e)
            return None
