
import streamlit as st

def create_counter(counter):
    if f'count_{counter["title"]}' not in st.session_state:
        st.session_state[f'count_{counter["title"]}'] = counter["initValue"]

    def increment_counter():
        st.session_state[f'count_{counter["title"]}'] += 1

    def decrement_counter():
        if st.session_state[f'count_{counter["title"]}'] > 0:
            st.session_state[f'count_{counter["title"]}'] -= 1

    def reset():
        st.session_state[f'count_{counter["title"]}'] = 0

    cols = st.columns([1, 1, 1, 1])
    with cols[0]:
        st.button("-", on_click=decrement_counter, disabled=st.session_state[f'count_{counter["title"]}'] == 0, key=f"dec_{counter['title']}")
    with cols[1]:
        st.write(f"{counter['title']} ({counter['initValue']})")
        st.write(st.session_state[f'count_{counter["title"]}'], key=f"count_{counter['title']}")
    with cols[2]:
        st.button("+", on_click=increment_counter, key=f"inc_{counter['title']}")
    with cols[3]:
        st.button('Reset', on_click=reset, key=f"reset_{counter['title']}")

counters = [
    {
        "title": "Counter 1",
        "initValue": 10
    },
    {
        "title": "Counter 2",
        "initValue": 20
    },
    {
        "title": "Counter 3",
        "initValue": 30
    },
    {
        "title": "Counter 4",
        "initValue": 40
    },
    {
        "title": "Counter 5",
        "initValue": 50
    }
]

for counter in counters:
    create_counter(counter)
    st.markdown("###")

def reset_all():
    for counter in counters:
        st.session_state[f'count_{counter["title"]}'] = counter["initValue"]

st.write("Sum: ", sum(st.session_state[f'count_{counter["title"]}'] for counter in counters))
st.button("Reset All", on_click=reset_all)