from src.data.loader import load_data


def test_load_data_returns_dict():
    data = load_data()
    assert isinstance(data, dict)


def test_load_data_has_required_keys():
    data = load_data()
    assert "disciplinas" in data
    assert "locais" in data
    assert "contatos" in data


def test_disciplines_have_required_fields():
    data = load_data()
    for disc in data["disciplinas"]:
        assert "nome" in disc
        assert "aliases" in disc
        assert isinstance(disc["aliases"], list)


def test_locations_have_required_fields():
    data = load_data()
    for loc in data["locais"]:
        assert "nome" in loc
        assert "localizacao" in loc


def test_contacts_have_required_fields():
    data = load_data()
    for contact in data["contatos"]:
        assert "nome" in contact
        assert "email" in contact
