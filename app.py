#test 1

# import streamlit as st
# import PyPDF2
# import pandas as pd
# import numpy as np
# import google.generativeai as genai
# from sklearn.metrics.pairwise import cosine_similarity
# import textwrap

# # Set your API key
# API_KEY = 'AIzaSyCrbeU4QGZYHXR2AIAfeiko5AN8NCerQ24'  # Replace with your actual API key
# genai.configure(api_key=API_KEY)

# # Helper functions
# def embed_content(title, text, model='models/embedding-001', task_type='retrieval_document'):
#     response = genai.embed_content(model=model, content=text, task_type=task_type, title=title)
#     return response["embedding"]

# def extract_text_from_pdf(pdf_file):
#     reader = PyPDF2.PdfReader(pdf_file)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text()
#     return text

# def create_chunks(text, chunk_size=300, overlap=50):
#     words = text.split()
#     chunks = []
#     for i in range(0, len(words), chunk_size - overlap):
#         chunk = " ".join(words[i:i + chunk_size])
#         chunks.append(chunk)
#     return chunks

# def find_top_chunks(query, dataframe, top_n=3, model='models/embedding-001'):
#     query_response = genai.embed_content(model=model, content=query, task_type='retrieval_query')
#     query_embedding = query_response["embedding"]

#     document_embeddings = np.stack(dataframe['Embeddings'])
#     similarities = cosine_similarity([query_embedding], document_embeddings)[0]
#     top_indices = similarities.argsort()[-top_n:][::-1]  # Get top_n indices

#     return dataframe.iloc[top_indices]['Text'].tolist()

# def make_prompt(query, relevant_passages):
#     passages = " ".join(relevant_passages)
#     escaped = passages.replace("'", "").replace('"', "").replace("\n", " ")
#     prompt = textwrap.dedent(f"""\
#     You are a helpful and informative bot that answers questions using text from the reference passages included below. \
#     Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
#     However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
#     strike a friendly and conversational tone. \
#     If the passage is irrelevant to the answer, you may ignore it.
#     QUESTION: '{query}'
#     PASSAGES: '{escaped}'

#     ANSWER:
#     """)
#     return prompt

# # Streamlit UI
# st.title("PDF Question Answering App")

# # PDF Upload
# uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")

# if uploaded_pdf is not None:
#     # Extract text from uploaded PDF
#     document_text = extract_text_from_pdf(uploaded_pdf)

#     # Create chunks
#     chunks = create_chunks(document_text)
    
#     # Embed the chunks
#     df = pd.DataFrame(chunks, columns=['Text'])
#     df['Title'] = ['Chunk ' + str(i+1) for i in range(len(chunks))]
#     df['Embeddings'] = df.apply(lambda row: embed_content(row['Title'], row['Text']), axis=1)

#     # User Query
#     query = st.text_input("Ask a question")

#     if query:
#         # Find relevant passages
#         top_passages = find_top_chunks(query, df, top_n=3)
        
#         # Create a prompt for the generative model
#         prompt = make_prompt(query, top_passages)

#         # Get the answer from the generative model
#         model = genai.GenerativeModel('gemini-1.5-pro-latest')
#         answer = model.generate_content(prompt)

#         # Display the answer
#         st.write("Answer:", answer.text)

# test 2


# import streamlit as st
# import PyPDF2
# import pandas as pd
# import numpy as np
# import google.generativeai as genai
# from sklearn.metrics.pairwise import cosine_similarity
# import textwrap

# # Set your API key
# API_KEY = 'AIzaSyCrbeU4QGZYHXR2AIAfeiko5AN8NCerQ24'  # Replace with your actual API key
# genai.configure(api_key=API_KEY)

# # Helper functions
# def embed_content(title, text, model='models/embedding-004', task_type='retrieval_document'):
#     response = genai.embed_content(model=model, content=text, task_type=task_type, title=title)
#     return response["embedding"]

# def extract_text_from_pdf(pdf_file):
#     reader = PyPDF2.PdfReader(pdf_file)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text()
#     return text

# def create_chunks(text, chunk_size=500, overlap=50):
#     words = text.split()
#     chunks = []
#     for i in range(0, len(words), chunk_size - overlap):
#         chunk = " ".join(words[i:i + chunk_size])
#         chunks.append(chunk)
#     return chunks

