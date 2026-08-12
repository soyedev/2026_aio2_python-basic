name = "alice"
age = int(input("나이를 입력하세요: "))

print(f"이름: {name}, 나이: {age}")

def calculate_sum(a, b):
    result = a + b
    return result

result = calculate_sum(3, 5)

if result > 0:
    print("양수입니다")