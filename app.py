import streamlit as st


def main():
    st.title("Prosta aplikacja Streamlit")
    user_input = st.text_input("Wpisz coś:")
    if st.button("Echo"):
        st.write(f"Wprowadziłeś: {user_input}")


if __name__ == "__main__":
    main()
