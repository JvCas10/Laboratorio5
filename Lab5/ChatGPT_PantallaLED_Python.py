import openai
from pyfirmata import Arduino, util, STRING_DATA

port='COM1'

def askGPT(text):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 150,
    )
    respuesta = response.choices[0].text
    print(respuesta)

    val = respuesta[2:18]
    val2 = respuesta[18:31]
    

    board=Arduino(port)
    if True:
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(val))
        board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(val2))
    
def main():
    if True:
        myQn = "Dame una recomendacion para cuando hay un objeto muy cerca del sensor ultrasonico en 20 caracteres o menos"
        askGPT(myQn)
        print('\n')    

main()