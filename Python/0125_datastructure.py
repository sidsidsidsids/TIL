#주어진 문자열에서 숫자 문자 기호가 각각 몇개인지를 판단하는 함수 작성해보세요
def check(target_str):
    pass
    l_count=0;n_count=0;count=0
    for i in target_str:
        if i.isdecimal() == True:
            n_count += 1
        elif i.isalpha() == True:
            l_count += 1
        else :
            count += 1
    return print(f'문자 : {l_count}개, 숫자 : {n_count}개, 기호 : {count}개')

check('q!1')
#문자 : 개, 숫자 : 개, 기호 : 개