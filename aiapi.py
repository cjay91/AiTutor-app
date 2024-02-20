import openai
import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY

prompt = 'explain data science with 3 paragraphs'


def generateChatResponse(prompt):
    messages = []
    messages.append(
        {"role": "system", "content": "You are an assistant who answers questions friendly."})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)

    # response = 'hiii'
    response = openai.ChatCompletion.create(
        model='gpt-4', messages=messages)

    try:
        answer = response['choices'][0]['message']['content']
    except:
        answer = 'wrong!'

    return answer


def generateExpandResponse(prompt):
    messages = []
    messages.append(
        {"role": "system", "content": f"Explain more about the following content. Give many facts as possible. \n\n {prompt}"})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)

    # response = 'hiii'
    response = openai.ChatCompletion.create(
        model='gpt-4', messages=messages)

    try:
        answer = response['choices'][0]['message']['content']
    except:
        answer = 'wrong!'

    return answer
