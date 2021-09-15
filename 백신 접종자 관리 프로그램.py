# 프로그램 시작 시 Notice.
print("######### 백신 접종자 관리 프로그램 실행 #########")
print("1. 오늘 접종 할 인원.")
print("2. 접종 예정자의 나이.")
print("3. 접종 예정자의 금일 1차, 2차접종 여부를 기입하세요.\n")

# 총 접종인원에 맞게 for문 행동
total_number = int(input("오늘 접종 예정자 인원수를 입력해주세요: " ))

# 입력 연령대, 접종 차수 검증 리스트
allow_age = [10, 20, 30, 40, 50, 60]
allow_cls = [1, 2]

# 각 연령대별 총원 파라미터 초기화
total_10age = 0
total_20age = 0
total_30age = 0
total_40age = 0
total_50age = 0
total_60age = 0

# 1차접종 완료자, 2차접종 완료자 총원 파라미터 초기화
total_1st = 0
total_2nd = 0

# 접종자 관리 프로그램 시작.
for cycle in range(0,total_number):
    while True:
        age = int(input("접종 예정자 연령대를 입력해주세요(10대:10, 20대:20 ~ 60대:60): " ))
        classification = int(input("해당 접종 예정자는 오늘 1차접종인가요, 2차 접종인가요? (1차:1, 2차:2): " ))
        if (age in allow_age) != True or (classification in allow_cls) != True: # 입력한 접종 예정자 연령대가 연령대 검증리스트에 없거나, 접종 차수가 접종 차수 검증리스트에 없을 경우 noti 후 무시
            print("해당 입력값의 형식이 올바르지 않습니다. 다시 시도해주세요.\n")
            continue
        else: # 접종예정자 연령대와 접종 차수 입력값이 정상적일 경우
            if age == 10: # 10대일 경우
                if classification == 1: # 1차 접종자일 경우
                    total_1st += 1 # 1차 접종자 총원에 ++
                else: # 2차 접종자일 경우
                    total_2nd += 1 # 2차 접종자 총원에 ++
                total_20age += 1 # 10대 인원 총원에 ++
                break # for문 1회 count
            
            elif age == 20:
                if classification == 1:
                    total_1st += 1
                else:
                    total_2nd += 1
                total_20age += 1
                break

            elif age == 30:
                if classification == 1:
                    total_1st += 1
                else:
                    total_2nd += 1
                total_30age += 1
                break

            elif age == 40:
                if classification == 1:
                    total_1st += 1
                else:
                    total_2nd += 1
                total_40age += 1
                break

            elif age == 50:
                if classification == 1:
                    total_1st += 1
                else:
                    total_2nd += 1
                total_50age += 1
                break

            else:
                if classification == 1:
                    total_1st += 1
                else:
                    total_2nd += 1
                total_60age += 1
                break
    print("다음 인원의 접종데이터를 DB에 입력합니다.\n")
    
print("전체 인원 %d명의 DB 입력이 완료되었습니다.\n" %total_number)
print("전체 인원의 연령대는 다음과 같습니다.")
print("10대 접종자의 총 인원수는 %d명 입니다." %total_10age)
print("20대 접종자의 총 인원수는 %d명 입니다." %total_20age)
print("30대 접종자의 총 인원수는 %d명 입니다." %total_30age)
print("40대 접종자의 총 인원수는 %d명 입니다." %total_40age)
print("50대 접종자의 총 인원수는 %d명 입니다." %total_50age)
print("60대 접종자의 총 인원수는 %d명 입니다. \n" %total_60age)
print("전체 접종자의 접종 차수는 다음과 같습니다.")
print("1차 접종자의 총 인원수는 %d명 입니다." %total_1st)
print("2차 접종자의 총 인원수는 %d명 입니다." %total_2nd)
print("######### 백신 접종자 관리 프로그램 종료 #########")


