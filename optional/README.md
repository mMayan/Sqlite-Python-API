# Introdução
Eu fiz este código como um desafio adicional e para aprender a usar a biblioteca Requests. Depois de criar uma API e manipulá-la utilizando o Postman, senti a necessidade de entender como fazer isso diretamente com Python.

## Tecnologias usadas
- **[Requests](https://requests.readthedocs.io/en/latest/)**
- **[Dearpygui](https://dearpygui.readthedocs.io/en/latest/about/what-why.html)**

## Como utilizar o código
Primeiramente, você precisará rodar o arquivo `routes.py` para descobrir a URL da sua API. Em seguida, vá aos arquivos `db_interaction.py` e `user_interaction.py` e altere as variáveis de URL para a sua própria, **respeitando os endpoints**. Após essa etapa, o código estará pronto para ser executado.

É importante que o `routes.py` esteja rodando para que a API permaneça ativa.

### Rodando o código

Para executar este código, o processo é semelhante ao uso da API via Postman.

1. **Acesso:** Ao abrir, serão exibidas as janelas de registro e login. Escolha a que melhor se enquadra na sua necessidade.

Após o login, você poderá utilizar as opções disponíveis, pois todas elas exigem o token de verificação gerado pelo login.

2. **Visualização:** Nesta opção, são geradas duas janelas distintas para que o usuário escolha entre visualizar os produtos cadastrados ou os usuários registrados.

3. **Inserção:** Janela dedicada ao cadastro de produtos no banco de dados.

4. **Atualização:** Esta opção abre duas janelas, uma para produtos e outra para usuários. Nos produtos, você pode alterar o preço e o estoque com base no nome. Para os usuários, é possível apenas trocar a senha, também baseada no nome do usuário cadastrado.

5. **Deletar:** Esta opção permite a exclusão de produtos ou usuários cadastrados com base no ID. Para descobrir o ID de algum item, basta retornar ao menu de *visualização* e escolher entre usuário ou produto.

6. **Limpar janelas:** Função para limpar as janelas, caso a interface fique sobrecarregada.
