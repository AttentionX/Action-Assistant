def getWebsite(query, assistant):
    prompt = 'What is website I can visit to perform the following task? Refer to the examples below?'
    examples = '''
    Task: I want to order food from doordash
    Website: https://www.doordash.com/
    Task: cgv에서 영화 예약할게
    Website: https://www.cgv.co.kr/
    '''
    api_prompt = f"""{prompt}-----{examples}\n-----\nTask: {query}\nWebsite: """
    return assistant.chat(api_prompt)

def bestOption(query, options, assistant):
    prompt = "Which of the following options is the most relevant option to accomplish the given instruction? If you are unsure, ask the user to choose among the most relevant options (do not list all, just the options that appear to be the most relevant)"