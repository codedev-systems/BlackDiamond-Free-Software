<h2>O que é o BlackDiamond?</h2>
<p>O BlackDiamond é um sistema simples que automatiza a geração de documentos contábeis. Todos os cálculos necessários, assim como a geração e formatação do documento, são realizados de forma automática, facilitando e agilizando todo o processo de criação do documento e evitando falhas humanas.</p>

<h2>Documentos Contábeis</h2>
<p>O BlackDiamond trabalha com 3 tipos de documentos financeiros:</p>
<ul>
  <li>DRE (Demonstrativo de Resultado do Exercício): exibe os resultados de uma organização em um certo período, exibindo informações como receita bruta, receita líquida, lucro bruto, lucro operacional e lucro líquido.</li>
  <li>BP (Balanço Patrimonial): contém informações patrimoniais da empresa, exibindo todos seus ativos, passivos e o seu patrimônio líquido.</li>
  <li>DFC (Demonstrativo de Fluxo de Caixa): documento que registra todas as entradas e saídas de caixa de uma companhia em um determinado período.</li>
</ul>

<h2>Interface Simples</h2>
<p>A interface simples do BlackDiamond permite que o usuário faça uso de suas funcionalidades sem nenhuma dificuldade, bastando selecionar o tipo de documento que ele quer trabalhar por meio do menu lateral esquerdo e preencher todas as informações solicitadas via formulário, com toda parte mais complexa sendo realizada pelo BlackDiamond.</p>

<h2>Geração do Documento</h2>
<p>Ao final de todo processo é gerado um documento PDF contendo informações de acordo com o tipo de documento selecionado e com os dados passados via formulário. O nome do arquivo e a localização onde será salvo na máquina são de escolha do usuário.</p>

<h2>Geração do arquivo executável por meio dos scripts</h2>
<p>Para gerar o arquivo executável (.exe) do programa por dos scripts Python (.py), use do seguinte comando:</p>
<pre>pyinstaller --version-file=version.txt --name="BlackDiamond" --icon=images\icon.ico --hidden-import=babel.numbers --additional-hooks-dir=. --onefile --windowed main.py</pre>
<p><strong>OBS.: o executável do programa deve estar jundo do diretório /images.</strong></p>
