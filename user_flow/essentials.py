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

def steps(task):
    examples = f'''
    Objective: "Book a movie ticket for this weekend"
    I need to perform the following steps:
    1. 
    '''
    prompt = f'''
    Possible Actions:
    1. Ask user for more information
    2. Visit a website
    3. Click a button on a website
    4. Fill out a text form on a website
    5. Finished

    Objective: "{task}"
    In order to accomplish the objective , need to perform the following steps in order:
    
    '''