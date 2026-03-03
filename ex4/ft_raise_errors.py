
def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    """
    植物の健康状態をチェックする関数。

    植物名・水分量・日照時間が適切かを確認し、
    不正な値があれば ValueError を発生させる。
    すべての条件を満たしている場合は、
    植物が健康であることを示すメッセージを返す。

    Args:
        plant_name (str): チェック対象となる植物の名前
        water_level (int): 植物に与えられている水分量
        sunlight_hours (int):植物が受けている日照時間（時間）

    Raises:
        ValueError: 植物名が空の場合
        ValueError: 水分量が許容最大値を超えている場合
        ValueError: 日照時間が許容最小値を下回っている場合

    Returns:
        str:植物が健康であることを示すメッセージ
    """
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if not (1 <= water_level <= 10):
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if not (2 <= sunlight_hours <= 12):
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """
    check_plant_health 関数の動作を確認するテスト関数。

    正常な入力値と、不正な入力値（植物名・水分量・日照時間）
    をそれぞれ与え、例外が正しく発生・処理されるかを確認する。
    """
    print("=== Garden Plant Health Checker ===")
    print()

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 6))

    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 6)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 9, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("All error raising tests completed!")


# if __name__ == "__main__":
#    test_plant_checks()
