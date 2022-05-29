import pytest
def cal(bit_count, rate):
    if not isinstance(bit_count, int):
        raise TypeError('Error: bit_count must be a int')
    elif not isinstance(rate, float):
        raise TypeError('Error: rate must be a float')

    return bit_count * rate

def test_calc_func_default():
    assert cal(50, 10.0) == 500

def test_cal_func_exception():
    test_case = {
        "Ошибка rate must be float" :  {
            "input_data" : (50,"10"),
            "result" : "Error: rate must be a float"
        },
        "Ошибка  bit_count be int" :  {
            "input_data" : ("50.0",10.0),
            "result" : "Error: bit_count must be a int",
        },
    }

    for i in test_case:
        bit_count, rate =  test_case[i]["input_data"]
        with pytest.raises(TypeError, match=test_case[i]["result"]):
            cal(bit_count, rate)


def main():
    bit_count, rate = "50", 100

    cal(bit_count, rate)


if __name__ == "__main__":
    try:
        main()
    except TypeError as err:
        print('Ошибка типа данных' ,err)