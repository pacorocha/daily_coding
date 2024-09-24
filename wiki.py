import requests
import json
import sys
import os
import re
import dewiki

WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"  # Mude para "pt" se preferir resultados em português

def clean_search_term(search_term):
    """
    Limpa o termo de busca, removendo espaços e caracteres inválidos.
    """
    return re.sub(r'\s+', '_', search_term.strip())

def make_wikipedia_request(search_term, lang="en"):
    """
    Faz uma requisição à API da Wikipedia para buscar o conteúdo de uma página.
    """
    params = {
        "action": "query",
        "format": "json",
        "prop": "revisions",
        "rvprop": "content",
        "titles": search_term,
        "redirects": 1,  # Seguir redirecionamentos automaticamente
        "formatversion": 2
    }

    try:
        response = requests.get(WIKIPEDIA_API_URL, params=params)
        response.raise_for_status()  # Levanta exceções para códigos de status HTTP errados
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição HTTP: {e}")
        return None

def process_wikipedia_response(data):
    """
    Processa a resposta JSON da API da Wikipedia, extraindo o conteúdo e removendo formatação Wiki.
    """
    try:
        pages = data.get('query', {}).get('pages', [])
        if not pages or 'missing' in pages[0]:
            return None

        content = pages[0].get('revisions', [])[0].get('content', '')
        return dewiki.from_string(content)  # Remove a formatação Wiki
    except (KeyError, IndexError) as e:
        print(f"Erro ao processar os dados: {e}")
        return None

def save_to_file(search_term, content):
    """
    Salva o conteúdo buscado em um arquivo com o nome formatado "nome_da_busca.wiki".
    """
    file_name = clean_search_term(search_term) + '.wiki'
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Resultado salvo em: {file_name}')

def main():
    """
    Função principal que coordena a busca, tratamento de erros e salvamento do resultado.
    """
    if len(sys.argv) < 2:
        print("Erro: Nenhum termo de busca foi fornecido.")
        sys.exit(1)

    search_term = " ".join(sys.argv[1:])

    # Etapa 1: Fazer requisição à API da Wikipédia
    response_data = make_wikipedia_request(search_term)

    if not response_data:
        print(f"Erro: Não foi possível obter dados para '{search_term}'.")
        sys.exit(1)

    # Etapa 2: Processar o conteúdo retornado pela API
    content = process_wikipedia_response(response_data)

    if not content:
        print(f"Erro: Nenhum resultado encontrado para '{search_term}'.")
        sys.exit(1)

    # Etapa 3: Salvar o conteúdo em um arquivo
    save_to_file(search_term, content)

if __name__ == "__main__":
    main()
