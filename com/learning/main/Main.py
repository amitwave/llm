from com.learning.openai.SimpleOpenAiClient import SimpleOpenAiClient


def main():
    openAiClient = SimpleOpenAiClient()
    response = openAiClient.invokellm("Write an essay on Paris city")
    print(response.content)

if __name__ == "__main__":
    main()