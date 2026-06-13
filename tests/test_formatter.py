from src.utils.formatter import (
    format_discipline,
    format_location,
    format_contact,
    format_not_found,
    format_unknown,
)

DISCIPLINE = {
    "nome": "Banco de Dados",
    "codigo": "COMP001",
    "professor": "Prof. João Silva",
    "sala": "Lab 1",
    "horarios": ["Seg 10h-12h", "Qua 10h-12h"],
}

LOCATION = {
    "nome": "Secretaria",
    "localizacao": "Bloco A, térreo",
    "horario": "8h-17h",
}

CONTACT = {
    "nome": "Coordenação",
    "email": "coord@ic.ufal.br",
    "telefone": "(82) 3214-1000",
}


class TestFormatDiscipline:
    def test_contains_name(self):
        assert "Banco de Dados" in format_discipline(DISCIPLINE)

    def test_contains_professor(self):
        assert "Prof. João Silva" in format_discipline(DISCIPLINE)

    def test_contains_room(self):
        assert "Lab 1" in format_discipline(DISCIPLINE)

    def test_contains_all_schedules(self):
        result = format_discipline(DISCIPLINE)
        assert "Seg 10h-12h" in result
        assert "Qua 10h-12h" in result

    def test_missing_fields_show_na(self):
        result = format_discipline({"nome": "Test"})
        assert "N/A" in result


class TestFormatLocation:
    def test_contains_name(self):
        assert "Secretaria" in format_location(LOCATION)

    def test_contains_localizacao(self):
        assert "Bloco A" in format_location(LOCATION)

    def test_contains_horario(self):
        assert "8h-17h" in format_location(LOCATION)


class TestFormatContact:
    def test_contains_name(self):
        assert "Coordenação" in format_contact(CONTACT)

    def test_contains_email(self):
        assert "coord@ic.ufal.br" in format_contact(CONTACT)

    def test_contains_phone(self):
        assert "(82) 3214-1000" in format_contact(CONTACT)


class TestFormatNotFound:
    def test_contains_term(self):
        assert "Cálculo" in format_not_found("Cálculo")

    def test_empty_term_omits_quotes(self):
        result = format_not_found("")
        assert '""' not in result

    def test_is_non_empty(self):
        assert len(format_not_found("anything")) > 0


class TestFormatUnknown:
    def test_is_non_empty(self):
        assert len(format_unknown()) > 0

    def test_hints_at_capabilities(self):
        result = format_unknown()
        assert "disciplina" in result.lower() or "horário" in result.lower()
