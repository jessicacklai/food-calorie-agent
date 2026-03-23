from pydantic_ai.models.groq import GroqModel
from pydantic_ai import Agent
from dotenv import load_dotenv
import tools

load_dotenv() #use with .env file(e.g. GROQ_API_KEY = xx123abc)

model = GroqModel("llama-3.1-8b-instant")

agent = Agent(
    model,
    system_prompt=(
        "You are a dieting assistant. "
        "You can log meals (use log_food) and show today's calories (get_todays_calories). "
        "Help users track their food intake and provide advice on healthy eating."
    ),
    tools=[tools.log_food, tools.get_todays_calories],
)

def main():
    history = []

    while True:
        user_input: str = input("Input: ")

        if user_input.lower() in ("exit", "quit"):
            break

        response = agent.run_sync(user_input)

        print(response.output) 

if __name__ == "__main__":
    main()