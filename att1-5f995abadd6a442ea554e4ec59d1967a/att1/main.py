from pathlib import Path
from src.principal import TextProcessor

def main():
    # Configuração robusta de caminhos
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / "data"
    DATA_DIR.mkdir(exist_ok=True)  # Cria a pasta se não existir
    
    file_path = DATA_DIR / "exemplo.txt"
    
    try:
        # Verificação explícita do arquivo
        if not file_path.exists():
            raise FileNotFoundError(
                f"Crie o arquivo '{file_path}' com texto para processamento!\n"
                f"Local esperado: {file_path.absolute()}"
            )
        
        # Processamento
        processor = TextProcessor(file_path)
        processor.read_file()
        
        print("="*50)
        print(f"{processor}\n")
        
        print("[1] Palavras começando com 'a':")
        print(processor.filter_words_starting_with('a'))
        
        print("\n[2] Datas encontradas:")
        print(processor.extract_dates())
        
        print("\n[3] Texto com dados sensíveis ocultos:")
        print(processor.hide_sensitive_info()[:300] + "...")
        
        print("\n" + "="*50)
        
    except Exception as e:
        print(f"\nERRO: {e}\n")
        print(" Erro durante a execução do programa." )
        print(" Possíveis causas:")
        print(" 1 O arquivo não foi encontrado ou o caminho está incorreto.")
        print(" 2 O arquivo não contém texto ou está vazio.")
        print(" 3 Problemas de permissão para ler o arquivo.")
        print(" 4 Problemas de codificação ao ler o arquivo.")
        print(" 5 O arquivo não está no formato esperado.")
        print(" 6 O arquivo não contém dados sensíveis para ocultar.")
        print(" Possíveis soluções:")
        print(" 1 Verifique se o arquivo 'exemplo.txt' está na pasta 'data'.")
        print(" 2 Verifique se o arquivo contém texto válido.")
        print(" 3 Verifique as permissões do arquivo.")
        print(" 4 Veja se o nome do arquivo está correto e se o caminho é válido.")

if __name__ == "__main__":
    main()