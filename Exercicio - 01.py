from Biblioteca import ContaBancaria

Usuario01 = ContaBancaria(1, "ze", "poupança")
Usuario01.verificarSaldo()
Usuario01.ativarContar()
Usuario01.verificarSaldo()
Usuario01.ajustarLimite(1000)
Usuario01.sacarValor(200)
Usuario01.verificarSaldo()
Usuario01.depositar(300)
Usuario01.verificarSaldo()