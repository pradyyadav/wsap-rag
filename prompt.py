from vector_search import retrieve_similar, client, query
import os

text_list = []



sender = "deepanshu"
receiver = "pradyumna"

text_list = retrieve_similar(client, query)


prompt_template = f"""
                Using the below context information respond to the user query.
                context: '{text_list}'
                query: '{query}'
                Response structure should look like this:
                
                # *Query response in form of JSON*

                *JSON response*
                
                Respond to the query after reading the context just like {receiver}. Consider the query is asked by {sender}. Always follow the mannerism, tone, style, language, personality of {receiver}.

                The response should contain text first and then JSON.

                Whenever you find any important details like time, place, date, create a json response, example if you find time, place and date in conversation, the json will look like below. The JSON object should look like this limited with 3 backticks. JUST OUTPUT THE JSON, NO NEED TO INCLUDE ANY TITLE OR TEXT BEFORE IT:
                
                Else, if you don't find the details, just output the response only in text.

                'Response': * < response text > (in original language) *
                
                ```[
                    {{
                        'Time': * Time *
                        'Place': * place name *
                        'Date': * Date (translate to english) *
                    }}
                ]```

                """
if __name__=='__main__':
    print(prompt_template)
