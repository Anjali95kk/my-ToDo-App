import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    if st.session_state["new_todo"] == "":
        pass
    else:
        todo = st.session_state["new_todo"] +"\n"
        todos.append(todo)
        functions.write_todos(todos)


st.title("My ToDo App")
st.subheader("This is my todo app!")
st.write("This app is to increase your productivity")


for i,item in enumerate(todos,start =0):
    checkbox = st.checkbox(item, key = item)
    if checkbox:
        print(i)
        print(item)
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()

st.text_input(label = "Enter a ToDo:", placeholder ="Add a new todo.....",
              on_change = add_todo, key="new_todo")

st.session_state
