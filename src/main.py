#Importations 
from rdflib import Graph
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from style import apply_style

# Charger l'image du logo
def load_logo(window):
    # Charger l'image à partir d'un fichier local
    image = Image.open('bus.jpg')

    # Réduire la taille de l'image si nécessaire
    image = image.resize((100, 100), Image.ANTIALIAS)

    # Convertir l'image en image Tkinter
    logo = ImageTk.PhotoImage(image)

    # Créer un label pour l'image
    logo_label = tk.Label(window, image=logo)
    logo_label.image = logo  # Conserver une référence à l'image
    logo_label.pack(pady=10)  # Afficher l'image

# Fonction pour exécuter une requête SPARQL et retourner les résultats sous forme de liste
def execute_sparql_query(g, query):
    results = g.query(query)
    return list(results)

#Definition des fontions pour faire des requêtes
def display_category():
    query = """
    SELECT DISTINCT ?category ?individual WHERE {
        ?individual a ?category .
    }
    """
    # Exécution de la requête SPARQL
    results = execute_sparql_query(g, query)

    # Création de la fenêtre Tkinter
    window = tk.Toplevel()
    window.title("Toutes les catégories")
    window.geometry("800x400")

    # Création du widget de tableau pour afficher les résultats
    table = ttk.Treeview(window)
    table["columns"] = ("individual", "category")
    table.column("#0", width=0, stretch=tk.NO)
    table.column("individual", anchor=tk.W, width=200)
    table.column("category", anchor=tk.W, width=150)
    table.heading("#0", text="", anchor=tk.W)
    table.heading("individual", text="Individual", anchor=tk.W)
    table.heading("category", text="Category", anchor=tk.W)

    # Ajout des résultats au tableau
    for i, result in enumerate(results):
        individual = str(result.individual).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        category = str(result.category).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        table.insert("", tk.END, text=str(i+1), values=(individual, category))

    # Affichage du tableau
    table.pack(fill=tk.BOTH, expand=True)

    # Fonction de fermeture de la fenêtre
    def close_window():
        window.destroy()

    # Bouton de fermeture
    close_button = ttk.Button(window, text="Close", command=close_window)
    close_button.pack(pady=10)

def display_transport_prices():
    query = """
    SELECT ?journey ?transportMode ?price ?duration ?distance ?carbonEmission WHERE {
      ?journey rdf:type transport:Journey .
      ?journey transport:hasTransportMode ?transportMode .
      ?journey transport:cost ?price .
      ?journey transport:duration ?duration .
      ?journey transport:distance ?distance .
      ?journey transport:carbonEmission ?carbonEmission .
    }
    """
    # Exécution de la requête SPARQL
    results = execute_sparql_query(g, query)

    # Création de la fenêtre Tkinter
    window = tk.Toplevel()
    window.title("Prix Transports")
    window.geometry("800x400")

    # Création du widget de tableau pour afficher les résultats
    table = ttk.Treeview(window)
    table["columns"] = ("journey", "transportMode", "price", "duration", "distance", "carbonEmission")
    table.column("#0", width=0, stretch=tk.NO)
    table.column("journey", anchor=tk.W, width=200)
    table.column("transportMode", anchor=tk.W, width=150)
    table.column("price", anchor=tk.W, width=100)
    table.column("duration", anchor=tk.W, width=100)
    table.column("distance", anchor=tk.W, width=100)
    table.column("carbonEmission", anchor=tk.W, width=100)
    table.heading("#0", text="", anchor=tk.W)
    table.heading("journey", text="Journey", anchor=tk.W)
    table.heading("transportMode", text="Transport Mode", anchor=tk.W)
    table.heading("price", text="Price", anchor=tk.W)
    table.heading("duration", text="Duration", anchor=tk.W)
    table.heading("distance", text="Distance", anchor=tk.W)
    table.heading("carbonEmission", text="Carbon Emission", anchor=tk.W)

    # Ajout des résultats au tableau
    for i, result in enumerate(results):
        journey = str(result.journey).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        transport_mode = str(result.transportMode).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        price = str(result.price)
        duration = str(result.duration)
        distance = str(result.distance)
        carbon_emission = str(result.carbonEmission)
        table.insert("", tk.END, text=str(i+1), values=(journey, transport_mode, price, duration, distance, carbon_emission))

    # Affichage du tableau
    table.pack(fill=tk.BOTH, expand=True)

    # Fonction de fermeture de la fenêtre
    def close_window():
        window.destroy()

    # Bouton de fermeture
    close_button = ttk.Button(window, text="Close", command=close_window)
    close_button.pack(pady=10)
    
