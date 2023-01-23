import streamlit as st
import functions


tasks = functions.get_task()


def add_task():
    todo = st.session_state["new_todo"]
    tasks.append(todo + "\n")
    functions.write_task(tasks)
    st.session_state["new_todo"] = ""


st.title("The To Do App")
st.subheader("Let's make you organized")
st.write("Your things To Do")
for index, task in enumerate(tasks):
    checked = st.checkbox(task, key=task)
    if checked:
        tasks.pop(index)
        functions.write_task(tasks)
        del st.session_state[task]
        st.experimental_rerun()


st.text_input(label="New Task", placeholder="Add your task..",
              on_change=add_task, key="new_todo", label_visibility="hidden")