# def find_top_chunks(query, dataframe, top_n=3, model='models/embedding-004'):
#     query_response = genai.embed_content(model=model, content=query, task_type='retrieval_query')
#     query_embedding = query_response["embedding"]

#     document_embeddings = np.stack(dataframe['Embeddings'])
#     similarities = cosine_similarity([query_embedding], document_embeddings)[0]
#     top_indices = similarities.argsort()[-top_n:][::-1]  # Get top_n indices

#     return dataframe.iloc[top_indices]['Text'].tolist()

# def make_prompt(query, relevant_passages):
#     passages = " ".join(relevant_passages)
#     escaped = passages.replace("'", "").replace('"', "").replace("\n", " ")
#     prompt = textwrap.dedent(f"""\
#     You are a helpful and informative bot that answers questions using text from the reference passages included below. \
#     Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
#     However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
#     strike a friendly and conversational tone. \
#     If the passage is irrelevant to the answer, you may ignore it.
#     QUESTION: '{query}'
#     PASSAGES: '{escaped}'

#     ANSWER:
#     """)
#     return prompt

# # Streamlit UI
# st.title("PDF Question Answering App")

# # PDF Upload
# uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")

# if uploaded_pdf is not None:
#     # Extract text from uploaded PDF
#     document_text = extract_text_from_pdf(uploaded_pdf)

#     # Create chunks
#     chunks = create_chunks(document_text)
    
#     # Embed the chunks
#     df = pd.DataFrame(chunks, columns=['Text'])
#     df['Title'] = ['Chunk ' + str(i+1) for i in range(len(chunks))]
#     df['Embeddings'] = df.apply(lambda row: embed_content(row['Title'], row['Text']), axis=1)

#     # Loop to ask multiple questions
#     while True:
#         query = st.text_input("Ask a question (or leave empty to stop):", key="query")

#         if query:
#             # Find relevant passages
#             top_passages = find_top_chunks(query, df, top_n=3)
            
#             # Create a prompt for the generative model
#             prompt = make_prompt(query, top_passages)

#             # Get the answer from the generative model
#             model = genai.GenerativeModel('gemini-1.5-flash-exp-0827')
#             answer = model.generate_content(prompt)

#             # Display the answer
#             st.write("Answer:", answer.text)
#         else:
#             break  # Exit loop if query is empty


# test 3

# import streamlit as st
# import PyPDF2
# import pandas as pd
# import numpy as np
# import google.generativeai as genai
# from sklearn.metrics.pairwise import cosine_similarity
# import textwrap

# # Set your API key
# API_KEY = 'AIzaSyCrbeU4QGZYHXR2AIAfeiko5AN8NCerQ24'  # Replace with your actual API key
# genai.configure(api_key=API_KEY)

# # Helper functions
# def embed_content(title, text, model='models/embedding-001', task_type='retrieval_document'):
#     response = genai.embed_content(model=model, content=text, task_type=task_type, title=title)
#     return response["embedding"]

# def extract_text_from_pdf(pdf_file):
#     reader = PyPDF2.PdfReader(pdf_file)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text()
#     return text

# def create_chunks(text, chunk_size=300, overlap=50):
#     words = text.split()
#     chunks = []
#     for i in range(0, len(words), chunk_size - overlap):
#         chunk = " ".join(words[i:i + chunk_size])
#         chunks.append(chunk)
#     return chunks

# def find_top_chunks(query, dataframe, top_n=3, model='models/embedding-001'):
#     query_response = genai.embed_content(model=model, content=query, task_type='retrieval_query')
#     query_embedding = query_response["embedding"]

#     document_embeddings = np.stack(dataframe['Embeddings'])
#     similarities = cosine_similarity([query_embedding], document_embeddings)[0]
#     top_indices = similarities.argsort()[-top_n:][::-1]  # Get top_n indices

#     return dataframe.iloc[top_indices]['Text'].tolist()

# def make_prompt(query, relevant_passages):
#     passages = " ".join(relevant_passages)
#     escaped = passages.replace("'", "").replace('"', "").replace("\n", " ")
#     prompt = textwrap.dedent(f"""\
#     You are a helpful and informative bot that answers questions using text from the reference passages included below. \
#     Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
#     However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
#     strike a friendly and conversational tone. \
#     If the passage is irrelevant to the answer, you may ignore it.
#     QUESTION: '{query}'
#     PASSAGES: '{escaped}'