def display_cheapest_transport_prices():
    # Requête SPARQL pour récupérer les trajets avec les prix les moins chers
    query = """
    SELECT ?journey ?transportMode ?price WHERE {
      ?journey rdf:type transport:Journey .
      ?journey transport:hasTransportMode ?transportMode .
      ?journey transport:cost ?price .
      FILTER NOT EXISTS {
        ?journey transport:cost ?cheaperPrice .
        ?cheaperJourney rdf:type transport:Journey .
        ?cheaperJourney transport:hasTransportMode ?transportMode .
        ?cheaperJourney transport:cost ?cheaperPrice .
        FILTER (?cheaperPrice < ?price)
      }
    }
    """

    # Exécution de la requête SPARQL
    results = execute_sparql_query(g, query)

    # Création de la fenêtre Tkinter
    window = tk.Toplevel()
    window.title("Le transport le moins cher")
    window.geometry("600x400")

    # Création du widget de tableau pour afficher les résultats
    table = ttk.Treeview(window)
    table["columns"] = ("journey", "transportMode", "price")
    table.column("#0", width=0, stretch=tk.NO)
    table.column("journey", anchor=tk.W, width=200)
    table.column("transportMode", anchor=tk.W, width=200)
    table.column("price", anchor=tk.W, width=100)
    table.heading("#0", text="", anchor=tk.W)
    table.heading("journey", text="Journey", anchor=tk.W)
    table.heading("transportMode", text="Transport Mode", anchor=tk.W)
    table.heading("price", text="Price", anchor=tk.W)

    # Ajout des résultats au tableau
    for i, result in enumerate(results):
        journey = str(result.journey).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        transport_mode = str(result.transportMode).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        price = str(result.price)
        table.insert("", tk.END, text=str(i+1), values=(journey, transport_mode, price))

    # Affichage du tableau
    table.pack(fill=tk.BOTH, expand=True)

    # Fonction de fermeture de la fenêtre
    def close_window():
        window.destroy()

    # Bouton de fermeture
    close_button = ttk.Button(window, text="Close", command=close_window)
    close_button.pack(pady=10)

def display_least_polluting_transport():
    # Requête SPARQL pour récupérer le moyen de transport le moins polluant avec son prix
    query = """
    SELECT ?transportMode ?carbonEmission ?price WHERE {
      ?journey rdf:type transport:Journey .
      ?journey transport:hasTransportMode ?transportMode .
      ?journey transport:carbonEmission ?carbonEmission .
      ?journey transport:cost ?price .
    }
    GROUP BY ?transportMode ?carbonEmission ?price
    ORDER BY ASC(?carbonEmission)
    LIMIT 1
    """

    # Exécution de la requête SPARQL
    results = execute_sparql_query(g, query)

    # Récupération du résultat
    if results:
        transport_mode = str(results[0].transportMode).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        carbon_emission = str(results[0].carbonEmission)
        price = str(results[0].price)
        message = f"Le transport le moins polluant est le(a) {transport_mode} avec une emission carbonne de {carbon_emission} et un prix de {price}. Valider."

        # Affichage du message dans une boîte de dialogue
        messagebox.showinfo("Transport moins polluant", message)
    else:
        # Affichage d'un message d'erreur si aucun résultat n'est trouvé
        messagebox.showerror("Error", "No data found.")

def choose_transport():
    #Créer une nouvelle fenetre pour afficher le transport 
    transport_window = tk.Toplevel()
    transport_window.title("Choisi votre transport")
    transport_window.geometry("400x300")

    # Menu déroulant pour chaque element 
    global transport_mode_combobox  # Variable globale 
    transport_mode_label = ttk.Label(transport_window, text="Mode de transport:")
    transport_mode_label.pack(pady=10)
    transport_mode_combobox = ttk.Combobox(transport_window, values=get_transport_modes(), state="readonly")
    transport_mode_combobox.pack(pady=5)

    # Button pour afficher 
    display_info_button = ttk.Button(transport_window, text="Afficher les infos", command=display_transport_info)
    display_info_button.pack(pady=10)

def get_transport_modes():
    query = """
    SELECT DISTINCT ?transportMode WHERE {
        ?journey rdf:type transport:Journey .
        ?journey transport:hasTransportMode ?transportMode .
    }
    """
    results = execute_sparql_query(g, query)
    transport_modes = [str(result.transportMode).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "") for result in results]
    return transport_modes

