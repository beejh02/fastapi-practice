import asyncio

# 비동기 함수 정의
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# 비동기 코드 실행
async def main():
    await asyncio.gather(say_hello(), say_hello())  # 두 개의 코루틴을 동시에 실행

# 프로그램 실행
asyncio.run(main())