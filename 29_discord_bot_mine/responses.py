from difflib import get_close_matches
import json

def get_best_match(user_question: str, questions: dict) -> str | None:

    questions: list[str] = [q for q in questions]
    matches: list =get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]

def get_response(message: str, knowledge: dict) -> str:

    best_match: str | None = get_best_match(message, knowledge)

    if answer := knowledge.get(best_match):
        return answer
    else:
        return "Carapinga no te entiendo."
    
def load_knowledge(file_path: str) -> dict:

    with open(file_path, "r") as file:
        return json.load(file)
    
if __name__ == "__main__":
    test_knowledge: dict = load_knowledge("29_discord_bot_mine/knowledge.json")
    test_response: str = get_response("bye", knowledge=test_knowledge)
    print(test_response)