
class GardenError(Exception):
    """
    庭に関する問題を表すカスタム例外の基底クラス。

    植物や水やりなど、庭全体に関わるエラーの共通の親クラスとして使用する。
    個別の庭関連エラーは、このクラスを継承して定義される。
    """
    pass


class PlantError(GardenError):
    """
    植物に関する問題を表すカスタム例外。

    植物が枯れている、成長状態が異常であるなど、
    植物に関するエラーを表現するために使用する。
    """
    pass


class WaterError(GardenError):
    """
    水やりに関する問題を表すカスタム例外。

    水が不足している、または水やりに問題がある場合に
    発生させるエラーを表現するために使用する。
    """
    pass


def ft_custom_errors():
    """
    カスタム例外（GardenError, PlantError, WaterError）の
    動作を確認するデモ用関数。

    各例外を意図的に raise し、
    ・PlantError を個別に捕捉できること
    ・WaterError を個別に捕捉できること
    ・GardenError を使って、すべての庭関連エラーを
    まとめて捕捉できること
    を順番に確認する。

    例外が発生しても try / except によって処理され、
    プログラムが途中で停止せず最後まで実行されることを示す。
    """
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print()
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print()
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print()
    print("All custom error types work correctly!")


# if __name__ == "__main__":
#    ft_custom_errors()
