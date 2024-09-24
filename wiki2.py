import requests
from bs4 import BeautifulSoup
import sys
import time

WIKIPEDIA_BASE_URL = "https://en.wikipedia.org"
PHILOSOPHY_TITLE = "Philosophy"

def clean_title(title):
    """
    Remove espaços extras e normaliza o título.
    """
    return title.strip().capitalize()

def get_first_valid_link(soup):
    """
    Encontra o primeiro link válido em uma página da Wikipedia.
    - Ignora links em itálico, entre parênteses e links que não levem a novos artigos.
    """
    content_div = soup.find(id="mw-content-text")

    if content_div is None:
        return None

    for paragraph in content_div.find_all('p', recursive=True):
        for link in paragraph.find_all('a', recursive=True):
            # Verifica se o link está em um parágrafo válido e não está em itálico ou entre parênteses
            if link.find_parent('i') is None and '(' not in link.text and ')' not in link.text:
                href = link.get('href')
                if href and href.startswith("/wiki/") and ':' not in href:
                    return WIKIPEDIA_BASE_URL + href

    return None

def fetch_wikipedia_page(url):
    """
    Faz a requisição para a URL da Wikipedia e retorna o conteúdo da página.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro HTTP
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}. Unable to continue.")
        sys.exit(1)

def main():
    """
    Função principal que coordena o processo de encontrar o caminho até a Filosofia.
    """
    if len(sys.argv) < 2:
        print("Erro: Nenhuma palavra de busca foi fornecida.")
        sys.exit(1)

    search_term = "_".join(sys.argv[1:])
    search_url = f"{WIKIPEDIA_BASE_URL}/wiki/{search_term}"

    visited_articles = set()
    current_url = search_url
    article_count = 0

    while True:
        soup = fetch_wikipedia_page(current_url)
        title = soup.find(id="firstHeading").text

        clean_title_name = clean_title(title)
        print(clean_title_name)
        article_count += 1

        if clean_title_name == PHILOSOPHY_TITLE:
            print(f"{article_count} roads from {search_term.replace('_', ' ')} to philosophy!")
            break

        if current_url in visited_articles:
            print("It leads to an infinite loop!")
            break

        visited_articles.add(current_url)

        next_link = get_first_valid_link(soup)
        if not next_link:
            print("It leads to a dead end!")
            break

        current_url = next_link

        # Pausa para evitar sobrecarregar o servidor da Wikipedia
        time.sleep(1)

if __name__ == "__main__":
    main()
