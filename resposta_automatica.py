'''Este módulo proporciona uma forma alternativa para ativar e desativar as respostas automáticas dos emails mantidos pela UOL Diveo (exchange.vcaremail.com.br).
Funciona através de requisições get e post utilizando-se do módulo requests.
>>> Necessário instalar o módulo requests <<<

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

Histórico de versões:
Versão 1.0.1: Primeiro release. Adicionado orientação à objeto. Duas funções adicionadas.
Versão 1.0.0: Criado para testes internos e estudo de funcionamento, não publicado.

Versão: 1.0.1
Escrito por Victor Oliveira
victor.oliveira@gmx.com
'''
from requests import post as Post
from requests import get as Get
from re import findall as Findall

#TODO: Realizar validação de campos de email e data.
class RespostaAutomatica:
    def __init__(self, usuario, senha):
        #Tenta fazer a primeira requisição
        try:
            self.req = Post('https://exchange.vcaremail.com.br/owa/auth.owa',
                data={'destination' : 'https://exchange.vcaremail.com.br/owa/',
                    'flags' : '0',
                    'forcedownlevel' : '0',
                    'trusted' : '0',
                    'username' : usuario,
                    'password' : senha,
                    'isUtf8' : '1'},
                headers={'Cookie' : 'PBack=0'},
                allow_redirects=False)
            #A variável self.cookies contém os cookies no formato dict
            self.cookies = self.req.cookies.get_dict()
        except:
            print('Ocorreu um erro ao efetuar login. Tente novamente mais tarde')

        #Verifica se o usuário e/ou senha estão corretos.
        if self.cookies['cadata'] == None:
            print('Usuário e/ou senha incorretos.')

        #Faz uma segunda requisição para poder coletar a variável "hidcanary" dentro da página web
        #TODO: Coletar a variável "hidcanary" usando algum parser HTML
        self.req = Get('https://exchange.vcaremail.com.br/owa/', cookies=self.cookies)
        self.hidcanary = Findall('hidcanary.*"', self.req.content.decode())[0].split('"')[-2]
        self.cookies.update(self.req.cookies.get_dict())

    def Ativar(self, mensagem, hora_inicial, dia_inicial, mes_inicial, ano_inicial, hora_final, dia_final, mes_final, ano_final):
        '''Função para ativar mensagem de férias. Todos os argumentos são necessários para que a função seja executada.

        Descrição dos argumentos:

        mensagem(str) - Pode conter caracteres especiais. Para uma nova linha, digite "\n".
        hora_inicial(str ou int) - Hora inicial. Formato de 24 horas (de 0 a 23).
        dia_inicial(str ou int) - Dia inicial.
        mes_inicial(str ou int) - Mes inicial.
        ano_inicial(str ou int) - Ano inicial.
        hora_final(str ou int) - Hora final. Formato de 24 horas (de 0 a 23).
        dia_final(str ou int) - Dia final.
        mes_final(str ou int) - Mes final.
        ano_final(str ou int) - Ano final.

        Para mais ajuda e exemplos, consulte a ajuda do módulo com help(resposta_automatica)
        '''
        try:
            req = Post('https://exchange.vcaremail.com.br/owa/?ae=Options&t=Oof',
                data={'hidpnst' : '',
                    'rdoOof':  '1',
                    'chkTmd' : '',
                    'selSM' : mes_inicial,
                    'selSD' : dia_inicial,
                    'selSY' : ano_inicial,
                    'selST' : hora_inicial,
                    'selEM' : mes_final,
                    'selED' : dia_final,
                    'selEY' : ano_final,
                    'selET' : hora_final,
                    'chkInt' : '1',
                    'txtInt' : mensagem,
                    'chkExtSnd' : '',
                    'rdoAll' : '3',
                    'chkExt' : '',
                    'txtExt' : mensagem,
                    'hidcmdpst' : 'save',
                    'hidcanary' : self.hidcanary},
                cookies=self.cookies)
            return True
        except:
            return False

    def Desativar(self):
        '''Função para ativar mensagem de férias.
        Para mais ajuda e exemplos, consulte a ajuda do módulo com help(resposta_automatica)
        '''
        try:
            Post('https://exchange.vcaremail.com.br/owa/?ae=Options&t=Oof',
                data={'rdoOof':  '0',
                    'chkTmd' : '',
                    'chkInt' : '1',
                    'txtInt' : '',
                    'chkExtSnd' : '',
                    'rdoAll' : '3',
                    'chkExt' : '',
                    'txtExt' : '',
                    'hidcmdpst' : 'save',
                    'hidcanary' : self.hidcanary},
                cookies=self.cookies)
            return True
        except:
            return False
