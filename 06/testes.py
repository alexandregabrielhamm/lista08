from funcoes import *


def teste_verificar_carbono_resultado_false():
    result = verificar_conteudo_carbono(10)
    assert not result


def teste_verificar_carbono_resultado_true():
    result = verificar_conteudo_carbono
    assert result

def teste_verificar_dureza_false():
     result = verificar_dureza_rockwell(10)
     assert not result


def teste_verificar_dureza_true():
    result = verificar_dureza_rockwell(100)
    assert result


def test_verificar_resistencia_false():
    result = verificar_resistencia_tracao(1000)
    assert not result


def test_verificar_resistencia_true():
    resultado = verificar_resistencia_tracao(100000)
    assert resultado


def test_caulcular_grau_aco(mocker):
    mock_verificar_conteudo_carbono = mocker.patch("funcoes.verificar_conteudo_carbono")
    mock_verificar_conteudo_carbono.return_value = True

    mock_verificar_dureza_rockwell = mocker.patch("funcoes.verificar_dureza_rockwell")
    mock_verificar_dureza_rockwell.return_value = True

    mock_verificar_resistencia_tracao = mocker.patch("funcoes.verificar_resistencia_tracao")
    mock_verificar_resistencia_tracao.return_value = True

    # act
    grau_aco = calcular_grau(5, 75, 85000)

    #assert
    mock_verificar_conteudo_carbono.assert_called_with(5)
    mock_verificar_dureza_rockwell.assert_called_with(75)
    mock_verificar_resistencia_tracao.assert_called_with(85000)

    assert grau_aco == 10
