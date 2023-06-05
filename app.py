import streamlit as st
import requests

def search_image(keyword):
    # Votre clé d'API Pixabay
    API_KEY = "37049133-ef0bca53f1e2c2afd8d9f392d"

    # Requête à l'API Pixabay pour rechercher une image correspondant au mot-clé
    url = f"https://pixabay.com/api/?key={API_KEY}&q={keyword}&image_type=photo"
    response = requests.get(url)
    data = response.json()

    # Récupérer l'URL de l'image
    if data["hits"]:
        image_url = data["hits"][0]["webformatURL"]
        return image_url
    else:
        return None

# Interface utilisateur avec Streamlit
st.title("Recherche d'images en fonction d'un mot")
input_word = st.text_input("Entrez un mot")
if st.button("Rechercher l'image"):
    if input_word:
        image_url = search_image(input_word)
        if image_url:
            st.image(image_url, caption=input_word, use_column_width=True)
        else:
            st.warning("Aucune image trouvée pour ce mot")
    else:
        st.warning("Veuillez entrer un mot")