#     ANSWER:
#     """)
#     return prompt

# # Streamlit UI
# st.title("PDF Question Answering App")

# # PDF Upload
# uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")

# if uploaded_pdf is not None:
#     # Extract text from uploaded PDF
#     document_text = extract_text_from_pdf(uploaded_pdf)

#     # Create chunks
#     chunks = create_chunks(document_text)
    
#     # Embed the chunks
#     df = pd.DataFrame(chunks, columns=['Text'])
#     df['Title'] = ['Chunk ' + str(i+1) for i in range(len(chunks))]
#     df['Embeddings'] = df.apply(lambda row: embed_content(row['Title'], row['Text']), axis=1)

#     # User Query
#     query = st.text_input("Ask a question")

#     if query:
#         # Find relevant passages
#         top_passages = find_top_chunks(query, df, top_n=3)
        
#         # Create a prompt for the generative model
#         prompt = make_prompt(query, top_passages)

#         # Get the answer from the generative model
#         model = genai.GenerativeModel('gemini-1.5-pro-latest')
#         answer = model.generate_content(prompt)

#         # Display the answer
#         st.write("Answer:", answer.text)


#  test 4

# from flask import Flask, render_template, request, jsonify, session
# import PyPDF2
# import pandas as pd
# import numpy as np
# import google.generativeai as genai
# from sklearn.metrics.pairwise import cosine_similarity
# import textwrap
# import os

# app = Flask(__name__)

# # Set your API key
# API_KEY = 'AIzaSyCrbeU4QGZYHXR2AIAfeiko5AN8NCerQ24'  # Replace with your actual API key
# genai.configure(api_key=API_KEY)

# # Helper functions
# def embed_content(title, text, model='models/embedding-001', task_type='retrieval_document'):
#     response = genai.embed_content(model=model, content=text, task_type=task_type, title=title)
#     return response["embedding"]

# def extract_text_from_pdf(pdf_file):
#     reader = PyPDF2.PdfReader(pdf_file)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text()
#     return text

# def create_chunks(text, chunk_size=300, overlap=50):
#     words = text.split()
#     chunks = []
#     for i in range(0, len(words), chunk_size - overlap):
#         chunk = " ".join(words[i:i + chunk_size])
#         chunks.append(chunk)
#     return chunks

# def find_top_chunks(query, dataframe, top_n=3, model='models/embedding-001'):
#     query_response = genai.embed_content(model=model, content=query, task_type='retrieval_query')
#     query_embedding = query_response["embedding"]

#     document_embeddings = np.stack(dataframe['Embeddings'])
#     similarities = cosine_similarity([query_embedding], document_embeddings)[0]
#     top_indices = similarities.argsort()[-top_n:][::-1]  # Get top_n indices

#     return dataframe.iloc[top_indices]['Text'].tolist()

# def make_prompt(query, relevant_passages):
#     passages = " ".join(relevant_passages)
#     escaped = passages.replace("'", "").replace('"', "").replace("\n", " ")
#     prompt = textwrap.dedent(f"""\
#     You are a helpful and informative bot that answers questions using text from the reference passages included below. \
#     Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
#     However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
#     strike a friendly and conversational tone. \
#     If the passage is irrelevant to the answer, you may ignore it.
#     QUESTION: '{query}'
#     PASSAGES: '{escaped}'

#     ANSWER:
#     """)
#     return prompt

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_pdf():
#     if 'pdf' not in request.files:
#         return jsonify({'error': 'No PDF uploaded.'}), 400
    
#     file = request.files['pdf']
#     document_text = extract_text_from_pdf(file)

#     # Create chunks and embed
#     chunks = create_chunks(document_text)
#     df = pd.DataFrame(chunks, columns=['Text'])
#     df['Title'] = ['Chunk ' + str(i+1) for i in range(len(chunks))]
#     df['Embeddings'] = df.apply(lambda row: embed_content(row['Title'], row['Text']), axis=1)

#     # Save dataframe as a CSV file on the server instead of using session
#     df.to_csv('dataframe.csv', index=False)

#     return jsonify({'message': 'PDF processed and embeddings created successfully.'}), 200

# @app.route('/ask', methods=['POST'])
# def ask_question():
#     # Load the CSV file back into the dataframe
#     if not os.path.exists('dataframe.csv'):
#         return jsonify({'error': 'Please upload a PDF first.'}), 400

