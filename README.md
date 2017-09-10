# resposta_automatica
Permite ativar e desativar mensagens automaticas das contas de email da UOL Diveo (exchange.vcaremail.com.br)

Este módulo proporciona uma forma alternativa para ativar e desativar as respostas automáticas dos emails mantidos pela UOL Diveo (exchange.vcaremail.com.br).
Funciona através de requisições get e post utilizando-se do módulo requests.
**>>> Necessário instalar o módulo requests <<<**

Funções:

Ativar() -- Ativa as respostas automáticas*
Desativar() -- Desativa as respostas automáticas*
*As mensagens configuradas são as mesmas para os emails internos e externos

Se a função for executada com sucesso, retornará True e caso haja algum problema, retornará False.

Exemplo (Ativar resposta):
>>> import resposta_automatica
>>> tmp = RespostaAutomatica('email@email.com.br', 'senha_secreta')
>>> tmp.Ativar('Teste', '0', '1', '1', '2017', '0', '1', '2', '2017')
>>> True

Exemplo (Desativar resposta):
>>> import resposta_automatica
>>> tmp = RespostaAutomatica('email@email.com.br', 'senha_secreta')
>>> tmp.Desativar()
>>> True

Também é possível utilizar tal módulo em uma linha:
Exemplo (Ativar em uma linha):
>>> import resposta_automatica; RespostaAutomatica('email@email.com.br', 'senha_secreta').Ativar('Teste', '0', '1', '1', '2017', '0', '1', '2', '2017')
>>> True

Exemplo (Desativar em uma linha):
>>> import resposta_automatica; RespostaAutomatica('email@email.com.br', 'senha_secreta').Desativar()
>>> True

Escrito por Victor Oliveira
victor.oliveira@gmx.com
