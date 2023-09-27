import re
from questions import centro_paula_souza_question, saudacao
from responses import centro_paula_souza_response, saudacao_response_resume, saudacao_response_complete
from utils.remove_special_char import remove_special_characters


def message_reply(input_text, user_name):
    input_text = remove_special_characters(input_text)

    if re.search(saudacao, input_text, re.IGNORECASE):
        return f"{saudacao_response_resume}, {user_name}. {saudacao_response_complete}"

    elif re.search(centro_paula_souza_question, input_text, re.IGNORECASE):
        return f"{user_name}, {centro_paula_souza_response}"

    elif "tudo bem?" in input_text:
        return "Tudo ótimo e você?"

    else:
        return "Desculpe, não entendi!"
