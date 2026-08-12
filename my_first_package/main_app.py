# 방법 1: 모듈을 별명으로 가져오기
import magic_calc.basic_ops as myops

# 방법 2: 모듈 전체 가져오기
import magic_calc.advanced_ops

# 방법 3: 필요한 함수만 직접 가져오기
from magic_calc.basic_ops import multiply, divide
from magic_calc.advanced_ops import power

# 방법 1: 별명을 사용해서 함수 실행
# result = magic_calc.basic_ops.add(10,5)
result = myops.add(10,5)
print(result)

# 방법 2: 모듈 이름을 사용해서 함수 실행
result1 = magic_calc.advanced_ops.sqrt(10)
print(f"10+5={result} 10의 제곱근은 {result1}입니다.")

# 방법 3: 필요한 함수만 직접 가져와서 사용
print("\n--- 방법 3: multiply, divide, power 직접 사용 ---")
result_mul = multiply(7, 8)
print(f"7 * 8 = {result_mul}")

result_div = divide(10, 2)
print(f"10 / 2 = {result_div}")

result_power = power(2, 3)
print(f"2의 3제곱 = {result_power}")
