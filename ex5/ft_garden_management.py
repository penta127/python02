

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


class GardenManager:
    """
    庭の管理を行うクラス。

    植物の追加、植物への水やり、植物の健康チェックなどの基本操作を提供する。
    例外クラス（GardenError など）を使って異常系を表現する。
    """
    def __init__(self):
        """
        GardenManager を初期化する。

        Attributes:
            plants (list[str]): 登録済みの植物名のリスト。
        """
        self.plants = []

    def add_plant(self, plant_name):
        """
        GardenManager を初期化する。

        Attributes:
            plants (list[str]): 登録済みの植物名のリスト。
        """
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self, plant_list):
        """
        指定された植物リストに水やりを行う。

        水やりシステムのオープン/クローズを模擬し、finally で後処理を保証する。
        リストに None が含まれる場合は WaterError を発生させる。

        Args:
            plant_list (list[str | None]): 水やり対象の植物名のリスト。

        Raises:
            WaterError: plant_list に None が含まれる場合。
                ※このメソッド内で捕捉してログ表示するため、呼び出し元へは通常伝播しない。
        """
        print("Watering plants...")
        try:
            print("Opening watering system")
            for plant in plant_list:
                if plant is None:
                    raise WaterError("Cannot water None - invalid plant!")
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
        self,
        plant_name: str,
        water_level: int,
        sunlight_hours: int
    ):
        """
        植物の健康状態を簡易チェックする。

        入力値が許容範囲内であれば「healthy」として表示する。
        範囲外の場合は、状況に応じて GardenError 系例外を送出する。

        ルール:
            - plant_name は空でないこと
            - water_level は 1〜10 の範囲
            - sunlight_hours は 2〜12 の範囲

        Args:
            plant_name (str): チェック対象の植物名。
            water_level (int): 水量レベル（想定: 1〜10）。
            sunlight_hours (int): 日照時間（想定: 2〜12）。

        Raises:
            PlantError: plant_name が空/None の場合。
            WaterError: water_level が 1〜10 の範囲外の場合。
            GardenError: sunlight_hours が 2〜12 の範囲外の場合。
        """
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        if not (1 <= water_level <= 10):
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        if not (2 <= sunlight_hours <= 12):
            raise GardenError(
                f"Sunlight hours {sunlight_hours}"
                " is too low (min 2)")
        print(
            f"{plant_name}: healthy (water: {water_level},"
            f" sun: {sunlight_hours})")

    def error_recovery(self):
        """
        エラー発生を模擬するメソッド。

        テスト用に WaterError を必ず送出し、呼び出し側で例外処理・復旧を確認できるようにする。

        Raises:
            WaterError: 常に送出される（タンクの水不足を想定）。
        """
        raise WaterError("Not enough water in tank")


def ft_garden_management():
    """
    GardenManager の動作確認を行うテスト関数。

    以下を順に実行して、通常系と例外処理の挙動を確認する:
        1) 植物の追加（空文字で PlantError を発生させる）
        2) 登録済み植物への水やり
        3) 健康チェック（不正な water_level で GardenError 系例外を確認）
        4) error_recovery による例外発生と復旧メッセージの表示
    """
    print("=== Garden Management System ===")
    print()
    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato")
        garden.add_plant("lettuce")
        garden.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")
    print()
    garden.water_plants(garden.plants)
    print()
    print("Checking plant health...")
    try:
        garden.check_plant_health("tomato", 5, 8)
        garden.check_plant_health("lettuce", 15, 8)
    except GardenError as e:
        print(f"Error checking lettuce: {e}")
    print()
    print("Testing error recovery...")
    try:
        garden.error_recovery()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print()
    print("Garden management system test complete!")


# if __name__ == "__main__":
#    ft_garden_management()