#     df = pd.read_csv('dataframe.csv')

#     # Convert the embeddings column back to numpy arrays
#     df['Embeddings'] = df['Embeddings'].apply(eval).apply(np.array)

#     query = request.form['question']
    
#     top_passages = find_top_chunks(query, df, top_n=3)
#     prompt = make_prompt(query, top_passages)

#     model = genai.GenerativeModel('gemini-1.5-pro-latest')
#     answer = model.generate_content(prompt)
    
#     return jsonify({'answer': answer.text})

# if __name__ == '__main__':
#     app.secret_key = os.urandom(24)  # Ensure secret key is secure for production
#     app.run(debug=True)


# test 5

from flask import Flask, render_template, request, jsonify, session
import PyPDF2
import pandas as pd
import numpy as np
import google.generativeai as genai
from sklearn.metrics.pairwise import cosine_similarity
import textwrap
import os

app = Flask(__name__)

# Set your API key
API_KEY = 'AIzaSyCrbeU4QGZYHXR2AIAfeiko5AN8NCerQ24'  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# Helper functions
def embed_content(title, text, model='models/text-embedding-004', task_type='retrieval_document'):
    response = genai.embed_content(model=model, content=text, task_type=task_type, title=title)
    return response["embedding"]

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def create_chunks(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def find_top_chunks(query, dataframe, top_n=3, model='models/text-embedding-004'):
    query_response = genai.embed_content(model=model, content=query, task_type='retrieval_query')
    query_embedding = query_response["embedding"]

    document_embeddings = np.stack(dataframe['Embeddings'])
    similarities = cosine_similarity([query_embedding], document_embeddings)[0]
    top_indices = similarities.argsort()[-top_n:][::-1]  # Get top_n indices

    return dataframe.iloc[top_indices]['Text'].tolist()

def make_prompt(query, relevant_passages):
    passages = " ".join(relevant_passages)
    escaped = passages.replace("'", "").replace('"', "").replace("\n", " ")
    prompt = textwrap.dedent(f"""\
    You are a helpful and informative bot that answers questions using text from the reference passages included below. \
    Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
    However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
    strike a friendly and conversational tone. \
    Every time user asks a question, you go through all the chunks 
    If it is out of passage context then respond that it is irrelevant. \
    If the passage is irrelevant to the answer, you may ignore it.
    QUESTION: '{query}'
    PASSAGES: '{escaped}'

    ANSWER:
    """)
    return prompt

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No PDF uploaded.'}), 400
    
    file = request.files['pdf']
    document_text = extract_text_from_pdf(file)

    # Create chunks and embed
    chunks = create_chunks(document_text)
    df = pd.DataFrame(chunks, columns=['Text'])
    df['Title'] = ['Chunk ' + str(i+1) for i in range(len(chunks))]
    df['Embeddings'] = df.apply(lambda row: embed_content(row['Title'], row['Text']), axis=1)

    # Save dataframe as a CSV file on the server instead of using session
    df.to_csv('dataframe.csv', index=False)

    return jsonify({'message': 'PDF processed and embeddings created successfully.'}), 200

@app.route('/ask', methods=['POST'])
def ask_question():
    # Check if the CSV file exists
    if not os.path.exists('dataframe.csv'):
        return jsonify({'error': 'No data available. Please upload a sample first.'}), 400

    # Load the CSV file back into the dataframe
    try:
        df = pd.read_csv('dataframe.csv')
    except Exception as e:
        return jsonify({'error': f'Error reading the CSV file: {str(e)}'}), 500

    # Convert the embeddings column back to numpy arrays
    try:
        df['Embeddings'] = df['Embeddings'].apply(eval).apply(np.array)
    except Exception as e:
        return jsonify({'error': f'Error processing embeddings: {str(e)}'}), 500

    query = request.form['question']
    
    try:
        top_passages = find_top_chunks(query, df, top_n=3)
        prompt = make_prompt(query, top_passages)

        model = genai.GenerativeModel('gemini-1.5-flash')
        temperature = 0.1
        answer = model.generate_content(prompt)
    except Exception as e:
        return jsonify({'error': f'Error generating content: {str(e)}'}), 500
    
    return jsonify({'answer': answer.text})

if __name__ == '__main__':
    app.secret_key = os.urandom(24)  # Ensure secret key is secure for production
    app.run(debug=True)
