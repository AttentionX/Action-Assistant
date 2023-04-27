# Search for api and find from documentation
# Find the explanation, examples of the k most relevant api
# Request for additional explanation or clarity if needed

def getInstructions(keyword):
    instruction = f'''
    Convert the following command into a valid {keyword} command. Security is very important, if more information is needed or clarity is needed, please request for additional information. Don't make any gusses or assumptions. Be very careful to follow the user's intentions exactly. Don't be discouraged to ask for help, additional information, or clarity. 
    If you have are not requesting for more information or clarification, you must only return the git command and nothing else. If you are unsure, ask the user to choose among the most relevant options (do not list all, just the options that appear to be the most relevant)
    If you are requesting for more information or clarification, start your response with "Request: " and then the request for more information or clarification.
    '''

    prompt_instruction = f'''
    Convert the following command into a valid {keyword} command. Only return the {keyword} command with no other information or characters!
    '''
    return instruction, prompt_instruction