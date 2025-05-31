from PIL import Image


def main():
    img_path = "assets/logo.png"
    try:
        img = Image.open(img_path)
        img.show()  # OS標準の画像ビューアで表示
        print(f"画像 '{img_path}' を読み込みました。サイズ: {img.size}")
    except FileNotFoundError:
        print(f"画像ファイル '{img_path}' が見つかりませんでした。")


if __name__ == "__main__":
    main()
