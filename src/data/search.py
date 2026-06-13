def search_discipline(data: dict, term: str) -> dict | None:
    term = term.lower().strip()
    for discipline in data["disciplinas"]:
        targets = [discipline["nome"]] + discipline.get("aliases", []) + [discipline.get("codigo", "")]
        if any(term in t.lower() for t in targets):
            return discipline
    return None


def search_location(data: dict, term: str) -> dict | None:
    term = term.lower().strip()
    for location in data["locais"]:
        if term in location["nome"].lower():
            return location
    return None


def search_contact(data: dict, term: str) -> dict | None:
    term = term.lower().strip()
    for contact in data["contatos"]:
        if term in contact["nome"].lower():
            return contact
    return None
