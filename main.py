# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import openai
import hjson
import streamlit as st
import os
import subprocess
from editorconfig import OPENAI_API_KEY

def main():
    st.title('Code Generator by Lauren McGuire')
st.write('''
This is a code generation program that takes in natural language text and converts it to programming language commands. Built by Lauren McGuire with love
''')
st.write('Select the programming language you want to generate to:')
language = st.selectbox('', ('Python', 'C#', 'JavaScript', 'Go', 'Perl', 'PHP', 'Ruby', 'Swift', 'TypeScript', 'SQL', 'Shell'))

openai.api_key = OPENAI_API_KEY


input_text = st.text_area('Enter your question')




if st.button('Submit'):

    response = openai.Completion.create(
      model="code-davinci-002",
      temperature=.4,
      max_tokens=6500,
      prompt=language + " " + input_text,
      top_p=1,
      frequency_penalty=.4,
      presence_penalty=.3
    )

    hjson.dump(response, open("response.json", "w"))

    res=response['choices'][0]['text']

    st.code(res)

    if st.button("Run"):
      st.code("Running...")
      st.code(subprocess.run([res], shell=True))

if st.button("Restart"):
  st.write("Restarted...")
  os.system("python main.py")


#hide the streamlit logo



__name__ = "main"
if __name__ == "__main__":
  main()

