def format_discipline(discipline: dict) -> str:
    schedules = "\n".join(f"  • {h}" for h in discipline.get("horarios", []))
    return (
        f"📚 *{discipline['nome']}*\n"
        f"Código: `{discipline.get('codigo', 'N/A')}`\n"
        f"Professor: {discipline.get('professor', 'N/A')}\n"
        f"Sala: {discipline.get('sala', 'N/A')}\n"
        f"Horários:\n{schedules}"
    )


def format_location(location: dict) -> str:
    return (
        f"📍 *{location['nome']}*\n"
        f"Localização: {location.get('localizacao', 'N/A')}\n"
        f"Horário de funcionamento: {location.get('horario', 'N/A')}"
    )


def format_contact(contact: dict) -> str:
    return (
        f"📞 *{contact['nome']}*\n"
        f"E-mail: {contact.get('email', 'N/A')}\n"
        f"Telefone: {contact.get('telefone', 'N/A')}"
    )


def format_not_found(term: str) -> str:
    term_part = f' para "*{term}*"' if term else ""
    return (
        f"Não encontrei nenhum resultado{term_part}. 😕\n\n"
        "Tente perguntar de outra forma ou verifique se o nome está correto."
    )


def format_unknown() -> str:
    return (
        "Não entendi sua pergunta. 🤔\n\n"
        "Você pode me perguntar sobre:\n"
        "  • Disciplinas e horários\n"
        "  • Localização de salas e laboratórios\n"
        "  • Contatos da coordenação e secretaria"
    )
