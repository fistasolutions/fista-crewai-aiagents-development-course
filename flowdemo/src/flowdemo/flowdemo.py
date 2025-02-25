from crewai.flow.flow import Flow, listen, start
from litellm import completion

API_KEY="AIzaSyD9-JTJOZe8_4arZM5j3DhbrfX03g-iHg0"

class CityFunFact(Flow):

    @start()
    def generate_random_city(self):
        print("Starting flow")
        # Each flow state automatically gets a unique ID
      #  print(f"Flow State ID: {self.state['id']}")

        response = completion(
            model= "gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[
                {
                    "role": "user",
                    "content": "Return the name of a random city in the world.",
                },
            ],
        )

        random_city = response["choices"][0]["message"]["content"]
        # Store the city in our state
        self.state["city"] = random_city
        print(f"Random City: {random_city}")

        return random_city

    @listen(generate_random_city)
    def generate_fun_fact(self, random_city):
        response = completion(
            model= "gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[
                {
                    "role": "user",
                    "content": f"Tell me a fun fact about {random_city}",
                },
            ],
        )

        fun_fact = response["choices"][0]["message"]["content"]
        # Store the fun fact in our state
        self.state["fun_fact"] = fun_fact
        return fun_fact



flow = CityFunFact()
result = flow.kickoff()

print(f"Generated fun fact: {result}")

