from ... import

...
from ... import

...
from ... import

...


class ControladorSistemaEmpresas():

    def __init__(self):
        self.__empresas = []

    '''
    Permite incluir uma empresa utilizando a EmpresaDAO. 
    Valida pelo CNPJ se a empresa ja esta cadastrada
    @param empresa objeto Empresa que sera incluido
    @throws EmpresaDuplicadaException Excecao gerada quando se
    tenta incluir uma empresa com CNPJ ja cadastrado
    '''

    def inclui_empresa(self, empresa: Empresa):
        pass

    '''
    Permite excluir uma empresa cadastrada na EmpresaDAO
    @param empresa empresa que sera excluida
    '''

    def exclui_empresa(self, empresa: Empresa):
        pass

    '''
    Permite buscar uma empresa na lista de empresas pelo CNPJ
    @param cnpj numero do CNPJ da empresa desejada
    @return retorna None se a empresa nao for encontrada
    '''

    def busca_empresa_pelo_cnpj(self, cnpj: int) -> Empresa:
        pass

    '''
    Retorna a lista de empresas cadastradas
    @return lista de empresas cadastradas
    '''

    @property
    def empresas(self) -> list:
        return self.__empresas

    '''
    Calcula o total de impostos de todas as empresas.
    Invoca a operacao total_impostos() de cada uma
    das empresas cadastradas no Dicionario, somando os resultados
    @return somatorio dos impostos de todas as empresas cadastradas
    '''

    def calcula_total_impostos(self) -> float:
        pass
