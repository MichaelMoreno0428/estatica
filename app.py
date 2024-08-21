import streamlit as st

def main():
    st.title("Mi aplicación Streamlit gratuita")
    nombre = st.text_input("Ingresa tu nombre")
    if nombre:
        st.write(f"Hola, {nombre}! Bienvenido a tu aplicación Streamlit gratuita.")
    numero = st.slider("Elige un número", 0, 100)
    st.write(f"El número que elegiste es: {numero}")

if __name__ == "__main__":
    main()