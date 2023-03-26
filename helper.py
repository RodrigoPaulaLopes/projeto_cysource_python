def serializeUser(user):
    return {
        'id': user.id,
        'name': user.name,
        'last_name': user.last_name,
        'date_born': user.date_born,
        "cpf": user.cpf,
        "rg": user.rg,
        "email": user.email,
        "phone": user.phone
    }