# int 정수 float 실수 str 문자 bool 참 또는 거짓  

# box_num에 숫자만 넣자는 약속을 했어요 누군가 한글 표기법으로 숫자를 넣었습니다.

# box_num = "하나"
# box_num += 1
# print(box_num)
# type(box_num)

# int -> float 형변환

# print(float(5))
# print(int(5.0))

# 나이 = 10
# type(나이)
# # print(dir(나이))
# print(나이.bit_length())
# print(bin(나이))


#list, tuple, cdict, set 
# 이름 = "팡팡팡"
# 나이 = 35
# # 키 = 165.7
# 소속 = "s본부"

# # print(type(이름))
# # print(type(나이))
# # print(type(키))
# # print(type(소속))

# # print(float(5))
# # print(int(5.0))
# # print("5", "5.0")
# # print(type("5"), type("5.0"))

# #str: 문자열
# #특징: 스퀀스 자료형
# #시퀀스란? 요소들이 연속적으로 이어진 자료형 
# #값 하나하나를 요소라고 합니다.

# #0 인덱스
# print(소속)
# print(소속[0])
# print(소속[1])
# print(소속[2])
# print(소속[3])
# print(소속[4])
# print(소속[5])

# 옛날게임 = "바니바니 당근당근"*20
# print(옛날게임)
# print("본" in 소속)

# 퀴즈 = "차 4대가 고장나면? 카포에라"
# print(퀴즈[12:16])
# print(퀴즈[12:15])
# print(퀴즈[-1])

# 생년월일="2000.12.25"
# 년=생년월일[0:4]
# 월=생년월일[5:7]
# 일=생년월일[8:11]
# print(f'{년}, {월}, {일}')

# 숫자= "129145890435845"
# print(숫자[::])
# print(숫자[::-1]) #순서 반대로
# #첫 번째 인덱스 기준으로 2칸씩 띄어쓰기 출력하기
# print(숫자[::2])

퀴즈="스님이 공중에 뜬다를 4글자로 말하면? 어중이떠중이"
print(퀴즈[22:28])

라라랜드="사람들은 다른 사람들의 열정에 끌리게 되어있어 자신이 잊은 걸 상기시켜 주니까"
print(라라랜드[4:15])