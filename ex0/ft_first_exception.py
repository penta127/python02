
def check_temperature(temp_str: str):
    """
    文字列で与えられた温度をチェックして、植物に適した範囲かを判定する。

    ・数値に変換できない場合はエラーを表示する
    ・0℃未満または40℃を超える場合は、適切でない温度としてエラーを出す
    ・適切な温度の場合は正常メッセージを表示する

    Args:
        temp_str (str): 温度を表す文字列（例: "25", "-5", "abc"）

    Raises:
        ValueError: 温度が数値に変換できない場合
        ValueError: 温度が植物に適さない範囲（0℃未満、40℃超）の場合
    """
    print()
    print(f"Testing temperature: {temp_str}")
    try:
        x = int(temp_str)
        if x > 40:
            raise ValueError(f"{x}°C is too hot for plants (max 40°C)")
        if x < 0:
            raise ValueError(f"{x}°C is too cold for plants (min 0°C)")

        print(f"Temperature {x}°C is perfect for plants!")

    except ValueError as temper:
        if not temp_str.lstrip("-").isdigit():
            print(f"Error: '{temp_str}' is not a valid number")
        else:
            print(f"Error: {temper}")


def test_temperature_input():
    """
    動作確認用テスト
    """
    print("=== Garden Temperature Checker ===")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")

# if __name__ == "__main__":
#    test_temperature_input()
