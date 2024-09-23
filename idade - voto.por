programa
{
	
	funcao inicio()
	{ 
		inteiro idade
		
		escreva("por gentileza, digita sua idade: ")
			leia(idade)
			
		se(idade<16){
			escreva("Voto ainda não permitido")
		} senao se(idade>=16 e idade<18){
			escreva("Voto facultativo")
		} senao se(idade>=18 e idade<70){
			escreva("Voto obrigatório")
		} senao {
			escreva("voto facultativo para pessoas acima de 70 anos")
		}















	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 56; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */