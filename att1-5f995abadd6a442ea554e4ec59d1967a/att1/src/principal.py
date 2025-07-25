import re
from typing import List
from pathlib import Path

class TextProcessor:
    """
    Classe para processamento de textos com expressões regulares.
    Versão robusta com tratamento de erros e caminhos absolutos.
    """
    
    def __init__(self, file_path: str | Path) -> None:
        self.file_path = Path(file_path).absolute()
        if not self.file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.file_path}")
        self.content = ""
    
    def __str__(self) -> str:
        return f"Processador de: '{self.file_path.name}' ({len(self.content)} caracteres)"
    
    def read_file(self) -> None:
        """Lê o arquivo com tratamento de encoding"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.content = file.read()
        except UnicodeDecodeError:
            with open(self.file_path, 'r', encoding='latin-1') as file:
                self.content = file.read()

    def filter_words_starting_with(self, letter: str) -> List[str]:
        """Filtra palavras por letra inicial (case insensitive)"""
        pattern = re.compile(rf'\b[{letter.lower()}{letter.upper()}]\w*\b')
        return pattern.findall(self.content)
    
    def filter_words_containing(self, letter: str) -> List[str]:
        """Filtra palavras que contêm a letra em qualquer posição"""
        pattern = re.compile(rf'\b\w*[{letter.lower()}{letter.upper()}]\w*\b')
        return pattern.findall(self.content)
    
    def replace_commas_with_dots(self) -> str:
        """Substitui vírgulas por pontos"""
        return self.content.replace(',', '.')
    
    def extract_dates(self) -> List[str]:
        """Extrai datas nos formatos DD/MM/AAAA ou DD-MM-AAAA"""
        pattern = re.compile(r'\b\d{2}[/-]\d{2}[/-]\d{4}\b')
        return pattern.findall(self.content)
    
    def hide_sensitive_info(self) -> str:
        """Ofusca e-mails, CPFs e telefones"""
        text = re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', '[EMAIL]', self.content)
        text = re.sub(r'\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b', '[CPF]', text)
        text = re.sub(r'\(?\d{2}\)?[\s-]?\d{4,5}[\s-]?\d{4}\b', '[TELEFONE]', text)
        return text