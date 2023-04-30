# ##Example Selectors
def color_teller(thing):
    from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
    from langchain.vectorstores import FAISS
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.prompts import FewShotPromptTemplate, PromptTemplate
    from langchain.llms import OpenAI
    import os
    import openai 

    openai.api_key = os.environ.get("OPENAI_API_KEY")
    openaikey = openai.api_key

    llm = OpenAI(model_name = "gpt-3.5-turbo", openai_api_key = openaikey)

    example_prompt = PromptTemplate(
        input_variables = ["input", "output"],
        template = "Example Input: {input} \nExample Output: {output}",
    )

    #examples of the color of certain objects
    #this can ultimately point to a huge list of examples
    examples = [
        {"input": "orange fruit", "output": "orange"},
        {"input": "firetruck", "output": "red"},
        {"input": "cloud", "output": "white"},
        {"input": "wood", "output": "brown"},
        {"input": "steel", "output": "gray"},
        {"input": "coal", "output": "black"},
    ]

    example_selector = SemanticSimilarityExampleSelector.from_examples(
        examples,
        OpenAIEmbeddings(openai_api_key = openaikey),
        FAISS, #vectorstore class used to store embeddings; pip install faiss-cpu
        k = 2 #number of examples to produce
    )

    similar_prompt = FewShotPromptTemplate(
        #the object that will help us select examples
        example_selector = example_selector,
        #our prompt
        example_prompt = example_prompt,
        #cusotmizations that we'll add before and after
        prefix = "Give the color of the item",
        suffix = "Input: {input} \nOutput:",

        #what the input will get for the variable
        input_variables = ["input"],
    )


    output = llm(similar_prompt.format(input = thing))
    return output



test = color_teller("sky")
print(test)

exec()