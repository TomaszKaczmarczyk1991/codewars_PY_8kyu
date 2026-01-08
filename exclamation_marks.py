def remove(st):
    while st.endswith("!"):
        st = st[:-1]
    return st