def display_transport_info():
    global transport_mode_combobox
    transport_mode = transport_mode_combobox.get()

    query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX transport: <http://www.semanticweb.org/mael2/ontologies/2023/4/transport#>

    SELECT ?journey ?price ?duration ?distance ?carbonEmission WHERE {
      ?journey rdf:type transport:Journey .
      ?journey transport:hasTransportMode transport:%s .
      ?journey transport:cost ?price .
      ?journey transport:duration ?duration .
      ?journey transport:distance ?distance .
      ?journey transport:carbonEmission ?carbonEmission .
    }
    """ % transport_mode

    # Executer la requête SPARQL
    results = execute_sparql_query(g, query)

    info_window = tk.Toplevel()
    info_window.title("Transport Info")
    info_window.geometry("400x300")

    # Créer des labels 
    info_frame = ttk.LabelFrame(info_window, text="Information Transport")
    info_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Configurer le style
    style = ttk.Style()
    style.configure("TLabelframe", background="white")
    style.configure("TLabelframe.Label", font=("Arial", 12, "bold"))

 # Afficher les informations 
    if results:
        journey = str(results[0].journey).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        price = str(results[0].price)
        duration = str(results[0].duration)
        distance = str(results[0].distance)
        carbon_emission = str(results[0].carbonEmission)

# Créer des labels pour chaque

        journey_label = ttk.Label(info_frame, text="Transport: ")
        journey_label.grid(row=0, column=0, sticky=tk.W)
        journey_value = ttk.Label(info_frame, text=journey)
        journey_value.grid(row=0, column=1, sticky=tk.W)

        price_label = ttk.Label(info_frame, text="Prix: ")
        price_label.grid(row=1, column=0, sticky=tk.W)
        price_value = ttk.Label(info_frame, text=price)
        price_value.grid(row=1, column=1, sticky=tk.W)

        duration_label = ttk.Label(info_frame, text="Durée: ")
        duration_label.grid(row=2, column=0, sticky=tk.W)
        duration_value = ttk.Label(info_frame, text=duration)
        duration_value.grid(row=2, column=1, sticky=tk.W)

        distance_label = ttk.Label(info_frame, text="Distance: ")
        distance_label.grid(row=3, column=0, sticky=tk.W)
        distance_value = ttk.Label(info_frame, text=distance)
        distance_value.grid(row=3, column=1, sticky=tk.W)

        carbon_emission_label = ttk.Label(info_frame, text="Emission carbone: ")
        carbon_emission_label.grid(row=4, column=0, sticky=tk.W)
        carbon_emission_value = ttk.Label(info_frame, text=carbon_emission)
        carbon_emission_value.grid(row=4, column=1, sticky=tk.W)

 # Configurer le style des labels
        style.configure("TLabel", background="white", font=("Arial", 10))

    else:
        error_label = ttk.Label(info_frame, text="Aucune information saisie.")
        error_label.grid(row=0, column=0, padx=20, pady=20)
        style.configure("TLabel", background="white", font=("Arial", 12, "bold"), foreground="red")

    close_button = ttk.Button(info_window, text="Close", command=info_window.destroy)
    close_button.pack(pady=10)

    if results:
        journey = str(results[0].journey).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        price = str(results[0].price)
        duration = str(results[0].duration)
        distance = str(results[0].distance)
        carbon_emission = str(results[0].carbonEmission)
    else:
        messagebox.showerror("Error", "Aucune information a été trouvée.")

def open_sparql_window():
    # Créer une nouvelle fenêtre pour les requêtes SPARQL
    sparql_window = tk.Toplevel()
    sparql_window.title("SPARQL Queries")
    sparql_window.geometry("600x400")

    # Cadre pour la requête SPARQL
    sparql_queries_frame = ttk.LabelFrame(sparql_window, text="Requêtes SPARQL")
    sparql_queries_frame.pack(pady=10, fill=tk.BOTH)

    sparql_query_text = tk.Text(sparql_queries_frame, height=5)
    sparql_query_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

    # Fonction pour exécuter la requête SPARQL
    def execute_sparql():
        query = sparql_query_text.get("1.0", tk.END).strip()
        results = execute_sparql_query(g, query)
        sparql_result_text.delete("1.0", tk.END)
        for result in results:
            sparql_result_text.insert(tk.END, str(result) + "\n")

    execute_button = ttk.Button(sparql_queries_frame, text="Exécuter", command=execute_sparql)
    execute_button.pack(pady=5)

    # Cadre pour le résultat de la requête SPARQL
    sparql_result_frame = ttk.LabelFrame(sparql_window, text="Résultat requête SPARQL")
    sparql_result_frame.pack(pady=10, fill=tk.BOTH)

    sparql_result_text = tk.Text(sparql_result_frame, height=10)
    sparql_result_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)


# Chargement des données RDF
g = Graph()
g.parse("transport.rdf", format="xml")

# Création de la fenêtre principale
window = tk.Tk()
window.title("EcoTrip")
window.geometry("400x300")
window.configure(background='white')

# Charger le logo
load_logo(window)

# Création du conteneur principal
container = ttk.Frame(window)
container.pack(fill=tk.BOTH, expand=True)

# Appliquer le style
apply_style()

# Création des boutons pour afficher les tables

button_width = 20 

transport_prices_button = ttk.Button(container, text="Prix transports", width=button_width, command=display_transport_prices)
transport_prices_button.pack(pady=10)

least_polluting_transport_button = ttk.Button(container, text="Moins polluant",width=button_width, command=display_least_polluting_transport)
least_polluting_transport_button.pack(pady=10)

transport_categories_button = ttk.Button(container, text="Catégories", width=button_width, command=display_category)
transport_categories_button.pack(pady=10)

choose_transport_button = ttk.Button(container, text="Choose Transport",width=button_width, command=choose_transport)
choose_transport_button.pack(pady=10)

sparql_button = ttk.Button(container, text="SPARQL", width=button_width, command=open_sparql_window)
sparql_button.pack(pady=10)

# Boucle principale de l'interface graphique
window.mainloop()

