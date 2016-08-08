# Reportagens

Esta estrutura de publicação baseada em Flask foi criada para a reportagem especial "Identidade Parcelada" da Escolda de Jornalismo/Enois.

As reportagens serão criadas como pastas dentro da pasta principal. As pastas não-reportagens (que contém outros arquivos relacionados à estrutura), para que não interfiram no carregamento das páginas, devem ser nomeadas como arquivos ocultos do unix (começando com ".") ou arquivos especiais do python (começando com "__"). O sistema vai tentar carregar como uma página (uma reportagem) qualquer pasta com nome fora desses padrões.

As reportagens são servidas em endereços no formato
  [http://dominio.principal.com/**nomedapasta**](#)
o endereço raiz do domínio assim como qualquer pasta inexistente retorna um erro 403, que pode ser usado para redirecionar para o site principal (essa estrutura foi pensada para coexistir com um site já existente com distribuição a cargo do servidor web).

As reportagens deverão ter a seguinte estrutura de pastas:

### templates
  Arquivos html que serão, de fato, a página a ser carregada.
Eles podem ter variáveis e estruturas lógicas usando a 'linguagem' de template [Jinja2](http://jinja.pocoo.org/docs/dev/templates/).

### content
  Arquivos em markdown (com extensão .md).
O conteúdo será convertido de markdown para html e inserido nos templates onde for encontrada a tag Jinja2 **{% content._nomedoarquivo_ %}**. O objetivo é prover uma forma simplificada de edição do conteúdo do site pelo github e editores similares que usam Markdown.

### data
  Similar à pasta **content**, mas abriga arquivos **json** (com a extensão .json).
Os arquivos devem obrigatoriamente conter um [objeto JSON](http://www.json.org/object.gif), contendo, claro, chaves e valores. Os valores desse dicionário serão inseridos nos templates por meio de tags do Jinja2 no formato **{% data.nomedoraquivo.chave %}**. O objetivo é permitir o uso de estruturas lógicas nos templates além de passar ao template dados gerados dinamicamente.
  
### static
  Abriga arquivos que serão acessados diretamente sem nenhum tipo de interferência do sistema. Serve para abrigar imagens, folhas de estilo (CSS), scripts e outros tipos de arquivos de conteúdo estático. 
  
  Salvo indicação em contrário o conteúdo das reportagens, este código é licenciado em WTFPL.
