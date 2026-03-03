
def garden_operations():
    """
    Pythonの代表的な例外処理をデモンストレーションする。
    以下の例外を、意図的に発生させて try / except で捕捉する。

    ValueError :
        不正な値が与えられた場合に発生する例外。
        例として、数値を期待する処理に文字列を渡すケースを扱う。

    ZeroDivisionError :
        0で割り算を行った場合に発生する例外。
        数値としては正しいが、計算として不可能な操作を示す。

    FileNotFoundError :
        存在しないファイルを読み込みモードで開こうとした場合に発生する例外。
        OSレベルの「ファイルが存在しない」エラーに対応する。

    KeyError :
        辞書に存在しないキーへアクセスした場合に発生する例外。
        データ構造に対する不正な参照を示す。

    また、複数の例外を1つの except 節でまとめて捕捉する例も示し、
    例外が発生してもプログラムが最後まで実行されることを確認する。

    """

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print()

    print("Testing ZeroDivisionError...")
    try:
        10/0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print()

    print("Testing FileNotFoundError...")
    try:
        open("koito.txt", "r")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print()

    print("Testing KeyError...")
    try:
        dictionary = {"itou": 1, "kouki": 2}
        print(dictionary["koito"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print()

    print("Testing multiple errors together...")
    try:
        int("abc")
        10 / 0
        open("koito.txt", "r")
        dictionary = {"itou": 1, "kouki": 2}
        print(dictionary["koito"])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print()
    print("All error types tested successfully!")


def test_error_types():
    """
    arden_operations 関数を実行し、各種例外処理の動作を確認する。

    プログラムの開始メッセージを表示した後、
    garden_operations を呼び出して、すべての例外処理が
    正しく行われることを確認するためのテスト用関数。
    """
    print("=== Garden Error Types Demo ===")
    print()
    garden_operations()

# if __name__ == "__main__":
#    test_error_types()
