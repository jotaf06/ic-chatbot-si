import pytest
from src.data.search import search_discipline, search_location, search_contact

SAMPLE_DATA = {
    "disciplinas": [
        {
            "nome": "Banco de Dados",
            "codigo": "COMP001",
            "professor": "Prof. João Silva",
            "sala": "Lab 1",
            "horarios": ["Seg 10h-12h"],
            "aliases": ["BD", "database"],
        },
        {
            "nome": "Estrutura de Dados",
            "codigo": "COMP002",
            "professor": "Profa. Maria Souza",
            "sala": "Sala 204",
            "horarios": ["Ter 14h-16h"],
            "aliases": ["ED"],
        },
    ],
    "locais": [
        {"nome": "Secretaria", "localizacao": "Bloco A, térreo", "horario": "8h-17h"},
        {"nome": "Lab 1", "localizacao": "Bloco A, sala 010", "horario": "7h-22h"},
    ],
    "contatos": [
        {"nome": "Coordenação", "email": "coord@ic.ufal.br", "telefone": "(82) 3214-1000"},
    ],
}


class TestSearchDiscipline:
    def test_finds_by_exact_name(self):
        result = search_discipline(SAMPLE_DATA, "Banco de Dados")
        assert result["nome"] == "Banco de Dados"

    def test_finds_by_partial_name(self):
        result = search_discipline(SAMPLE_DATA, "banco")
        assert result["nome"] == "Banco de Dados"

    def test_finds_by_alias(self):
        result = search_discipline(SAMPLE_DATA, "BD")
        assert result["nome"] == "Banco de Dados"

    def test_finds_by_alias_case_insensitive(self):
        result = search_discipline(SAMPLE_DATA, "bd")
        assert result["nome"] == "Banco de Dados"

    def test_finds_by_code(self):
        result = search_discipline(SAMPLE_DATA, "COMP002")
        assert result["nome"] == "Estrutura de Dados"

    def test_returns_none_when_not_found(self):
        result = search_discipline(SAMPLE_DATA, "Cálculo")
        assert result is None

    def test_case_insensitive_name(self):
        result = search_discipline(SAMPLE_DATA, "BANCO DE DADOS")
        assert result is not None


class TestSearchLocation:
    def test_finds_by_name(self):
        result = search_location(SAMPLE_DATA, "Secretaria")
        assert result["nome"] == "Secretaria"

    def test_finds_by_partial_name(self):
        result = search_location(SAMPLE_DATA, "lab")
        assert result["nome"] == "Lab 1"

    def test_case_insensitive(self):
        result = search_location(SAMPLE_DATA, "secretaria")
        assert result is not None

    def test_returns_none_when_not_found(self):
        result = search_location(SAMPLE_DATA, "biblioteca")
        assert result is None


class TestSearchContact:
    def test_finds_by_name(self):
        result = search_contact(SAMPLE_DATA, "Coordenação")
        assert result["email"] == "coord@ic.ufal.br"

    def test_finds_by_partial_name(self):
        result = search_contact(SAMPLE_DATA, "coord")
        assert result is not None

    def test_case_insensitive(self):
        result = search_contact(SAMPLE_DATA, "COORDENAÇÃO")
        assert result is not None

    def test_returns_none_when_not_found(self):
        result = search_contact(SAMPLE_DATA, "TI")
        assert result is None
