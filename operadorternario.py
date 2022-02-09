logged_user = True

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário não logado.'
print(msg)

print('===============**================================')

logged_user = False
msg = 'Usuario logado.' if (logged_user) else 'usuario precisa logar.'
print(msg)

print('===============**================================')


idade = input('Digite sua idade: ')

if not idade.isnumeric():
    print('Você precisa digitar apenas numeros.')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'

    print(msg)