def water_plants(plant_list):
    """
    植物リストを順番に水やりする関数。

    水やりシステムを開始し、渡された植物リストの各要素に対して
    水やり処理を行う。
    無効な植物（None）が含まれている場合はエラーを発生させるが、
    エラーの有無に関わらず、必ず後処理として
    水やりシステムを終了（クリーンアップ）する。

    Args:
        plant_list (list):水やり対象の植物名を格納したリスト

    Raises:
        ValueError: 植物名が None の場合に発生する
    """
    success = True
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        success = False
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")
        if success:
            print("Watering completed successfully!")


def test_watering_system():
    """
    water_plants 関数の動作確認を行うテスト関数。

    正常な植物リストを使った場合と、
    エラー（None を含む）を発生させた場合の両方を実行し、
    finally ブロックによるクリーンアップ処理が
    常に実行されることを確認する。
    """
    print("=== Garden Watering System ===")
    print()
    print("Testing normal watering...")
    normal_plants = ["tomato", "lettuce", "carrots"]
    water_plants(normal_plants)
    print()
    print("Testing with error...")
    error_plants = ["tomato", None, "carrots"]
    water_plants(error_plants)
    print()
    print("Cleanup always happens, even with errors!")

# if __name__ == "__main__":
#    test_watering_system()
