import streamlit as st
import pandas as pd

# Function to chat with XLSX files
def chat_with_xlsx(file_path):
    df = pd.read_excel(file_path)
    st.write(df.head())  # Display the first few rows of the file
    
    st.write("What would you like to do with this file?")
    action = st.selectbox("Select an action", options=["Filter rows", "Sort rows", "Display columns"])
    
    if action == "Filter rows":
        col = st.selectbox("Select a column to filter by", options=df.columns)
        value = st.text_input("Enter a value to filter")
        
        filtered_df = df[df[col] == value]
        st.write(filtered_df)
        
    elif action == "Sort rows":
        col = st.selectbox("Select a column to sort by", options=df.columns)
        
        sort_order = st.selectbox("Select a sort order", options=["Ascending", "Descending"])
        ascending = sort_order == "Ascending"
        
        sorted_df = df.sort_values(by=col, ascending=ascending)
        st.write(sorted_df)
        
    elif action == "Display columns":
        columns = st.multiselect("Select columns to display", options=df.columns)
        columns_df = df[columns]
        st.write(columns_df)

# Function to ask a question
def ask_question():
    question = st.text_input("Ask a question")
    
    if question:
        # You can add your custom logic here to generate a response to the user's question
        # For example, you could use a natural language processing (NLP) model to generate responses.
        response = "You asked: " + question  # Replace this with your actual response logic
        st.write("Response:", response)

def main():
    st.title("Chat with XLSX Files")
    file_path = st.file_uploader("Upload a file", type=["xlsx"])
    
    if file_path is not None:
        chat_with_xlsx(file_path)
    
    ask_question()  # Call the function to ask a question

if __name__ == "__main__":
    main()
